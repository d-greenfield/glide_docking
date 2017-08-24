import os
import sys
dirs = open('directories.txt','r')
i = 0 
for line in dirs:
	line = line.strip('\n')
	os.chdir(''+str(line))
	os.system('cp *_pv.maegz ../../SP ')
	os.chdir('..')
	i = i + 1
