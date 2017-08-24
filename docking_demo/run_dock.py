import sys
import os


dirs = open('directories.txt', 'r')
count = 0
for i in dirs:
	i = i.strip('\n') 
	os.chdir(''+ str(i))
	os.system("bash run_glide_" + str(count) + ".sh")	
	count = count + 1
	os.chdir('..')
