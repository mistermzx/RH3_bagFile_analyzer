#UNIT C-3: Exercise: Analyze bag files
## URL for repository:
https://github.com/mistermzx/rh3_bagfile_analyzer
(added surirohit as collaborator)
## Instructions to reproduce results:
1. Place .bag files in /data folder
..1. example_rosbag_H3.bag 
..2. amod19-rh3-ex-record-MartinZiranXu.bag
2. Build image:
dts devel build -f --arch amd64
3. Run docker container:
..1. For example .bag file:
docker run -it --rm  -v ~/Documents/rh3_bagfile_analyzer:/home -e BAGFILE_PATH=/home/data/example_rosbag_H3.bag duckietown/rh3_bagfile_analyzer:v1-amd64
..2. For recorded .bag file (lane following):
docker run -it --rm  -v ~/Documents/rh3_bagfile_analyzer:/home -e BAGFILE_PATH=/home/data/amod19-rh3-ex-record-MartinZiranXu.bag duckietown/rh3_bagfile_analyzer:v1-amd64
