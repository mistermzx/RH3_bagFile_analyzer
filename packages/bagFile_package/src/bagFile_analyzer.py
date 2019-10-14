import rosbag
import os
import numpy as np

file_input = os.environ['BAGFILE_PATH']
bag = rosbag.Bag(file_input)
my_topics = bag.get_type_and_topic_info()[1].keys()
n_topics = len(my_topics)

for j in range(n_topics):
    t_vec = list()
    n_messages = 0;
    for topic, msg, t in bag.read_messages(topics=my_topics[j]):
        n_messages += 1
        t_vec.append(t.to_time()) #converted time from rospy.rostime.Time to float (in sec)

    dt_array = np.zeros(n_messages-1)
    for i in range(n_messages-1):
        dt_array[i] = t_vec[i+1]-t_vec[i]

    print (my_topics[j]+":")
    print(' num_messages: {:d}').format(n_messages)
    print(' period:')
    print('     min: {:f}').format(np.min(dt_array))
    print('     max: {:f}').format(np.max(dt_array))
    print('     average: {:f}').format(np.mean(dt_array))
    print('     median: {:f}').format(np.median(dt_array))



# for topic, msg, t in bag.read_messages(topics=my_topics):
#     print topic

bag.close()
