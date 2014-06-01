'''
Created on 2014. 6. 1.

@author: Yun-chan
'''

import time

#
def confirm(pin):
    #Make sure resource is available
    try:
        f= open ('/sys/class/gpio/unexport','w')
        f.write(str(pin))
        f.close()
    except IOError as e:
        lol=0
        
def export(pin):
    #Export pin number
    f= open ('/sys/class/gpio/export','w')
    f.write(str(pin))
    f.close()

def setDirection(pin):
    #Define Pin Direction as Output for LED
    path = '/sys/class/gpio/gpio' + pin + '/direction'
    f= open (path,'w')
    f.write('out')
    f.close()
    
def blink(pin, blinks):
    #Loop through LED 'ON' and 'OFF' for the number of times specified
    i=0;
    path = '/sys/class/gpio/gpio' + pin + '/value'
    while(i<int(blinks)):
        
        f= open (path,'w')
        f.write('1')
        f.close()
    
        time.sleep(0.5)
    
        f= open (path,'w')
        f.write('0')
        f.close()
    
        time.sleep(0.5)
        i+=1
        
def turnOn(pin):
    #Loop through LED 'ON' and 'OFF' for the number of times specified
    path = '/sys/class/gpio/gpio' + pin + '/value'
        
    f= open (path,'w')
    f.write('1')
    time.sleep(10.5)
    f.close()



def close(pin):
    #Unexport Pin 
    f= open ('/sys/class/gpio/unexport','w')
    f.write(str(pin))
    f.close()
    

#main 
def answer(pin, loop=1):
    confirm(pin)
    export(pin)
    setDirection(pin)
    blink(pin, loop)
    close(pin)
    
#main 
def answer2(pin):
    confirm(pin)
    export(pin)
    setDirection(pin)
    turnOn(pin)
    close(pin)
    
    
    
#main

GPIO0 = 17
GPIO1 = 18
GPIO2 = 27
GPIO3 = 22
GPIO4 = 23

#
def loop():
    print "start!"
    
    answer(str(GPIO0))
    answer(str(GPIO1))
    answer(str(GPIO2))
    answer(str(GPIO3))
    answer(str(GPIO4))
    print "good!"
    

answer2(str(GPIO4))
