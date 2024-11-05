#!/usr/bin/python
#
# Author: Francesco Montorsi (c) 2012
# Creation date: 30/12/2012
#

import glob, subprocess, os, sys


# constants
# IMPORTANT: modify these with values suitable for your system:

path_apply_script = "C:\\Users\\Francesco\\Dropbox\\mySite\\macros\\apply_ieee_citation_style"
path_diff_tool = "C:\\Program Files (x86)\\WinMerge\\WinMergeU.exe"



# NO NEED TO CHANGE ANYTHING BELOW THIS LINE

# import main script functionalities
sys.path.insert(0, path_apply_script)
#print(sys.path)
import apply_ieee_citation_style

path_diff_tool = "\"" + path_diff_tool + "\""

original_files = glob.glob("*.bib")
for bibtex_fname in original_files:
    print("\n\nNow processing file: %s" % bibtex_fname)

    print("-------------------------------------------------------------------------------")
    #os.system(path_apply_script + " " + bibtex_fname)
    #subprocess.call(path_apply_script + " " + bibtex_fname, shell=True)
    count = apply_ieee_citation_style.do_apply(bibtex_fname, path_apply_script + os.sep + "style", False)

    if count > 0:
        root_ext = os.path.splitext(bibtex_fname)
        out_fname = root_ext[0] + ".tmp" + root_ext[1]
        
        print("Now launching diffing tool: %s" % path_diff_tool)
        os.system(path_diff_tool + " " + bibtex_fname + " " + out_fname)
        
        #stdscr.getch()
        print("-------------------------------------------------------------------------------")
        answer = input("Changes are ok? Should I replace original file [y/n]?")
        if answer == "y":
            os.remove(bibtex_fname)
            os.rename(out_fname, bibtex_fname)
    else:
        print("-------------------------------------------------------------------------------")
        input("Press Enter to continue or CTRL+C to exit...")

    
fprintf("Batch completed")
