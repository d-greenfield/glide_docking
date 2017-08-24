import sys, os, subprocess
f = sys.argv[1]
workfile = open(str(f), 'r')   #the file you get from glide_merge with the scoring cutoff you impose
lines = workfile.readlines()
workfile.close()
###REPLACE PATH BELOW WITH PATH TO YOUR FILE OPENED ABVOE
#this counts the number of ligands in the file, then splits that file into 10 other files to make the docking go faster on the computer. could and will be prettier in the future, just need more time :p

size = subprocess.Popen(['grep','-c', 'f_m_ct {', '/nfs/staff/dgreenfield/MurJ/XP/for_xp.mae'], stdout=subprocess.PIPE).communicate()[0]
print size

xp_file_1 = open('xp_1.mae', 'w')
xp_file_2 = open('xp_2.mae', 'w')
xp_file_3 = open('xp_3.mae', 'w')
xp_file_4 = open('xp_4.mae', 'w')
xp_file_5 = open('xp_5.mae', 'w')
xp_file_6 = open('xp_6.mae', 'w')
xp_file_7 = open('xp_7.mae', 'w')
xp_file_8 = open('xp_8.mae', 'w')
xp_file_9 = open('xp_9.mae', 'w')
xp_file_10 = open('xp_10.mae', 'w')
count = 0 
f_count = 0
##replace this with sp, xp_flex, whatever you want as appropriate
file_arr = [xp_file_1, xp_file_2, xp_file_3, xp_file_4, xp_file_5, xp_file_6, xp_file_7, xp_file_8, xp_file_9, xp_file_10] 

for line in lines:
	line = line.strip('\n')

	if line == 'f_m_ct { ':
		count = count + 1
	
	if count <= int(size)/10:
		file_arr[0].write(line + '\n')
	else:
		f_count = f_count +1
		print "done with " + str(f_count)
		file_arr = file_arr[1:]
		count = 0
