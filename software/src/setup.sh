#!/bin/bash
echo "               __                 __    _          __       ____         _                   ____    __          
  ___ __ _____/ /__    ___ ____  / /_  (_)__  ___ / /____ _/ / / _    __(_)__    ______ __  / __/__ / /___ _____ 
 (_-</ // / _  / _ \  / _ `/ _ \/ __/ / / _ \(_-</ __/ _ `/ / / | |/|/ / / _ \  /___/ // / _\ \/ -_) __/ // / _ \
/___/\_,_/\_,_/\___/  \_,_/ .__/\__/ /_/_//_/___/\__/\_,_/_/_/  |__,__/_/_//_/      \_, / /___/\__/\__/\_,_/ .__/
                         /_/                                                       /___/                  /_/    "

echo "This script will install the everything you need to run our code."

# ------- Clone Repo -------
echo "Cloning the repository..."
cd ~/
git clone https://github.com/sudo-apt-install-win-y/WRO2025-FE-sudoaptinstallwin-y.git
cd WRO2025-FE-sudoaptinstallwin-y/software

# ------- Installs Python packages -------
echo "Installing Python packages..."
if [ -f requirements.txt ]; then
    echo "Installing Python dependencies..."
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
else
    echo "No requirements.txt found, skipping pip installs."
fi
echo "Environment setup complete."

# ------- Installs the button_watcher.py script -------
echo "Setting up button_watcher service..."
cd ~/WRO2025-FE-sudoaptinstallwin-y/software/
sudo cp $PWD/button_watcher/button_watcher.py /usr/local/bin/button_watcher.py
chmod +x /usr/local/bin/button_watcher.py
sudo cp $PWD/button_watcher/button_watcher.service /etc/systemd/system/button_watcher.service
sudo systemctl daemon-reload
sudo systemctl enable button_watcher.service
sudo systemctl start button_watcher.service
echo "button_watcher service is set up and running."
echo "Setup complete. You can now use the software. Press the button once to put the robot into hold mode, and press it again to start the round1 program. Press to exit the running program, this will return the robot to hold mode. Once in hold mode, long press to run the round2 program."