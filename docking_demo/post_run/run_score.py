import sys
import os


dirs = open('directories.txt', 'r')
count = 1
for i in dirs:
	if count <= -1: 
		count = count + 1
		continue
	else:
		i = i.strip('\n') 
		os.chdir(''+ str(i))
		direct = i.split('_')
		print direct
		#os.system("bash run_glide_" + str(count) + ".sh")
		if (int(direct[3][-2:]) < 10):
			print direct[3][-1:]
			os.system("$SCHRODINGER/utilities/glide_sort -R INFILE_" + str(direct[3][-1:]) + "_pv.maegz > out_" + str(direct[3][2:]) + '.txt')  
		if (int(direct[3]) >= 10):
			break
			os.system("$SCHRODINGER/utilities/glide_sort -R INFILE_" + str(direct[3][1:]) + "_pv.maegz > out_" + str(direct[3][1:]) + '.txt')  
		os.chdir('..')
		count = count + 1
