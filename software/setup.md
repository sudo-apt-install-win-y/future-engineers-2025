# How to setup the robot for code
Firstly you need to complete building the robot [here](/hardware/howtobuild.md)
## 1. Flash the SD Card
To get started you will need to flash the micro SD card that will be inserted into the Raspberry Pi
First go to [the raspberry pi downloads page](https://www.raspberrypi.com/software/) and download raspberry pi imager for your OS.
Then install the imager.
Open it. Insert the micro SD Card into your computer. Choose your model of pi on the app. choose full desktop environment. choose the microsd card. click flash. 

## 2. Setup the Pi
plug the microsd into your pi. turn it on. set up the pi by following the onscreen instructions. access the pi's terminal using ssh or a monitor and keybaord.

## 2. Run setup.sh
First you need to get the setup.sh code from its public github.
<pre>curl https://github.com/sudo-apt-install-win-y/setup-script/blob/main/setup.sh</pre>
Now you need to just run the bash file and everything should install.
<pre>bash setup.sh</pre>