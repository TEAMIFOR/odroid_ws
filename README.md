# odroid_ws

```
git clone https://github.com/TEAMIFOR/odroid_ws.git
cd odroid_ws
chmod 755 launcher.sh
. ./launcher.sh
```
Sole prurpose of this repo is to act as primary package for the odroid system as to complete the mission. So please keep the master branch clean, for adding new features and scripts which are imcompatible (ie, scripts without ros implementation, scripts with harcoded values, scripts to test stuff) commit to a new branch and submit a pull request. In case the developer missed any important points or harcoded some values, then it can be fixed in the pull request and pull request can be accepted to add features to master branch.
TODO: necessary cleanup required

## Changelog
```
v1 single rospackage to run ellipse detection(python) and offboard demo(cpp) together
```

## Notes
```
default image input camera at /dev/video0, can be changed inside usb_cam launchfile, also to be changed under missionpkg launchfile
calibrate camera first (rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.108 image:=/usb_cam/raw_image camera:=/usb_cam
```
