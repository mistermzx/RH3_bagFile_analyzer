# Template: template-ros

This template provides a boilerplate repository
for developing ROS-based software in Duckietown.

**NOTE:** If you want to develop software that does not use
ROS, check out [this template](https://github.com/duckietown/template-basic).


## How to use it

### 1. Fork this repository

Use the fork button in the top-right corner of the github page to fork this template repository.


### 2. Create a new repository

Create a new repository on github.com while
specifying the newly forked template repository as
a template for your new repository.


### 3. Define dependencies

List the dependencies in the files `dependencies-apt.txt` and
`dependencies-py.txt` (apt packages and pip packages respectively).


### 4. Place your code

Place your ROS packages in the directory `/packages` of
your new repository.

**NOTE:** Do not use absolute paths in your code,
the code you place under `/packages` will be copied to
a different location later.


### 5. Setup the launchfile

Change the file `launch.sh` in your repository to
launch your code.

### How to execute
# build
dts devel build -f --arch amd64
# run
docker run -it --rm  -v ~/Documents/rh3_bagfile_analyzer:/home -e BAGFILE_PATH=/home/data/example_rosbag_H3.bag duckietown/rh3_bagfile_analyzer:v1-amd64
docker run -it --rm  -v ~/Documents/rh3_bagfile_analyzer:/home -e BAGFILE_PATH=/home/data/laneFollowing_rh3.bag duckietown/rh3_bagfile_analyzer:v1-amd64
