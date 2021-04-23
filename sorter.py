%pylab inline
import time 
from __future__ import print_function 
from pypot.creatures import PoppyErgoJr 
from pypot.primitive.move import MoveRecorder, MovePlayer, Move 
poppy = PoppyErgoJr() 
motors=[poppy.m1, poppy.m2, poppy.m3, poppy.m4, poppy.m5, poppy.m6] 

poppy.rest_posture.start() 
for m in poppy.motors: m.led="blue" 
time.sleep(2) 
poppy.rest_posture.stop() 

recorderRed = MoveRecorder(poppy, 50, motors)
recorderGreen = MoveRecorder(poppy, 50, motors)

for m in motors: m.compliant=True 
for m in motors: m.led="red" 
recorderRed.start() 
time.sleep(10)
recorderRed.stop()

poppy.rest_posture.start() 
for m in poppy.motors: m.led="blue" 
time.sleep(2) 
poppy.rest_posture.stop()

for m in motors: m.compliant=True 
for m in poppy.motors: m.led="green" 
recorderGreen.start()
time.sleep(10) 
recorderGreen.stop() 

for m in poppy.motors: m.led="blue" 
poppy.rest_posture.start() 
time.sleep(2) 
poppy.rest_posture.stop() 

for i in range(3000): 
    img=poppy.camera.frame 
    red=img[240][320][2] 
    green=img[240][320][1] 
    if red>green: 
        varv='red'
        for m in poppy.motors: 
            m.led=varv 
        player = MovePlayer(poppy, recorderRed.move)
        player.start()
        time.sleep(11)
    else: 
        varv='green' 
        for m in poppy.motors: 
            m.led=varv
        player = MovePlayer(poppy, recorderGreen.move) 
        player.start() 
        time.sleep(11) 
       
    print(red, green) 
    
    time.sleep(0.1)  
    