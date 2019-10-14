# UNIT C-3: Exercise: Analyze bag files
## URL for repository:
https://github.com/mistermzx/rh3_bagfile_analyzer
(added surirohit as collaborator)
## Instructions to reproduce results:
1. Place .bag files in /data folder
  * example_rosbag_H3.bag 
  * amod19-rh3-ex-record-MartinZiranXu.bag

2. Build image:
```shell
dts devel build -f --arch amd64
```

3. Run docker container:
 * For example .bag file:
```shell
docker run -it --rm  -v ~/Documents/rh3_bagfile_analyzer:/home -e BAGFILE_PATH=/home/data/example_rosbag_H3.bag duckietown/rh3_bagfile_analyzer:v1-amd64
```
 * For recorded .bag file (lane following):
```shell
docker run -it --rm  -v ~/Documents/rh3_bagfile_analyzer:/home -e BAGFILE_PATH=/home/data/amod19-rh3-ex-record-MartinZiranXu.bag duckietown/rh3_bagfile_analyzer:v1-amd64
```
## Results
Terminal Output:
  * example_rosbag_H3.bag 
```shell
/tesla/camera_node/camera_info:
 num_messages: 653
 period:
     min: 0.014833
     max: 0.052063
     average: 0.033308
     median: 0.033248

/tesla/line_detector_node/segment_list:
 num_messages: 198
 period:
     min: 0.078026
     max: 0.171424
     average: 0.109110
     median: 0.104937
/tesla/wheels_driver_node/wheels_cmd:
 num_messages: 74
 period:
     min: 0.022158
     max: 4.163808
     average: 0.261137
     median: 0.112478
```
  * amod19-rh3-ex-record-MartinZiranXu.bag
```shell
/duckiepopstar/camera_node/image/compressed:

 num_messages: 871
 period:
     min: 0.012813
     max: 0.055679
     average: 0.033277
     median: 0.033271
/duckiepopstar/wheels_driver_node/wheels_cmd:
 num_messages: 343
 period:
     min: 0.028119
     max: 0.265192
     average: 0.079504
     median: 0.072142
```
