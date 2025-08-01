import RPi.GPIO as GPIO
import time
import board
import busio
import digitalio
import adafruit_vl53l0x

IN1 = 17
IN2 = 27
ENA = 18
servo = 12

Kp = 9
Ki = 0
Kd = 4

error = 0
current_time = 0
integral = 1
last_time = time.time()
dt = 0
steering_angle = 90
output = 0
last_error = 1

turncounterleft = 0
turncounterright = 0

sensor1 = None
sensor2 = None
sensor3 = None
sensor4 = None

distance1 = 0
distance2 = 0
distance3 = 0
distance4 = 0

sensor_addresses = [0x30, 0x31, 0x32, 0x33]
sensor_shutdown_pins = [board.D5, board.D6, board.D13, board.D26]
sensors = []

turningright = False
turningleft = False


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

def setupsensors():
    global sensors
    print("Setting up 4 sensors...")
    
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Create and shutdown all sensors
    xshuts = []
    for pin in sensor_shutdown_pins:
        x = digitalio.DigitalInOut(pin)
        x.direction = digitalio.Direction.OUTPUT
        x.value = False
        xshuts.append(x)

    time.sleep(0.1)

    for i, xshut in enumerate(xshuts):
        xshut.value = True
        time.sleep(0.1)
    
        sensor = adafruit_vl53l0x.VL53L0X(i2c)
        sensor.set_address(sensor_addresses[i])
        time.sleep(0.1) 
    
        # Reconnect all sensors using new addresses
    sensors = [
        adafruit_vl53l0x.VL53L0X(i2c, address=addr)
        for addr in sensor_addresses
    ]
    print("All sensors ready.")

def get_distance(index):
    if 0 <= index < len(sensors):
        return sensors[index].range
    return -1  # Error value

def setup():
    setupsensors()
    set_angle(90)

def get_distances():
    global distance1, distance2, distance3, distance4
    distance1 = get_distance(0)
    distance2 = get_distance(1)
    distance3 = get_distance(2)
    distance4 = get_distance(3)
    distance1 = distance1 / 10
    distance2 = distance2 / 10
    distance3 = distance3 / 10
    distance4 = distance4 / 10

def pidleft():
    get_distances()
    global distance1, distance2, distance3, distance4
    global last_time, last_error, current_time, error, integral
    global integral

    current_time = time.time()
    dt = current_time - last_time

    error = distance1 - distance2
    integral += error * dt
    derivative = (error - last_error) / dt

    output = Kp * error + Ki * integral + Kd * derivative

    steering_angle = 90 + output
    steering_angle = max(40, min(120, steering_angle))

    set_angle(steering_angle)

    last_error = error
    last_time = current_time

def pidright():
    get_distances()
    global distance1, distance2, distance3, distance4
    global last_time, last_error, current_time, error, integral

    current_time = time.time()
    dt = current_time - last_time

    error = distance3 - distance4
    integral += error * dt
    derivative = (error - last_error) / dt

    output = Kp * error + Ki * integral + Kd * derivative

    steering_angle = 90 + output
    steering_angle = max(40, min(120, steering_angle))

    set_angle(steering_angle)

    last_error = error
    last_time = current_time

setup()
forward(20)
while True:
    while True:
        pidleft()
        print(distance1, distance3)
        if distance1 > 100:
            turncounterleft += 1

        elif distance3 > 100:
            turncounterright += 1
        
        if turncounterleft == 3:
            turncounterleft = 0
            print('cornering left')
            forward(30)
            time.sleep(0.2)
            set_angle(60)
            time.sleep(1)
            set_angle(90)
            forward(20)
            break

        elif turncounterright == 3:
            turncounterright = 0
            print('cornering right')
            forward(30)
            time.sleep(0.2)
            set_angle(120)
            time.sleep(1)
            set_angle(90)
            forward(20)
            break

        time.sleep(0.05)

    if turningleft == True:
        while True:
            pidleft()
            if distance1 > 70:
                turncounterleft += 1

            if turncounterleft == 3:
                forward(30)
                time.sleep(0.2)
                set_angle(60)
                time.sleep(1)
                set_angle(90)
                forward(20)
                
            time.sleep(0.05)
        
    elif turningright == True:
        while True:
            pidright()
            if distance3 > 70:
                turncounterright += 1
            
            if turncounterright == 3:
                forward(30)
                time.sleep(0.2)
                set_angle(60)
                time.sleep(1)
                set_angle(90)
                forward(20)
            
            time.sleep