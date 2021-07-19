# kuka_plc_ros

|Branch    |  ROS Distro  |  Status   | GitHub Action | Azure Pipeline | 
|----------|--------------|-----------|---------------|----------------|
|master    |  Melodic     |[![Build Status](https://travis-ci.org/prachandabhanu/kuka_plc_ros.svg?branch=master)](https://travis-ci.org/prachandabhanu/kuka_plc_ros),[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FLernFabrik%2Fkuka_iiwa7_ros.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FLernFabrik%2Fkuka_iiwa7_ros?ref=badge_shield) | ![CI](https://github.com/prachandabhanu/kuka_plc_ros/workflows/CI/badge.svg?branch=master) | [![Build Status](https://dev.azure.com/IWT-Digitization/BuildEnv/_apis/build/status/LernFabrik.kuka_iiwa7_ros?branchName=master&stageName=Catkin%20Build&jobName=ubuntu&configuration=ubuntu%20MELODIC)](https://dev.azure.com/IWT-Digitization/BuildEnv/_build/latest?definitionId=12&branchName=master)|
| Master   |  Noetic      |    NAN    |    NAN        |[![Build Status](https://dev.azure.com/IWT-Digitization/BuildEnv/_apis/build/status/LernFabrik.kuka_iiwa7_ros?branchName=master&stageName=Catkin%20Build&jobName=ubuntu&configuration=ubuntu%20NOETIC)](https://dev.azure.com/IWT-Digitization/BuildEnv/_build/latest?definitionId=12&branchName=master)|

### License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FLernFabrik%2Fkuka_iiwa7_ros.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FLernFabrik%2Fkuka_iiwa7_ros?ref=badge_large)

### Instalation
```
cd ~/catkin_ws/src
wstool init
wstool merge <path>/kuka_ros.rostinstall
wstool --delete-changed-uris up
```

# How to start
**++** represent new terminal.
1. **++** `roscore`
2. **++** `iwtros_launch iiwa_description.launch`
3. **++** `wsg_50_tcp_driver test.launch`
4. **++** `iwtros_lauch iwtros_env.lauch``
5. **++** `kuka_control plc_control_node.py`
6. Start the programm in Conveyor belt system
7. Finally **++** `kuka_control control.launch`
