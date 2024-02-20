#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

rospy.init_node("Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x300")

pub2 = rospy.Publisher("chatter",String,queue_size=10)


def fw():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= 0.0
    pub.publish(cmd)
    pub2.publish("fw")
        
def bw():
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z= 0.0
    pub.publish(cmd)
    pub2.publish("bw")
       
def lt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= AngularVel.get()
    pub.publish(cmd)
    pub2.publish("lt")
   
def rt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= -AngularVel.get()
    pub.publish(cmd)
    pub2.publish("rt")
    
LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1) # 1 is defult value for scale
LinearVel.pack()

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1) # 1 is defult value for scale
AngularVel.pack()

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=120)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=230)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=180)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=180)

frame.mainloop()    
    
    
    
