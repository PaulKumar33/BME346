# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:30:37 2018

@author: paulk
"""

import serial 
import matplotlib.pyplot as plt
import numpy as np
import win32com.client

connected = False

wmi = win32com.client.GetObject("winmgmts:")
for port in wmi.InstancesOf("Win32_SerialPort"):
    if "Arduino" in port.Name:
        comPort = port.DeviceID
        print(comPort, "Is Arduino")
        
ser = serial.Serial(comPort, 9600)

while not connected:
    serin = ser.read()
    connected = True
    
plt.ion()

length = 500

#init empty variables

x = [0]*length
y = [0]*length
z = [0]*length


xline, = plt.plot(x)
yline, = plt.plot(y)
zline, = plt.plot(y)
plt.ylim(-10, 10)

for i in range(length):
    data = ser.readline()
    sep = data.split()
    
    x.append(float(sep[0]))
    y.append(float(sep[1]))
    z.append(float(sep[2]))
    
    del x[0]
    del y[0]
    del z[0]
    
    xline.set_xdata(np.arange(len(x)))
    yline.set_xdata(np.arange(len(y)))
    zline.set_xdata(np.arange(len(z)))
    
    xline.set_