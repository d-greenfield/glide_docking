import os
import sys

pdbfilename = str(sys.argv[1].strip('.pdb'))
precision = str(sys.argv[2])
directory_file = open('directories.txt', 'w') 					#creates text file of directories which is used in write.py

i = 0
while i != 66:									#generate directories to organize where output files are held
	if i < 10:
		os.mkdir(pdbfilename + '_glide_' + precision + "_00" + str(i))
		directory_file.write(pdbfilename + '_glide_' + precision + "_00" + str(i))
	else:	
		os.mkdir(pdbfilename + '_glide_' + precision + "_0" + str(i))
		directory_file.write(pdbfilename + '_glide_' + precision + "_0" + str(i))
	i = i - 1

directory_file.close()
#copy all necessary files into freshly made directories

os.system('python ../pre_run/write.py')

