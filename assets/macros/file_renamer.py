#!/usr/bin/python
#
# file_renamer.py - 
#    An utility script to automatically rename files with a certain rule
#
# Author: Francesco Montorsi (c) 2012
# Creation date: 25/12/2012
#

import os
import re
import sys
import argparse


# constants
# ---------

to_search = "(ebook)";
to_subst = "";




def walktree(topFolder, fileCallback, dirCallback=None):
    '''recursively descend the directory tree rooted at topFolder,
       calling the callback function for each regular file'''

    for f in os.listdir(topFolder):
        pathname = os.path.join(topFolder, f)
        tuple = os.stat(pathname)
        mode = tuple[ST_MODE]
        sz = tuple[ST_SIZE]
        modtime = tuple[ST_MTIME]
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            if dirCallback!=None:
                dirCallback(pathname)
            walktree(pathname, fileCallback, dirCallback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            if fileCallback!=None:
                fileCallback(pathname, sz, modtime)
        else:
            # Unknown file type, print a message
            print("Skipping '%s'..." % pathname)

def fileCallback(pathname, sz, modtime)
    tmp = os.path.split(path)
    path = tmp[0]
    filename = tmp[1]
    if to_search in filename:
        new_name = filename.replace(to_search,to_subst)
        new_name = os.path.join(path,new_name)
        print(" %s => %s" % (pathname, new_name))
        #os.rename(pathname, new_name)

walktree(".", fileCallback)

