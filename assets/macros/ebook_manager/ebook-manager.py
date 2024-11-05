#!/usr/bin/python
#
# ebook-manager.py - An utility script to keep synchronized bi-directionally
#                    two repositories of ebooks.
#
# Author: Francesco Montorsi (c) 2008
# Creation date: 2/7/2008
#

import sys, os, shutil, subprocess, platform
from stat import *
from ebook_mng_common import *



# check arguments
# ---------------

if sys.version_info[0]<3:
    print("Sorry, Python >= 3.0.0 is required for this script to run.")
    exit(1)
    
if len(sys.argv)<3:
    print("\nUsage: %s [mode] main-path\n" % os.path.basename(sys.argv[0]))
    print("Allowed working modes are:")
    print(" list           updates the list.txt file with the list of PDF,CHM,DJVU")
    print("                files in the 'main-path'.")
    print(" sync path      synchronizes the given 'path' with the 'main-path'.")
    print(" check-names    checks the files of 'main-path' for incorrect file names.")
    print("Note that you must specify exactly one working mode.")
    print("\nCopyright (c) 2008 by Francesco Montorsi (http://frm.users.sourceforge.net/)")
    exit(1)

mode = sys.argv[1]
main_path = os.path.abspath(sys.argv[-1])

if not os.access(main_path, os.R_OK):
    print("Cannot access for reading path '%s'." % (main_path))
    exit(1)



# main code:
# ----------

try:
    if mode=='list':
        print("Searching for all eBooks in '%s'" % main_path)

        # get the list of all books in main path
        lst = []
        def listBooks(file, fileSize, fileModTime):
            assert file.startswith(main_path)

            if isValidBook(file):
                lst.append(file[len(main_path)+1:])
        walktree(main_path, listBooks)
        lst.sort()

        print("Computing size of the eBooks folder...")
        try:
            if platform.system().lower() == "windows":
                sz = subprocess.check_output("..\\tools_win\\du.exe -sh " + main_path, universal_newlines=True)
                sz = sz.split('\t')[0]
            else:
                sz = subprocess.check_output("du -sh " + main_path, universal_newlines=True)
                sz = sz.split('\t')[0]
        except AttributeError as e:
            print(e)
        except NameError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            
        # for compatibility with Winzozz, use \r\n as newline separator:
        #sep = '\r\n'
        sep = '\n'

        # write the list.txt file
        print("Writing the list.txt file")
        fout = open(main_path + "/list.txt", "w", encoding="utf8")
        fout.write("This is the list of the %d books (%sbytes) contained in this folder." % (len(lst), sz))
        fout.write(sep)

        try:
            dirs = os.listdir(main_path)
            dirs.sort()
            for dir in dirs:
                if os.path.isdir(main_path + "/" + dir):
                    books = []
                    for f in lst:
                        if os.path.dirname(f).startswith(dir):
                            books.append(f[len(dir)+1:])

                    # make an entry only for those folders actually containing books:
                    if len(books)>0:
                        fout.write(sep + " => " + dir + sep)
                        for b in books:
                            fout.write("  - " + b + sep)
        except UnicodeEncodeError as e:
            print(e)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    elif mode=='check-names':

        print("Checking file names in '%s' folder." % main_path)

        validChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789-,'"
        errCount = 0

        # check the filenames
        def listBooks(file, fileSize, fileModTime):
            global errCount
            if isValidBook(file):
                nameOnly = os.path.basename(file).rsplit('.')[0]
                for c in nameOnly:
                    if c not in validChars:
                        print("Invalid name for '%s'." % file[len(main_path)+1:])
                        errCount = errCount + 1
        walktree(main_path, listBooks)

        print("Found %d books with an invalid name." % errCount)

    elif mode=='sync':

        # check the second path given
        path2 = os.path.abspath(sys.argv[2])
        if not os.access(path2, os.R_OK):
            print("Cannot access for read path '%s'." % path2)
            exit(1)

        if main_path==path2:
            print("Please provide two different paths.")
            exit(1)

        # do sync dirs first
        print("Synchronizing path '%s' with '%s'..." % (main_path, path2))
        if syncDirs(main_path, path2):
            print("\nPlease correct the previously reported discrepancies. Cannot continue.")
            exit(1)

        # sync files:
        syncFiles(main_path, path2)
        print("\nScript complete.")

    else:
        print("Invalid working mode '%s'." % mode)
        exit(1)

except KeyboardInterrupt:
    print("\nInterrupted by user.\n")
    exit(1)

except:
    print("\nUnhandled exception!.\n")
    exit(1)

exit(0)     # success
