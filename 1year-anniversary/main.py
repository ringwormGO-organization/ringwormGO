# import required module
from playsound import playsound

# ascii.txt display
f = open('ascii.txt', 'r')
content = f.read()
print(content)
f.close

# for playing mp3 file
playsound('song.mp3')
