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
 *For example .bag file:
```shell
docker run -it --rm  -v ~/Documents/rh3_bagfile_analyzer:/home -e BAGFILE_PATH=/home/data/example_rosbag_H3.bag duckietown/rh3_bagfile_analyzer:v1-amd64
```
 *For recorded .bag file (lane following):
```shell
docker run -it --rm  -v ~/Documents/rh3_bagfile_analyzer:/home -e BAGFILE_PATH=/home/data/amod19-rh3-ex-record-MartinZiranXu.bag duckietown/rh3_bagfile_analyzer:v1-amd64
```

