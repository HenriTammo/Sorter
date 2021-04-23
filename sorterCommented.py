%pylab inline
import time #lubab kasutada time lisamoodulit millega saab programmis määrata pause
from __future__ import print_function #kuna tegemist on python2 programmiga, siis see lubab võtta python3-st print käsu
from pypot.creatures import PoppyErgoJr #võimaldab robotile spetsiifilise käske anda
from pypot.primitive.move import MoveRecorder, MovePlayer, Move #võimaldab liigutusi salvestada

poppy = PoppyErgoJr() #defineerime roboti
motors=[poppy.m1, poppy.m2, poppy.m3, poppy.m4, poppy.m5, poppy.m6] #defineerime kõik kuus mootorit

poppy.rest_posture.start() #robot võtab puhke asendi sisse
for m in poppy.motors: m.led="blue" #muuda roboti led lambid siniseks
time.sleep(2) #oota kaks sekundit
poppy.rest_posture.stop() #puhke asendi funktsioon lõppeb

recorderRed = MoveRecorder(poppy, 50, motors)
recorderGreen = MoveRecorder(poppy, 50, motors)

for m in motors: m.compliant=True #muuda roboti mootorid inimese poolt liigutatavaks
for m in motors: m.led="red" #muuda roboti led lambid punaseks
recorderRed.start() #alusta liigutuse salvestamist punase värvi jaoks
time.sleep(10) #oota kümme sekundit
recorderRed.stop() #lõpeta salvestamine

poppy.rest_posture.start() #robot võtab puhke asendi sisse
for m in poppy.motors: m.led="blue" #muuda roboti led lambid siniseks
time.sleep(2) #oota kaks sekundit
poppy.rest_posture.stop() #puhke asendi funktsioon lõppeb

for m in motors: m.compliant=True #muuda roboti mootorid inimese poolt liigutatavaks
for m in poppy.motors: m.led="green" #muuda roboti led lambid roheliseks
recorderGreen.start() #alusta liigutuse salvestamist rohelise värvi jaoks
time.sleep(10) #oota kümme sekundit
recorderGreen.stop() #lõpeta salvestamine

for m in poppy.motors: m.led="blue"  #muuda roboti led lambid siniseks
poppy.rest_posture.start() #robot võtab puhke asendi sisse
time.sleep(2) #oota kaks sekundit
poppy.rest_posture.stop() #puhke asendi funktsioon lõppeb

for i in range(3000): #tsükkel mis käib läbi 3000 iteratsiooni
    img=poppy.camera.frame #defineeri kaamera
    red=img[240][320][2] #defineeri robotile punane värv
    green=img[240][320][1] #defineeri robotile roheline värv
    if red>green: #kui robot näeb rohkem punast
        varv='red' #loo muutuja värvi jaoks
        for m in poppy.motors: #käi läbi küik mootorid
            m.led=varv #muuda led lambid punaseks
        player = MovePlayer(poppy, recorderRed.move) #loe sisse andmed punase liigutuse jaoks
        player.start() #mängi liigutus ette
        time.sleep(11) #oota 11 sekundit
    else: #kui robot ei näe valdavalt punast
        varv='green' #loo muutuja värvi jaoks
        for m in poppy.motors: #käi läbi küik mootorid
            m.led=varv #muuda led lambid roheliseks
        player = MovePlayer(poppy, recorderGreen.move) #loe sisse andmed punase liigutuse jaoks
        player.start() #mängi liigutus ette
        time.sleep(11) #oota 11 sekundit
       
    print(red, green) #näita kasutajale arvuliselt kui palju ta mingit värvi näeb
    
    time.sleep(0.1)  #oota 0.1 sekundit
    