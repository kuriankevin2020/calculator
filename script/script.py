import os
import shutil

VERSION = 'msscmcfp2'
SRC = 'C:\\Users\\Mimphiz\\Documents\\testrunner\\'
PRINTOUTS = SRC + VERSION +'\\upload\\regression-tests\\printouts'
DEST = SRC + '\\result\\' + VERSION

FRAGMENTS = ['Analysis', 'Connection', 'Gen', 'Ip', 'Rnw', 'Routing', 'Signaling']

def listDir(dir, fragment):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        if fileName.endswith(fragment + '.z'):
            FILE = os.path.abspath(os.path.join(PRINTOUTS, fileName))
            shutil.copy(FILE, DEST + '\\' + fragment)
        
if __name__=='__main__':
    for fragment in FRAGMENTS:
        os.makedirs(SRC + '\\result\\' + VERSION + '\\' + fragment)
        listDir(PRINTOUTS, fragment)