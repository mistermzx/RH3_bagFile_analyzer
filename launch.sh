#!/bin/bash

set -e

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------
# roscore &
# sleep 5
# rosrun bagFile_package bagFile_analyzer.py
cd /home
python ./packages/bagFile_package/src/bagFile_analyzer.py
