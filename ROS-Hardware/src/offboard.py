#! /usr/bin/env python3

# import rospy
# from geometry_msgs.msg import PoseStamped
# from mavros_msgs.msg import State
# from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
# import keyboard
# from std_msgs.msg import String

# current_state = State()
# pose = PoseStamped()

# def state_cb(msg):
#     global current_state
#     current_state = msg

# def position_cb(msg):
#     global current_position
#     current_position = msg


# #if __name__ == "__main__":


# def control_Drone(key):
#     print(key)
#     global current_position
#     current_position = key.data
#     # Setpoint publishing MUST be faster than 2Hz
#     rate = rospy.Rate(20)
#     # Wait for Flight Controller connection
#     # keys_pressed = keyboard.read_event(suppress=True).name.split(' ')

#     while(not rospy.is_shutdown() and not current_state.connected):
#         rate.sleep()
#         print('Not Connected')
    
#     print('Connected')
    
    

#     #set the pos.position.x to current position.x


#     pose.pose.position.x = current_position.pose.position.x
#     pose.pose.position.y = current_position.pose.position.y
#     pose.pose.position.z = current_position.pose.position.z
#     # Send a few setpoints before starting
#     for i in range(100):
#         if(rospy.is_shutdown()):
#             break
#         local_pos_pub.publish(pose)
#         rate.sleep()
    
#     offb_set_mode = SetModeRequest()
#     offb_set_mode.custom_mode = 'OFFBOARD'
    
#     arm_cmd = CommandBoolRequest()
#     arm_cmd.value = True
#     last_req = rospy.Time.now()
    
#     try:
#         while not rospy.is_shutdown():
#             if key == 'w':
#                 pose.pose.position.z += 5
#                 print(pose.pose.position.z)
#     except Exception as e:
#         print(e)
    

#     while(not rospy.is_shutdown()):
#         print('Connected')
#         if(current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
#             if(set_mode_client.call(offb_set_mode).mode_sent == True):
#                 rospy.loginfo("OFFBOARD enabled")
#             last_req = rospy.Time.now()
#         else:
#             if(not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
#                 if(arming_client.call(arm_cmd).success == True):
#                     rospy.loginfo("Vehicle armed")
#                 last_req = rospy.Time.now()
#         print(f"The position is {pose.pose.position.z}")
#         local_pos_pub.publish(pose)
#         rate.sleep()




# rospy.init_node("offb_node_py")

# state_sub = rospy.Subscriber("/mavros/state", State, callback = state_cb)
# local_pos_pub = rospy.Publisher("/mavros/setpoint_position/local", PoseStamped, queue_size=10)
# local_pos_sub = rospy.Subscriber("/mavros/setpoint_position/local", PoseStamped, callback = position_cb)

# middleware_sub = rospy.Subscriber("/middleware/control", String, control_Drone)
# rospy.wait_for_service("/mavros/cmd/arming")
# arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)

# rospy.wait_for_service("/mavros/set_mode")
# set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)


# rospy.spin()
# import airsim #pip install airsim

# #for car use CarClient() 
# client = airsim.MultirotorClient()


# responses = client.simGetImages([
# airsim.ImageRequest("0", airsim.ImageType.DepthVis),  #depth visualization image
# airsim.ImageRequest("1", airsim.ImageType.DepthPerspective, True), #depth in perspective projection
# airsim.ImageRequest("1", airsim.ImageType.Scene), #scene vision image in png format
# airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGBA array
# print('Retrieved images: %d' % len(responses[0].image_data_uint8))
# print(responses[0])

# import airsim

# import pprint
# import tempfile
# import os
# import time

# import cv2
# import numpy as np

# client = airsim.VehicleClient()

# responses = client.simGetImages([
#     airsim.ImageRequest("0", airsim.ImageType.DepthVis),  #depth visualization image
#     airsim.ImageRequest("1", airsim.ImageType.DepthPerspective, True), #depth in perspective projection
#     airsim.ImageRequest("1", airsim.ImageType.Scene), #scene vision image in png format
#     airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGBA array
# print('Retrieved images: %d' % len(responses))


# for idx, response in enumerate(responses):



#     if response.pixels_as_float:
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
#         #airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
#     elif response.compress: #png format
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#         #airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
#     else: #uncompressed array
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#         img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) # get numpy array
#         img_rgb = img1d.reshape(response.height, response.width, 3) # reshape array to 4 channel image array H X W X 3

#         #test run ay 7aga#!/usr/bin/env python3


# import rospy
# from geometry_msgs.msg import PoseStamped
# from mavros_msgs.msg import State
# from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
# from pynput import keyboard as kb
# from std_msgs.msg import String


# current_state = State()

# def state_cb(msg):
#     global current_state
#     current_state = msg

# def position_cb(msg):
#     global current_position
#     current_position = msg

# def increase_altitude():
#     global pose
#     pose.pose.position.z += 1
#     local_pos_pub.publish(pose)


# def decrease_altitude():
#     global pose
#     pose.pose.position.z -= 1
#     local_pos_pub.publish(pose)

