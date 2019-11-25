#from __future__ import print_function
import numpy as np
import cv2
import os
import time
from PIL import Image
import pickle
# import mpi4py import MPI

# print(cv2.__version__)

vid = cv2.VideoCapture('vids/Mr_Bean.gif')
#vid = cv2.VideoCapture('vids/Fireworks.mp4')
#vid = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
og_width = int(vid.get(3))
og_height = int(vid.get(4))

#width = int(og_width/4)
#height = int(og_height/4)
width = og_width
height = og_height


ascPix = (' ', '.', '~', ',', ';', '!', '+', 'l', 'z',
          '}', 'y', 'e', '3', 'A', 'H', 'K', 'Q', 'W', '@')

strVid = []
frameTotal = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
ret = True
count = 0

while(True):
    ret, frame = vid.read()
    if(not ret):
        break
    #cv2.imshow('frame', frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (width, height))
    # print(frame)
    picString = ''

    #width, height = cv2.size(frame)
    #frame = frame.convert(mode='L')
    for i in range(0, height, 2):
        if (i > height - 2):
            break
        # count = 0
        for j in range(width-1):
            pix = (frame[i, j] + frame[i+1, j])/2.0
            # print(pix)
            index = int(pix/255.0*len(ascPix))
            if (index == len(ascPix)):
                index = index - 1
            # index2 = len(ascPix) -1 - int(pix/255.0*len(ascPix))
            # out.write(ascPix[index2])

            # print (index)
            # print (ascPix[index], end='')
            picString += ascPix[index]
            # count += 1

        # out.write('\n')
        #print (' ')
        picString += '\n'
    # os.system('clear')
    count += 1
    print(count, " of ", frameTotal)
    strVid.append(picString)
    # time.sleep(0.01)

with open('output/mrBean.data', 'wb') as output:
    pickle.dump(strVid, output)

for frame in strVid:
    os.system('clear')
    print(frame)
    time.sleep(0.02)
