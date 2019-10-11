import rosbag
bag = rosbag.Bag('example_rosbag_H3.bag')
for topic, msg, t in bag.read_messages(topics=['chatter', 'numbers']):
    print msg
bag.close()
