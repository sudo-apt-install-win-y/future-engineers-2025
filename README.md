# sudo apt install win -y Engineering journal
## Table of contents
### [Mobility Management](#1-mobility-management)
### [Power and Sense Management](#2-power-and-sense-management)
### [Obstacle Management](#3-obstacle-management)
### [Pictures](#4-pictures----team-and-vehicle)
### [Performance Videos](#5-performance-videos)
### [Github Ultilisation](#6-github-utiliaation)
### [3D Models](/models)
### [Source Code](/src)

---
## 1. Mobility Management
### Drivetrain type
Our robot is built like a normal RWD (Rear Wheel Drive) car you find in everyday life. This means it has two wheels at the rear of the robot, which provide drive. At the front of the robot, two wheels provide steering functionality. 
### Rear Drive Assembly
The rear axle is powered by a single 12V DC motor with external gears, which speeds the robot up to allow for faster driving around the board. These gears connect to a simple but reliable rear axle, which is held in place by two ball bearings on either side of the robot. These connect to two thick and grippy rubber wheels that provide strong traction to the board mat.
### Front Drive Assembly
The front wheels are not powered to provide traction but are used for steering to navigate obstacles, turn corners, and parallel park the robot. We used a standard 12V 180-degree servo motor to turn a certain amount or continue straight. The steering rack utilises Ackermann steering geometry to make sure that turns are taken properly, accounting for wheels on the inside and outside of a turn needing to trace out circles of different radii (since the inner wheel takes a tighter path while the outer wheel takes a wider path).
(insert image here of it)

## 2. Power and Sense Management
### Power
We use 3 18650 batteries to provide 10.8 - 11.1 volts to our motor driver board. The motor driver board powers our DC Motor and Servo. To power our Raspberry Pi 4 B we have 2 more 18650 Batteries in a Waveshare UPS Hat B. This provides a stable power source to our Pi at 7.2 - 7.4 volts directly onto the Pi's power rails through Pogo Pins.

### Sensors
Our robot has 4 VL53L0X Time of Flight sensors situated with 2 on either side of our robot to give us the distances between the walls and our robot. Using these, we also determine a rough angle of our robot by looking at the distances at the front and the back of our robot.

Instead of these Time of Flights, we would have preferred a lidar to detect the walls; however, our club wouldn't buy one for us.

The robot is also equipped with a Raspberry Pi Camera 3 Regular Angle (76 degrees) to see the red and green obstacles in round 2. 

Our robot has a Gyroscope and accelerometer sensor (MPU60-50). We do not use the Accelerometer; we just use the Gyroscope to determine the angle of the robot. 

Finally, we have a colour sensor to detect the orange and blue lines on the mat to know when to take the corner.

## 3. Obstacle Management


## 4. Pictures -- Team and Vehicle


## 5. Performance Videos


## 6. GitHub Utilisation