# def move_left():
#     global pose
#     pose.pose.position.x -= 1
#     local_pos_pub.publish(pose)

# def move_right():
#     global pose
#     pose.pose.position.x += 1
#     local_pos_pub.publish(pose)


# def on_press(key):
#     print(key)
#     if key.data == 'w':
#         increase_altitude()
#     elif key.data == 's':
#         decrease_altitude()
#     elif key.data == 'a':
#         move_left()
#     elif key.data == 'd':
#         move_right()

# if __name__ == "__main__":
#     rospy.init_node("offb_node_py")
#     state_sub = rospy.Subscriber("/mavros/state", State, callback=state_cb)
#     local_pos_pub = rospy.Publisher("/mavros/setpoint_position/local", PoseStamped, queue_size=10)
#     local_pos_sub = rospy.Subscriber("/mavros/setpoint_position/local", PoseStamped, callback = position_cb)

#     rospy.wait_for_service("/mavros/cmd/arming")
#     arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
#     rospy.wait_for_service("/mavros/set_mode")
#     set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
#     middleware_sub = rospy.Subscriber("/middleware/control", String, on_press)



#     rate = rospy.Rate(20)

#     while not rospy.is_shutdown() and not current_state.connected:
#         rate.sleep()
#         print('Not Connected')
#     print('Connected')

#     pose = PoseStamped()
#     pose.pose.position.x = 0
#     pose.pose.position.y = 0
#     pose.pose.position.z = 12

#     for i in range(100):
#         if rospy.is_shutdown():
#             break
#         local_pos_pub.publish(pose)
#         rate.sleep()

#     offb_set_mode = SetModeRequest()
#     offb_set_mode.custom_mode = 'OFFBOARD'
#     arm_cmd = CommandBoolRequest()
#     arm_cmd.value = True
#     last_req = rospy.Time.now()

#     # Create a listener for keyboard input
#     listener = kb.Listener(on_press=on_press)
#     listener.start()

#     while not rospy.is_shutdown():
#         print('Connected')

#         if current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0):
#             if set_mode_client.call(offb_set_mode).mode_sent:
#                 rospy.loginfo("OFFBOARD enabled")
#             last_req = rospy.Time.now()
#         else:
#             if not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0):
#                 if arming_client.call(arm_cmd).success:
#                     rospy.loginfo("Vehicle armed")
#                 last_req = rospy.Time.now()
        
        
#         rate.sleep()

#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
from pynput import keyboard as kb
from std_msgs.msg import String


current_state = State()

def state_cb(msg):
    global current_state
    current_state = msg

def position_cb(msg):
    global current_position
    current_position = msg

def increase_altitude():
    global pose
    pose.pose.position.z += 1
    local_pos_pub.publish(pose)


def decrease_altitude():
    global pose
    pose.pose.position.z -= 1
    local_pos_pub.publish(pose)

def move_left():
    global pose
    pose.pose.position.x -= 1
    local_pos_pub.publish(pose)

def move_right():
    global pose
    pose.pose.position.x += 1
    local_pos_pub.publish(pose)


def on_press(key):
    print(key)
    if key.data == 'w':
        increase_altitude()
    elif key.data == 's':
        decrease_altitude()
    elif key.data == 'a':
        move_left()
    elif key.data == 'd':
        move_right()

if __name__ == "__main__":
    rospy.init_node("offb_node_py")
    state_sub = rospy.Subscriber("/mavros/state", State, callback=state_cb)
    local_pos_pub = rospy.Publisher("/mavros/setpoint_position/local", PoseStamped, queue_size=10)
    local_pos_sub = rospy.Subscriber("/mavros/setpoint_position/local", PoseStamped, callback = position_cb)

    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
    middleware_sub = rospy.Subscriber("/middleware/control", String, on_press)



    rate = rospy.Rate(20)

    while not rospy.is_shutdown() and not current_state.connected:
        rate.sleep()
        print('Not Connected')
    print('Connected')

    pose = PoseStamped()
    pose.pose.position.x = 0
    pose.pose.position.y = 0
    pose.pose.position.z = 12

    for i in range(100):
        if rospy.is_shutdown():
            break
        local_pos_pub.publish(pose)
        rate.sleep()

    offb_set_mode = SetModeRequest()
    offb_set_mode.custom_mode = 'OFFBOARD'
    arm_cmd = CommandBoolRequest()
    arm_cmd.value = True
    last_req = rospy.Time.now()

    # Create a listener for keyboard input
    listener = kb.Listener(on_press=on_press)
    listener.start()

    while not rospy.is_shutdown():
        print('Connected')
        if current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0):
            if set_mode_client.call(offb_set_mode).mode_sent:
                rospy.loginfo("OFFBOARD enabled")
            last_req = rospy.Time.now()
        else:
            if not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0):
                if arming_client.call(arm_cmd).success:
                    rospy.loginfo("Vehicle armed")
                last_req = rospy.Time.now()
            
        
        rate.sleep()
        rospy.spin()