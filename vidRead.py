import pickle
import time
import os

with open('output/mrBean.data', 'rb') as output:
    strVid = pickle.load(output)
while True:
    for frame in strVid:
        os.system('clear')
        print(frame)
        time.sleep(0.1)
