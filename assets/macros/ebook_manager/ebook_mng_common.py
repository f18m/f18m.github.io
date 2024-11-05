#
# ebook_mng_common.py - helper code for ebook-manager
#
# Author: Francesco Montorsi (c) 2008
# Creation date: 2/7/2008
#

import sys, os, shutil
from stat import *


# block the user from running this file directly
if __name__ == '__main__':
    # Running as a script
    print("Sorry, this file is only a collection of utilities for ebook-manager.py")
    print("Run ebook-manager.py instead of this file.")
    exit(1)


# utilities
# ---------

class IndexedFile:
    def __init__(self, pathAndName, size, mtime):
        self.pathAndName = pathAndName
        self.size = size
        self.mtime = mtime

def prettySize(size):
    suffixes = [("B",2**10), ("K",2**20), ("M",2**30), ("G",2**40), ("T",2**50)]
    for suf, lim in suffixes:
        if size > lim:
            continue
        else:
            return round(size/float(lim/2**10),2).__str__()+suf

def prettyFileName(filename, maxColumn=80):
    splitAt=(maxColumn-10)/2
    ret = filename
    if len(filename) > maxColumn:
        ret = filename[:splitAt] + " ... " + filename[len(filename)-splitAt:]
    return ret

def prettyFileList(filenames, maxColumn=100):
    ret = ""
    for f in filenames:
        ret += prettyFileName(f, maxColumn) + '\n    '
    return '    ' + ret.strip()

def rawPrint(str):
    # print() always put a final newline, which we don't want here:
    sys.stdout.write(str)
    sys.stdout.flush()  # make it appear immediately on the console

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

def isValidBook(filename):
    ext = os.path.splitext(filename)[1]
    if ext in [ '.pdf', '.chm', '.djvu', '.txt' ] and os.path.basename(filename)[0]!='.':
        return True
    return False

def askQuestion(question, allowedReplies):
    ar = []
    for r in allowedReplies:
        ar.append(r + '\n')
    reply=''
    while reply not in ar:
        rawPrint(question)
        reply = sys.stdin.readline()
    return reply[:-1]       # remove the final newline

def askYesNoQuestion(question, yesChar="y", noChar="n"):
    reply=''
    while reply != noChar + '\n':
        rawPrint(question)
        reply = sys.stdin.readline()
        if reply == yesChar + '\n':
            return True
    return False



# utilities for the 'sync' mode
# -----------------------------

# make sure that in both paths there are the same subdirectories
def syncDirs(path1,path2):

    def visitdir1(dirname):
        relativePath = dirname[len(path1)+1:]
        dirsToCheck[relativePath] = relativePath

    def visitdir2(dirname):
        relativePath = dirname[len(path2)+1:]
        if relativePath not in dirsToCheck:
            dirsOnlyInPath2.append(relativePath)
        else:
            # this directory is ok; remove it from the list of folders yet to be checked:
            del dirsToCheck[relativePath]

    needFix = False
    dirsToCheck = dict()
    dirsOnlyInPath2 = []
    walktree(path1, None, visitdir1)
    walktree(path2, None, visitdir2)

    if len(dirsToCheck)>0:
        print("\n  Directories:\n    %s\n  exist only in the '%s' path." \
              % ('\n    '.join(list(dirsToCheck.keys())), path1))
        needFix = True

    if len(dirsOnlyInPath2)>0:
        print("\n  Directories:\n    %s\n  exist only in the '%s' path." \
              % ('\n    '.join(dirsOnlyInPath2), path2))
        needFix=True

    return needFix



