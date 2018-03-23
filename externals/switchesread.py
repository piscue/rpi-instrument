# Author: piscue 20180323
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
import wiringpi
import time
import os

#wiringpi.wiringPiSetupGpio()
wiringpi.wiringPiSetup()
#wiringpi.wiringPiSetupSys()

#wiringpi.pinMode(2, 0)
switch1_old = 0
switch2_old = 0
switch3_old = 0
switch4_old = 0

def send2Pd(message=''):
    os.system("echo '" + message + "' | pdsend 3000 localhost udp")

while True:
    switch1 = wiringpi.digitalRead(4)
    switch2 = wiringpi.digitalRead(5)
    switch3 = wiringpi.digitalRead(2)
    switch4 = wiringpi.digitalRead(3)
    if switch1 != switch1_old:
        print ("switch1: " + str(switch1))
        switch1_old = switch1
        message = 'switch1 ' + str(switch1)
        send2Pd (message)
    if switch2 != switch2_old:
        print ("switch2: " + str(switch2))
        switch2_old = switch2
        message = 'switch2 ' + str(switch2)
        send2Pd (message)
    if switch3 != switch3_old:
        print ("switch3: " + str(switch3))
        switch3_old = switch3
        message = 'switch3 ' + str(switch3)
        send2Pd (message)
    if switch4 != switch4_old:
        print ("switch4: " + str(switch4))
        switch4_old = switch4
        message = 'switch4 ' + str(switch4)
        send2Pd (message)
    time.sleep(0.01)
