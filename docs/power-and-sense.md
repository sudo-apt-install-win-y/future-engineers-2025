## Power and Sense Management
### Power
We use 3 18650 batteries to provide 10.8 - 11.1 volts to our motor driver board. The motor driver board powers our DC Motor and Servo. To power our Raspberry Pi 4 B we have 2 more 18650 Batteries in a Waveshare UPS Hat B. This provides a stable power source to our Pi at 7.2 - 7.4 volts directly onto the Pi's power rails through Pogo Pins.

### Time of Flight Sensors
Our robot has 4 VL53L0X Time of Flight sensors situated with 2 on either side of our robot to give us the distances between the walls and our robot. Using these, we also determine a rough angle of our robot by looking at the distances at the front and the back of our robot.

Instead of these Time of Flights, we would have preferred a lidar to detect the walls; however, our club wouldn't buy one for us.

### Camera
The robot is also equipped with a Raspberry Pi Camera 3 Regular Angle (76 degrees) to see the red and green obstacles in round 2. 

### Direction Sensing
Our robot has a Gyroscope and accelerometer sensor (MPU60-50). We do not use the Accelerometer; we just use the Gyroscope to determine the angle of the robot. 

### Color sensing
Finally, we have a colour sensor to detect the orange and blue lines on the mat to know when to take the corner.