# sync files
def syncFiles(path1,path2):

    def visitfile1(file, fileSize, fileModTime):
        #print 'visiting', file, ' size=', fileSize, 'moddate=', fileModTime
        if isValidBook(file) or file.endswith(".py"):
            relativePath = file[len(path1)+1:]
            files1[relativePath] = IndexedFile(relativePath, fileSize, fileModTime)

    def visitfile2(file, fileSize, fileModTime):
        if isValidBook(file) or file.endswith(".py"):
            relativePath = file[len(path2)+1:]

            # index this file
            files2[relativePath] = IndexedFile(relativePath, fileSize, fileModTime)

            # check if it's present in path1
            if relativePath not in filesOnlyInPath1:
                filesOnlyInPath2.append(relativePath)
            else:
                # warn about its filesize eventually
                if fileSize!=filesOnlyInPath1[relativePath].size:
                    print("\n  The file '%s' has different sizes in the two " \
                        "paths being checked:\n    %s (%s)\n    %s (%s)" \
                        % (prettyFileName(relativePath,30), \
                            path1,prettySize(filesOnlyInPath1[relativePath].size), \
                            path2,prettySize(fileSize)))

                # this file is ok; remove it from the list of files yet to be checked:
                del filesOnlyInPath1[relativePath]


    # index files in first path
    files1 = dict()
    walktree(path1, visitfile1)

    # index & check files in the second path
    filesOnlyInPath1 = files1
    files2 = dict()
    filesOnlyInPath2 = []
    walktree(path2, visitfile2)


    def askForRenaming(path1,f1,path2,f2):
        try:
            print()
            print("  Seems that the same file has two different names in the two repos. Which is the correct name:")
            print("   [A] %s\n   [B] %s\n   [C] none; enter a new one" % (os.path.basename(f1), os.path.basename(f2)))

            reply = askQuestion("  Choose among [A], [B] or [C]: ", ["A","B","C"])
            if reply=='A':
                print("  Renaming to '%s'" % os.path.basename(f1))
                os.rename(os.path.join(path2, f2), os.path.join(path2, f1))
            elif reply=='B':
                print("  Renaming to '%s'" % os.path.basename(f2))
                os.rename(os.path.join(path1, f1), os.path.join(path1, f2))
            elif reply=='C':
                newname=''
                while not isValidBook(newname):
                    rawPrint("  Please provide the new name (with extension): ")
                    newname = sys.stdin.readline().strip()
                os.rename(os.path.join(path1, f1), os.path.join(path1, newname))
                os.rename(os.path.join(path2, f2), os.path.join(path2, newname))
        except:
            print("Error renaming... cannot proceed.")
            exit(1)
        return True

    # first auto-detect renamings:
    alreadyShown = []

    for f1 in filesOnlyInPath1:
        path = os.path.dirname(f1)

        # search in the relative folder of f1 in path2 for files with the same size:
        for f2 in files2:
            if os.path.dirname(f2)==path and files2[f2].size==files1[f1].size:
                alreadyShown.append(f1)
                askForRenaming(path1,f1,path2,f2)

    for f2 in filesOnlyInPath2:
        path = os.path.dirname(f2)

        # search in the relative folder of f1 in path2 for files with the same size:
        for f1 in files1:
            if f1 not in alreadyShown and os.path.dirname(f1)==path and files1[f1].size==files2[f2].size:
                askForRenaming(path1,f1,path2,f2)

    # show lists of the files which are missing from repos
    needFix = False
    if len(filesOnlyInPath1)>0:
        print("\n  Files (LIST A):\n%s\n  exist only in path '%s'." \
            % (prettyFileList(list(filesOnlyInPath1.keys())), path1))
        needFix = True
    if len(filesOnlyInPath2)>0:
        print("\n  Files (LIST B):\n%s\n  exist only in path '%s'." \
            % (prettyFileList(filesOnlyInPath2), path2))
        needFix = True

    print()
    if not needFix:
        print("Seems the two paths contains the same folders and the same files!")
        return True

    # now copy files missing from one folder to the other
    def copyListOfFiles(lst, lname, sourcepath, destpath):
        if len(lst)==0:
            return True

        if askYesNoQuestion("  Should I copy the %d files of LIST %s to '%s' [y/n]? " % \
                            (len(lst), lname, destpath)):
            rawPrint("  Copying...")
            for f in lst:
                # copy preserving mtime and access time:
                shutil.copy2(os.path.join(sourcepath,f), os.path.join(destpath,f))
                rawPrint(".")

            print()   # final newline
            return True
        return False

    copyListOfFiles(filesOnlyInPath1, "A", path1, path2)
    copyListOfFiles(filesOnlyInPath2, "B", path2, path1)

    return True
