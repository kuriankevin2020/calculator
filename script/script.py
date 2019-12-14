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
    logging.info('Fragment Folder Created: ' + DEST + '\\' + fragment)
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        if fileName.endswith(fragment + '.z'):            
            FILE = os.path.abspath(os.path.join(PRINTOUTS, fileName))
            logging.debug('File Found: ' + FILE)
            shutil.copy(FILE, DEST + '\\' + fragment)
            logging.debug('Copied ' + fileName + ' to ' + DEST + '\\' + fragment)
            
def unzipFile(dir, fragment):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        f_Name , f_Ext = os.path.splitext(fileName)
        path = DEST + '\\' + fragment + '\\' + f_Name
        os.mkdir(path)
        logging.debug('Folder Created: ' + path)
        zip_ref = zipfile.ZipFile(DEST + '\\' + fragment + '\\' + fileName,'r')
        zip_ref.extractall(path)
        logging.debug('Extracted ' + fileName + ' to ' + path)
        
if __name__=='__main__':
    for fragment in FRAGMENTS:
        copyFiles(PRINTOUTS, fragment)
        logging.info('Copied all ' + fragment + ' files to ' + DEST + '\\' + fragment)
        unzipFile(DEST + '\\' + fragment, fragment)
        logging.info('Extracted all ' + fragment + ' files under ' + DEST + '\\' + fragment)
    logging.info('Script Execution Completed Successfully.')
    print('EOF')