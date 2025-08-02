import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import board
import busio
import digitalio
from picamera2 import Picamera2
import adafruit_tcs34725

# Set up I2C communication
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the TCS34725 color sensor
sensor = adafruit_tcs34725.TCS34725(i2c)

IN1 = 17
IN2 = 27
ENA = 18
servo = 12


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

pwm2 = GPIO.PWM(ENA, 100)
pwm = GPIO.PWM(servo, 50)
pwm2.start(0)
pwm.start(0)

def forward(speed=100):
    """Rotate motor forward."""
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm2.ChangeDutyCycle(speed)

def reverse(speed=100):
    """Rotate motor backward."""
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm2.ChangeDutyCycle(speed)

def stop():
    """Stop the motor."""
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(0)

def coast():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

def set_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(servo, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo, False)
    pwm.ChangeDutyCycle(0)

def read_colour():
    """Read color from the TCS34725 sensor."""
    r, g, b = sensor.color_rgb_bytes
    return r, g, b

# Initialize the camera
picam2 = Picamera2()
# Configure the camera
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
# Start the camera
picam2.start()

while True:
    lap_count = 0
    last_corner = None
    # Main loop
    while lap_count < 3:
        # Capture frame
        frame = picam2.capture_array()

    # Convert to HSV for color filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    # Define green color range in HSV
    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80, 255, 255])
    # Define red color ranges in HSV (adjusted for lower light)
    lower_red1 = np.array([0, 70, 50])    # Lower saturation and value thresholds
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])  # Lower saturation and value thresholds
    upper_red2 = np.array([180, 255, 255])
    
    # Create masks for green, red, and purple objects
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Combine masks for all objects
    mask_all = cv2.bitwise_or(mask_green, mask_red)
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(mask_all, (7, 7), 0)
    # Apply morphological operations to clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(blurred, cv2.MORPH_CLOSE, kernel)
    # Use morph as binary image for contours
    thresh = morph
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    
    if contours:
        # Find the largest contour
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        M = cv2.moments(largest)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            # Draw the center
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            # Determine position
            width = frame.shape[1]
            if cx < width // 3:
                position = "Left"
            elif cx < 2 * width // 3:
                position = "Center"
            else:
                position = "Right"

            # Determine color of the tracked object (red or green only)
            color = "Unknown"
            if mask_green[cy, cx] > 0:
                color = "Green"
            elif mask_red[cy, cx] > 0:
                color = "Red"

            cv2.putText(frame, f"{color} {position}", (cx, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

            forward(30)
            if color == "Red" and position == "Right":
                set_angle(120)
            if color == "Red" and position == "Center":
                set_angle(100)
            if color == "Red" and position == "Left":
                set_angle(90)
            if color == "Green" and position == "Right":
                set_angle(90)
            if color == "Green" and position == "Center":
                set_angle(80)
            if color == "Green" and position == "Left":
                set_angle(60)

            # Use color sensor for cornering
            r, g, b = read_colour()
            # Simple blue/orange detection (tune thresholds as needed)
            if b > r and b > g and b > 100:  # Blue detected
                if last_corner != 'blue':
                    lap_count += 1
                    print(f'Lap {lap_count}: cornering left (blue detected)')
                    last_corner = 'blue'
                forward(30)
                time.sleep(0.2)
                set_angle(60)
                time.sleep(1)
                set_angle(90)
                forward(20)
            elif r > g and r > b and r > 100 and g > 50 and b < 50:  # Orange detected (tune as needed)
                if last_corner != 'orange':
                    lap_count += 1
                    print(f'Lap {lap_count}: cornering right (orange detected)')
                    last_corner = 'orange'
                forward(30)
                time.sleep(0.2)
                set_angle(120)
                time.sleep(1)
                set_angle(90)
                forward(20)

            # Print all relevant data
            print(f"Object color: {color}, position: {position}, center: ({cx}, {cy}), area: {area}, Sensor RGB: ({r}, {g}, {b})")
        # Flip the frame upside down and side to side for display
        flipped_display = cv2.flip(frame, -1)
        cv2.imshow("Frame", cv2.cvtColor(flipped_display, cv2.COLOR_RGB2BGR))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    picam2.stop()
    cv2.destroyAllWindows()
    GPIO.cleanup()