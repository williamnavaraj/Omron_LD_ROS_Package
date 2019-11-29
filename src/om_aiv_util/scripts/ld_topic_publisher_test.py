#!/usr/bin/env python
## publishes std_msgs/Strings messages
## to the 5 ld_status topics
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from om_aiv_util.msg import Location
import math
import numpy as np
import socket
import threading
import time
import re
import sys
BUFFER_SIZE = 2056
#import socketconnection class to connect to robot
#requires socketconnection_class.py file in the same folder
from socketconnection_class import ConnectSocket
connecttcp = ConnectSocket()
s = connecttcp.sock
#get ip adress and port from launch file
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")

# ip_address = "172.21.5.123"
# port = 7171
connecttcp.connect(str(ip_address), port)
rospy.init_node('ld_topic_publisher', anonymous=True)

def applicationFaultQuery(command, command2, text):
    #specify topic name
    topic_name = "ldarcl_{}".format(command)
    pub = rospy.Publisher(topic_name, String, queue_size=10)
    #specify node name
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Running command: ", command
    #send command to arcl
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        # currtime = time.time()   # 5 minutes from now
        # print currtime
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "End of {}".format(command2) in rcv:
                break
            if "Unknown command {}".format(command) in rcv:
                rospy.logerr(rcv)
                return rcv
            else:
                # print time.time()
                # if time.time() - currtime > TIMEOUT:
                #     break
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
                # print rcv
    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if "{}:".format(command) in line:
            cmd = line.split("{}:".format(command))
            #print required data
            rospy.loginfo(",{}:".format(command).join(cmd)[1:])
            #publish data
            pub.publish(''.join(cmd))
            break
        #if there are no faults print "Np faults"
        if "{}:".format(command) not in line:
            rospy.loginfo(text)
            pub.publish(text)
            # rate.sleep()

def faultsGet(command, command2, text):
    pub = rospy.Publisher('ldarcl_faultsGet', String, queue_size=10)
    print(Style.RESET_ALL)
    print(Fore.YELLOW)
    print "Getting list of faults..."
    command = "faultsGet"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)

        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "End of FaultList" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)

                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'FaultList:' in line:
            faultsGet = line.split("FaultList:")
            rospy.loginfo(",FaultList:".join(faultsGet)[1:])
            pub.publish(''.join(faultsGet))
            # rate.sleep()
            break
        if 'FaultList:' not in line:
            rospy.loginfo("No faults")
            pub.publish("No faults")
            # rate.sleep()

def getDateTime():
    pub = rospy.Publisher('ldarcl_getDateTime', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting date and time..."
    command = "getDateTime"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "DateTime:" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'DateTime:' in line:
            getDateTime = line.split("DateTime:")
            rospy.loginfo(",DateTime:".join(getDateTime)[1:])
            pub.publish(''.join(getDateTime))
            # rate.sleep()

def getGoals():
    pub = rospy.Publisher('ldarcl_getGoals', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print "Getting list of goals found in current map..."
    command = "getGoals"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "End of goals" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'Goal:' in line:
            getGoals = line.split("Goal:")
            rospy.loginfo(",Goal:".join(getGoals)[1:])
            pub.publish(''.join(getGoals))
            # rate.sleep()

def getMacros():
    pub = rospy.Publisher('ldarcl_getMacros', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of macros found in current map..."
    command = "getMacros"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "End of macros" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'Macro:' in line:
            getMacros = line.split("Macro:")
            rospy.loginfo(",Macro:".join(getMacros)[1:])
            pub.publish(''.join(getMacros))
            # rate.sleep()

def getRoutes():
    pub = rospy.Publisher('ldarcl_getRoutes', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of route names found in current map..."
    command = "getRoutes"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "End of routes" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'Route:' in line:
            getRoutes = line.split("Route:")
            rospy.loginfo(",Route:".join(getRoutes)[1:])
            pub.publish(''.join(getRoutes))
            # rate.sleep()

def odometer():
    pub = rospy.Publisher('ldarcl_odometer', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting odometer readings..."
    command = "odometer"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "Odometer:" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'Odometer:' in line:
            odometer = line.split("Odometer:")
            rospy.loginfo(",Odometer:".join(odometer)[1:])
            pub.publish(''.join(odometer))
            # rate.sleep()

def oneLineStatus():
    pub = rospy.Publisher('ldarcl_oneLineStatus', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting one line status..."
    command = "oneLineStatus"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "Status:" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'Status:' in line:
            oneLineStatus = line.split("Status:")
            rospy.loginfo(",Status:".join(oneLineStatus)[1:])
            pub.publish(''.join(oneLineStatus))
            # rate.sleep()

def queryDockStatus():
    pub = rospy.Publisher('ldarcl_queryDockStatus', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting docking/charging status..."
    command = "queryDockStatus"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "DockingState:" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'DockingState:' in line:
            queryDockStatus = line.split("DockingState:")
            rospy.loginfo(",DockingState:".join(queryDockStatus)[1:])
            pub.publish(''.join(queryDockStatus))
            # rate.sleep()

def queryFaults():
    pub = rospy.Publisher('ldarcl_queryFaults', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting faults..."
    command = "queryFaults"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "EndQueryFaults" in rcv:
                break
            if "End of FaultList" in rcv:
                break
            if "Unknown command queryfaults" in rcv:
                break
                pass
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
                pass


    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'RobotFaultQuery:' in line:
            queryDockStatus = line.split("RobotFaultQuery:")
            rospy.loginfo(",RobotFaultQuery:".join(queryDockStatus)[1:])
            pub.publish(''.join(queryDockStatus))
            # rate.sleep()
        else:
            pass

def queryMotors():
    pub = rospy.Publisher('ldarcl_queryMotors', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting state of robot motors..."
    command = "queryMotors"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "Motors" in rcv:
                break
            if "EStop" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'Motors' in line:
            queryMotors = line.split("Motors")
            rospy.loginfo(",Motors".join(queryMotors)[1:])
            pub.publish(''.join(queryMotors))
            # rate.sleep()
        if 'EStop' in line:
            queryMotors = line.split("Estop")
            rospy.loginfo(",Estop".join(queryMotors)[1:])
            pub.publish(''.join(queryMotors))
            # rate.sleep()

def queueShowRobotLocal():
    pub = rospy.Publisher('ldarcl_queueShowRobotLocal', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting status of robot..."
    command = "queueShowRobotLocal"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "EndQueueShowRobot" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'QueueRobot:' in line:
            queueShowRobotLocal = line.split("QueueRobot:")
            rospy.loginfo(",QueueRobot:".join(queueShowRobotLocal)[1:])
            pub.publish(''.join(queueShowRobotLocal))
            # rate.sleep()

def waitTaskState():
    pub = rospy.Publisher('ldarcl_waitTaskState', String, queue_size=10)
    # rospy.init_node('ld_topic_publisher', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting status of wait task..."
    command = "waitTaskState"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "WaitState:" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'WaitState:' in line:
            waitTaskState = line.split("WaitState:")
            rospy.loginfo(",WaitState:".join(waitTaskState)[1:])
            pub.publish(''.join(waitTaskState))
            # rate.sleep()


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            applicationFaultQuery('ApplicationFaultQuey', 'ApplicationFaultQuery: No Faults')
            faultsGet()
            getDateTime()
            getGoals()
            getMacros()
            getRoutes()
            odometer()
            oneLineStatus()
            queryDockStatus()
            # queryFaults()
            queryMotors()
            queueShowRobotLocal()
            waitTaskState()

    except rospy.ROSInterruptException:
        pass
