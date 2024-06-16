# pavucontrol_System_Icon
A simple python script that creats an icon in your system tray which gives you the option of opening pavucontrol with one click. Pavucontrol is an audio management program. 

##Setup
###Make sure you have what you need
```bash
sudo apt update
sudo apt install python3 python3-pip pavucontrol xdotool
pip3 install pystray pillow
```
###Make the script executable
```bash
chmod +x volume_control.py
```
###Adding to startup applications
Create a .desktop file:
```bash
mkdir -p ~/.config/autostart
nano ~/.config/autostart/volume_control.desktop
```
Then add the following content to the file:
```ini
[Desktop Entry]
Type=Application
Exec=/path/to/your/volume_control.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Volume Control
Comment=Start Volume Control Tray Icon
```
Replace /path/to/your/volume_control.py with the full path to your script.

Reboot your system to ensure functionality
