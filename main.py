import re_encode
import threading
import generate_video
from multiprocessing import Queue
import os

INP_PATH = '../videos/' # Input videos directory
MAX_COUNT = 5 # Maximum threads

def main():

    q = Queue()
    inputs = []

    for i in os.listdir(INP_PATH):
        if (i != '.DS_Store') & (len(i.split("_")) == 1):
            inputs.append(INP_PATH + i)

    for j in range(len(inputs)):
        q.put(j+1)

    while True:
        if threading.active_count() < MAX_COUNT:
            id = q.get()
            thread = re_encode.re_encode(id, inputs[id-1])
            thread.start()
        elif q.empty():
            break

    return


if __name__ == '__main__':
    main()
