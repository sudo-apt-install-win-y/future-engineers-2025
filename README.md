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
Our robot is built like a normal RWD (Rear Wheel Drive) car you find in everyday life. This means it has two wheels at the rear of the robot which provide drive. At the front of the robot there are two wheels which provide steering functionality. The rear axle is powered by a single DC motor with external gears.

## 2. Power and Sense Management
### Power
We use 3 18650 batteries to provide 10.8 - 11.1 volts to our motor driver board. The motor driver board powers our DC Motor and Servo. To power our Raspberry Pi 4 B we have 2 more 18650 Batteries in a Waveshare UPS Hat B. This provides a stable power source to our Pi at 7.2 - 7.4 volts directly onto the Pi's power rails through Pogo Pins.

### Sensors
Our robot has 4 VL53L0X Time of Flight sensors situated with 2 on either side of our robot to give us the distances between the walls and our robot. Using these we also determine a rough angle of our robot by looking at the distances at the front and the back of our robot.

Instead of these Time of Flights we would have preffered a lidar to detect the walls however our club wouldn't buy one for us.

The robot is also equiped with a Raspberry Pi Camera 3 Regular Angle (76 degrees) to see the red and green obstacles in round 2. 

Our robot has a Gyro and accelorometer sensor (MPU60-50). We do not use the Accelorometer, we just use the Gyro to determine the angle of the robot. 

Finally we have a colour sensor to detect the orange and blue lines on the mat to know when to take the corner.

## 3. Obstacle Management


## 4. Pictures -- Team and Vehicle


## 5. Performance Videos


## 6. GitHub Utilisation
