# not odroid_ws
ros simulation scripts for iarc mission using iris with optical flow, lpe and px4 flight stack.

## Setup Intructions 
```
git clone https://github.com/px4/Firmware.git
cd Firmware
make posix_sitl_lpe gazebo_iris_opt_flow
```
edit necessary files
```
source Tools/setup_gazebo.bash $(pwd) $(pwd)/build_posix_sitl_lpe
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo
roslaunch px4 mavros_posix_sitl.launch
```

## Changelog
```
v1 ellipse detection with single onboard cam
v2 ellipse detection with two onboard cam
v3 ellipse detection and offboard surveillance script fireup from single launch
v4 object detection and following scripts added
```

## Notes
```
the gazebo camera plugin which is edited into iris_opt_flow.sdf publishes a ros node, check topic names here ( replaces usb_cam node during simulation runs)

```
