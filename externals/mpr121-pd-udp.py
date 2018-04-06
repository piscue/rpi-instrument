# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Modified by: piscue 20180406
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import time

#for pdsend
#import os

# read gpio
import wiringpi

import Adafruit_MPR121.MPR121 as MPR121
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 3000
sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP

# Create MPR121 instance.
cap = MPR121.MPR121()
cap2 = MPR121.MPR121()

# WiringPI setup
wiringpi.wiringPiSetup()
switch1_old = 0
switch2_old = 0
switch3_old = 0
switch4_old = 0

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

if not cap2.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# Alternatively, specify a custom I2C address such as 0x5B (ADDR tied to 3.3V),
# 0x5C (ADDR tied to SDA), or 0x5D (ADDR tied to SCL).
cap2.begin(address=0x5C)

# Also you can specify an optional I2C bus with the bus keyword parameter.
#cap.begin(busnum=1)

# def for sending messages
def send2Pd(message=''):
    sock.sendto(message, (UDP_IP, UDP_PORT))

# Main loop to print a message every time a pin is touched.
print('Press Ctrl-C to quit.')
last_touched = cap.touched()
last_touched2 = cap2.touched()
while True:
    current_touched = cap.touched()
    current_touched2 = cap2.touched()

    ### 4 Switches
    switch1 = wiringpi.digitalRead(4)
    switch2 = wiringpi.digitalRead(5)
    switch3 = wiringpi.digitalRead(2)
    switch4 = wiringpi.digitalRead(3)
    if switch1 != switch1_old:
        #print ("sw 1: " + str(switch1))
        switch1_old = switch1
        message = 'sw 1 ' + str(switch1)
        send2Pd (message)
    if switch2 != switch2_old:
        switch2_old = switch2
        message = 'sw 2 ' + str(switch2)
        send2Pd (message)
    if switch3 != switch3_old:
        switch3_old = switch3
        message = 'sw 3 ' + str(switch3)
        send2Pd (message)
    if switch4 != switch4_old:
        switch4_old = switch4
        message = 'sw 4 ' + str(switch4)
        send2Pd (message)

    # Check each pin's last and current state to see if it was pressed or released.
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.

        ### Capacitive 1
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            #print('x1 {0:x} touched!'.format(i))
            message = 'x1 {0:x} 1'.format(i)
            send2Pd (message)
        # Next check if transitioned from touched to not touched.
        if not current_touched & pin_bit and last_touched & pin_bit:
            #print('x1 {0:x} released!'.format(i))
            message = 'x1 {0:x} 0'.format(i)
            send2Pd (message)

        ### Capicitive 2
        pin_bit2 = 1 << i
        if current_touched2 & pin_bit2 and not last_touched2 & pin_bit2:
            message = 'x2 {0:x} 1'.format(i)
            send2Pd (message)
        if not current_touched2 & pin_bit2 and last_touched2 & pin_bit2:
            message = 'x2 {0:x} 0'.format(i)
            send2Pd (message)


    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    last_touched2 = current_touched2

    time.sleep(0.01)

    # Alternatively, if you only care about checking one or a few pins you can
    # call the is_touched method with a pin number to directly check that pin.
    # This will be a little slower than the above code for checking a lot of pins.
    #if cap.is_touched(0):
    #    print('Pin 0 is being touched!')

    # If you're curious or want to see debug info for each pin, uncomment the
    # following lines:
    #print '\t\t\t\t\t\t\t\t\t\t\t\t\t 0x{0:0X}'.format(cap.touched())
    #filtered = [cap.filtered_data(i) for i in range(12)]
    #print('Filt:', '\t'.join(map(str, filtered)))
    #base = [cap.baseline_data(i) for i in range(12)]
    #print('Base:', '\t'.join(map(str, base)))
