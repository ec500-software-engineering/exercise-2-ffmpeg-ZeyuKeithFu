import threading
from ffmpy import FFmpeg
import time

class re_encode(threading.Thread):

    def __init__(self, q, threadID, vid_input):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
        self.vid_input = vid_input
        self.output1 = vid_input.split(".")[0] + "_720." + vid_input.split(".")[1]
        self.output2 = vid_input.split(".")[0] + "_480." + vid_input.split(".")[1]

    def run(self):
        while True:
            try:
                self.q.get(block=True)
            except:
                return

            ff = FFmpeg(
                executable='/Users/aznable/Desktop/exercise-2-ffmpeg-ZeyuKeithFu/ffmpeg',
                inputs={self.vid_input: ['-loglevel', '0']},
                outputs={self.output1: ['-s', 'hd720', '-b:v', '2M', '-framerate', '30'],
                         self.output2: ['-s', 'hd480', '-b:v', '1M', '-framerate', '30']}

            )
            print("Start encoding video" + str(self.threadID) + " ...")
            stime = time.time()
            ff.run()
            runtime = time.time() - stime
            print("Finished encoding video" + str(self.threadID) + " in " + str(runtime) + "s!")
