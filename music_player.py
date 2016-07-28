import pygame
import glob
import time
pygame.init()
music_directory = '/home/mihir/Music/'
list_of_all_files = glob.glob(music_directory+'*.mp3')
for i in range(len(list_of_all_files)):
	list_of_all_files[i] = list_of_all_files[i].split('/')[-1]
	print str(i+1)+' '+list_of_all_files[i]

index = int(raw_input('Give track number to play that track '))
index -= 1
pygame.mixer.music.load(music_directory+list_of_all_files[index])
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
	pygame.time.Clock().tick(10)
