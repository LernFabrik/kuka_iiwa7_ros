# kuka_plc_ros

|Branch    |  ROS Distro  |  Status   | GitHub Action |
|----------|--------------|-----------|---------------|
|master    |  Melodic     |[![Build Status](https://travis-ci.org/prachandabhanu/kuka_plc_ros.svg?branch=master)](https://travis-ci.org/prachandabhanu/kuka_plc_ros)| ![CI](https://github.com/prachandabhanu/kuka_plc_ros/workflows/CI/badge.svg?branch=master) |

### Instalation
```
cd ~/catkin_ws/src
wstool init
wstool merge <path>/kuka_ros.rostinstall
wstool --delete-changed-uris up
```