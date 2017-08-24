import sys, os, math

#12 + report of ##### poses
f = sys.argv[1]
lst = open(str(f), 'r')

count = 0
running_avg = 0.00
AVG = -7.71565334209
run_sum_diff = 0.00
total_ligs = 0.0
#sys.exit()					
###################################################^^^^^
for i in lst:
	scorefile = open(i.strip('\n'), 'r')
	scorelines = scorefile.readlines()
	size = 0
	total_lines = 12
	line_counter = 0
	temp_avg = 0.00
	for i in scorelines:
		line_counter = line_counter + 1
		i = i.split()
		if len(i) > 0:
			if i[2] == 'BEST':
				size = int(i[3])
				total_lines = size + total_lines
				print size
				total_ligs = total_ligs + float(size)
		if line_counter > 13 and line_counter < total_lines:
#			print i
			temp_avg = temp_avg + float(i[3])
	#		run_sum_diff = run_sum_diff + ((float(i[3]) - AVG)**2)	
		if line_counter > total_lines:
	#		running_avg = running_avg + temp_avg/float(size)
#			print running_avg
			print 'done ' + str(count)
			break
	#os.chdir('..')
	count = count + 1

total_avg = running_avg/10.0

print "The overall avg is: "  + str(total_avg)

AVG = float(total_avg)
count = 0
for i in lst:
#	os.chdir(''+ i.strip('\n'))
	scorefile = open(i.strip('\n'), 'r')
	scorelines = scorefile.readlines()
	size = 0
	total_lines = 12
	line_counter = 0
	temp_avg = 0.00
	for i in scorelines:
		line_counter = line_counter + 1
		i = i.split()
		if len(i) > 0:
			if i[2] == 'BEST':
				size = int(i[3])
				total_lines = size + total_lines
				print size
				total_ligs = total_ligs + float(size)
		if line_counter > 13 and line_counter < total_lines:
#			print i
			temp_avg = temp_avg + float(i[3])
			run_sum_diff = run_sum_diff + ((float(i[3]) - AVG)**2)	
		if line_counter > total_lines:
			running_avg = running_avg + temp_avg/float(size)
#			print running_avg
			print 'done ' + str(count)
			break
	#os.chdir('..')
	count = count + 1
std_dev = math.sqrt(run_sum_diff/total_ligs)
print "the standard deviation is +/- " + str(std_dev)
