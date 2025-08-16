# sudo apt install win -y - WRO 2025 Future Engineers
**Category:** Future Engineers - Self-Driving Cars

**Team:** DJ_Theron, TheGuyInTheRedSuit

**Coach:** Jarret Williams

**Country:** South Africa

## Table of contents
### [Mobility Management](/docs/mobility-manegement.md)
### [Power and Sense Management](/docs/power-and-sense.md)
### [Obstacle Management](/docs/obstacle-management.md)
### [Pictures](/docs/images/)
### [Performance Videos](/videos/demo-vids.md)
### [3D Models](/hardware/3d_models/)
### [Source Code](/software/src/)
### [How to build the robot](/hardware/howtobuild.md)
### [How to setup the robot to run code](/software/setup.md)
### [BOM (Bill Of Materials)](/hardware/bom/bill-of-materials.csv)
### [Schematics](/hardware/schematics/)

---

## Hardware Overview
At the heart of our robot is a main processor that runs all operations, a [Raspberry pi 4B 2GB](/docs/images/component_photos/RaspberryPi4B.jpg). Our robot has a Rear wheel drive and front wheel steering system (Ackermann) which allows for easy turning and motion. Rubber tires are utilised for grip they provide. The chassis explained earlier's RWD function is powered by a singular 12V DC brushed motor, Steering functionality is provided by a 12V servo motor connected. 
( _An in depth mobility manegement document can be found [here](/docs/mobility-manegement.md)_ )
The robot uses four time of flight sensors (VL53l0x), one colour sensor (tcs34725) and one Raspbery Pi Camera v3 to achive sensor fusion and computer vision. The Pi is powered by a Waveshare UPS HAT B, which contains 2 18650 batteries. The motors are powered by 3 18650 Batteries. Everything connects to a central ground. ( _An in depth power and sensing document can be found [here ](/docs/power-and-sense.md)_)
## Software Architecture
We used python