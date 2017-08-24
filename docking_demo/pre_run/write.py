import sys
import os


dirs = open('directories.txt', 'r')
count = 0
for i in dirs:
	i = i.strip('\n') 
	os.chdir(''+ str(i))
#	os.system('rm -r INFILE_*.in')
	infile = open('INFILE_'+str(count) +'.in', 'w')
	run = open('run_glide_' + str(count) + '.sh', 'w')

###CHANGE PATH TO WHERE YOUR FILES ARE HELD, BELOW IS MY EXAMPLE 
	if (count < 10):
		infile.write('DOCKING_METHOD   rigid\nGRIDFILE   /nfs/staff/dgreenfield/MurJ/HTVS/glide-grid_CL/glide-grid_CL.zip \nLIGANDFILE   /nfs/staff/dgreenfield/emolecules/3D/screening/subsets/split/emol_parent-single-variant-subset_00' + str(count) + '.mae.gz \nPRECISION   HTVS')
		run.write('"${SCHRODINGER}/glide" INFILE_' + str(count) + '.in -OVERWRITE -NJOBS 1  -TMPLAUNCHDIR')
	else:	
		infile.write('DOCKING_METHOD   rigid \nGRIDFILE   /nfs/staff/dgreenfield/MurJ/glide-grid_CL/glide-grid_CL.zip \nLIGANDFILE   /nfs/staff/dgreenfield/emolecules/3D/screening/subsets/split/emol_parent-single-variant-subset_0' + str(count) +  '.mae.gz \nPRECISION   HTVS')	
		run.write('"${SCHRODINGER}/glide" INFILE_' + str(count) + '.in -OVERWRITE -NJOBS 1  -TMPLAUNCHDIR')
	count = count + 1
	os.chdir('..')
