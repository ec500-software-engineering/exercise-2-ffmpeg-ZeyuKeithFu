import re_encode
import generate_video
from multiprocessing import Queue
import os

INP_PATH = '/Users/aznable/Desktop/exercise-2-ffmpeg-ZeyuKeithFu/videos/'
MAX_COUNT = 3

def main():
    q = Queue(3)
    inputs = []
    for i in os.listdir(INP_PATH):
        if i != '.DS_Store':
            inputs.append(INP_PATH + i)

    for j in range(len(inputs)):
        q.put(j + 1, block=True)
        t = re_encode.re_encode(q, j + 1, inputs[j])
        t.start()


if __name__ == '__main__':
    main()
