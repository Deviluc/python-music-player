from pygame import *
import os, sys, time, re
 
user_input = raw_input("Enter the path of your file: ")
 
MusicD = user_input
x = os.listdir(MusicD)

for i in range (0, len(x)):
	#print x[i]
	matchObject = re.search('.*\.mp3', x[i])

	if matchObject:
		print "Found an mp3 file: " + x[i]

 
mixer.init()
 
mixer.music.load("filepath.mp3")
mixer.music.play()
 
 
while mixer.music.get_busy():
    print 'Now Playing: Insert track name here'
    time.sleep(5)
print 'Nope'
