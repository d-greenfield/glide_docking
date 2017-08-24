# glide_docking
Collection of scripts to run glide docking pipeline
Directories: 
• HTVS, SP, XP, XP_flexible ==> Empty directories that will be filled with docking data from the various precision levels, created manually
• pre_run ==> two scripts write.py, and make_dir.py (which calls write.py)
• post_run ==> three scripts get_avg.py, run_score.py, split_edit.py


Floating Scripts:
• copy.py - potentially useful script if you need to copy files around 
• run_dock.py - will call all the run_glide.sh files in the directories made by make_dir.py


Useful Schrodinger scripts:
• $SCHRODINGER/utilities/glide_sort --> will score .maegz files output by glide

• $SCHRODINGER/utilities/glide_merge --> will make new .maegz files from existing ones. Allows you to impose scoring cutoffs so that you can have ligands that score better than whatever score you choose as lowest. You can provide a full file list using the -f (filename) flag when calling this program (generate by doing ls 5hk1_*.maegz > files.txt)


Use of my scripts: 
• make_dir.py - Call from inside the precision directory you're working with at the time. 
	1. Call make_dir.py (name of .pdb file) (precision level) [ex: make_dir.py 5hk1.pdb HTVS] --> Allows for make_dir.py to generate directories labeled in this example 5hk1_glide_HTVS_000, 5hk1_glide_HTVS_001, etc.
		The 000,001,... correspond to the ligand subset file in the emolecules directory 
	2. Generates run_glide.sh file and the specific glide input file (.in) for each ligand subset file you'll be using (numbered from 0-65). 

• run_dock.py - Call from inside the precision directory you're working with (python ../run_dock.py). This also uses the directories.txt file made by make_dir.py

• run_score.py - Call from inside precision directory you're in. This program calls the glide_sort and outputs a text file with all data.

• get_avg.py - Call from inside precision directory you're in. Given a .mae (NOT .maegz), this program can calculate the average score and standard deviation, see specifics how to run it below in pipeline below). Call by typing python get_avg.py [scorefilename.txt]

• split_edit.py - Call within directory. Schrodinger provides a glide_merge but not a glide_split function, so this program splits .mae files. This program calculates how many ligands are in a .mae file, and splits it into 10 separate files. This works pretty quickly (can split ~50k structures in like 10 seconds), but I could do this in a smarter way..will let you know if I get around to updating it. Call by typing python split_edit.py [filename.mae]


How I run the pipeline: 

1. Protein preparation - in the maestro GUI do the protein preparation protocol
	Protein crystal structures are prepared prior to docking in order to add hydrogen atoms, optimize hydrogen bonds, remove atomic clashes, and perform other operations that are not part of the x-ray crystal structure refinement process. 1

	Completed in the Maestro GUI:
 	Preprocessing options: 
	options used were same as options used in Schrodinger’s tutorial - assign bond orders, add hydrogens, create disulfide bonds, delete waters beyond 5 A from het groups 

	Refinement options:
	Hydrogen bond assignment: sample water orientations, use PROPKA pH of 7.0
	Remove waters
	Restrained Minimization: Converge heavy atoms to RMSD of 0.30 A, Force field OPLS   	2005 (did this before the Schrodinger 2016-2 update)

2. Would do ligand preparation, but the libary is already pre-prepared by Schrodinger before it was handed to us. Relevant if you have access to other ligand files and need to prepare them.

3. Grid generation - define the active site of the protein, or where you want to dock compounds. I would make sure to do this within the overall project directory (one level above precision directories) and make sure you change the path to this grid in the write.py file so that your files are generated with the right paths to the right files so the docking actually works.

4. Docking
	make_dir.py
	run_dock.py
	run_score.py
	glide_merge
	get_avg.py
		note: not the most efficient program, might update if given time
	glide_merge.py - use with cutoff based on avg - x*STDDEV to make new file to call in next precision level
	split_edit.py - split that file into 10 subfiles to be used in next precision level...might be worth doing 20 subfiles for sp depending on how many ligands you move through HTVS

	cd to new precision level
	repeat :) 
