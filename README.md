# WRO 2025 - Future Engineers  
## Team Name: sudo apt install win -y

---

## 1. Mobility Management

Our vehicle is built on a custom 4-wheeled chassis. The front wheels are linked to a **servo-driven steering mechanism**, while the rear wheels are powered by a **single DC motor connected to a rear axle**. This setup ensures the robot adheres to the WRO rules against differential drive. The vehicle is front-steered using a standard PWM-controlled servo motor, allowing smooth angle control between 60° and 120°.

We selected rubber-treaded wheels for traction and mounted the chassis low for better center of gravity and stability during turns. Steering angles are software-controlled to adapt to obstacle or color-based navigation scenarios.

We use a PWM-controlled motor driver with GPIO inputs `IN1`, `IN2`, and `ENA` to control speed and direction. The drivetrain was tested to work optimally between 20%–40% duty cycle for consistent track movement without wheel slip.

---

## 2. Power and Sensor Management

### Power System:
The robot is powered using a 7.4V Li-ion battery connected to a voltage regulator module supplying 5V and 3.3V rails. Servo and motor are powered through separate power lines to prevent brownouts. The Raspberry Pi 4 is powered independently through USB-C.

### Sensors:
- **4x VL53L0X Time-of-Flight Distance Sensors**: Front-facing, placed at slight angles to cover left and right forward directions, used for wall following and PID correction.
- **TCS34725 Color Sensor**: Mounted downward to detect blue and orange track corner markers.
- **PiCamera2**: Used in the Obstacle Challenge to detect red and green traffic signs and determine direction.
- **All sensors communicate over I2C**, with careful use of shutdown pins to avoid address conflicts.

The color sensor is used continuously during track following to detect corners based on blue/orange shades, while the camera handles high-level object detection during the obstacle challenge.

---

## 3. Obstacle Strategy (Algorithm & Code Logic)

### Open Challenge (Round 1):
- The robot drives forward using a low-speed PID wall-following algorithm using VL53L0X sensors.
- Color readings from the TCS34725 are used to detect blue or orange markers.
- On detecting **blue**, the robot turns left (60°), and on **orange**, it turns right (120°).
- The PID logic is dynamic and corrects steering while driving based on left/right distance sensor values.

### Obstacle Challenge (Round 2):
- The camera captures frames and converts them to HSV for color filtering.
- Red and green traffic signs are detected using pixel thresholding and position tracking.
  - **Red on Right**: turn hard right (120°)
  - **Red Center**: turn slightly right (100°)
  - **Green on Left**: turn hard left (60°)
  - **Green Center**: adjust left (80°)
- Lap count is tracked using blue/orange corner detection via the color sensor.
- After 3 laps, the robot is programmed to slow down and attempt parking.

### Sample PID Snippet:
```python
error = distance1 - distance2
output = Kp * error + Ki * integral + Kd * derivative
steering_angle = 90 + output
steering_angle = max(40, min(120, steering_angle))
set_angle(steering_angle)
