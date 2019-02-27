import threading
from ffmpy import FFmpeg

class re_encode(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        ff = FFmpeg(
            executable='/Users/aznable/Desktop/exercise-2-ffmpeg-ZeyuKeithFu/ffmpeg',
            inputs={'sailing.MP4': None},
            outputs={'output_720.mp4': ['-s', 'hd720', '-b:v', '2M', '-framerate', '30'],
                     'output_480.mp4': ['-s', 'hd480', '-b:v', '1M', '-framerate', '30']}
        )
        print("Start to encoding...")
        ff.run()