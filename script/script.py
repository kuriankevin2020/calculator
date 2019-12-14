import os
import shutil
import zipfile
import logging

logging.basicConfig(filename='script.log', level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s')

SRC = 'C:\\Users\\Mimphiz\\Documents\\testrunner'
logging.info('Source Folder :' + SRC)
VERSION = 'msscmcfp2'
PRINTOUTS = SRC + '\\' + VERSION +'\\upload\\regression-tests\\printouts'
logging.info('Printouts Folder :' + PRINTOUTS)
DEST = SRC + '\\result\\' + VERSION
logging.info('Destination Folder :' + DEST)
logging.info('Version :' + VERSION)

FRAGMENTS = ['Analysis', 'Connection', 'Gen', 'Ip', 'Rnw', 'Routing', 'Signaling']
logging.debug('FRAGMENTS :' + ', '.join(map(str, FRAGMENTS)))

def copyFiles(dir, fragment):
    os.makedirs(DEST + '\\' + fragment)
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        if fileName.endswith(fragment + '.z'):
            FILE = os.path.abspath(os.path.join(PRINTOUTS, fileName))
            shutil.copy(FILE, DEST + '\\' + fragment)
            
def unzipFile(dir, fragment):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        f_Name , f_Ext = os.path.splitext(fileName)
        path = DEST + '\\' + fragment + '\\' + f_Name
        os.mkdir(path)
        zip_ref = zipfile.ZipFile(DEST + '\\' + fragment + '\\' + fileName,'r')
        zip_ref.extractall(path)
        
if __name__=='__main__':
    for fragment in FRAGMENTS:
        copyFiles(PRINTOUTS, fragment)
        unzipFile(DEST + '\\' + fragment, fragment)
    print('EOF')