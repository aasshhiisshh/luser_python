'''
Here I am going to show 2 ways to make music player.
'''

#import prerequisites packages

import mp3play,time
data= r'pathname'
clip = mp3play.load(data)
clip.play()
time.sleep(20)
clip.stop()
********************************
##shortest way to make music player##
********************************
import subprocess
PLAYERPATH = "Music-player install path"
subprocess.call([PLAYERPATH, "path for music"])
