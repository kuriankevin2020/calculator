import os
import shutil
import zipfile
import logging

logging.basicConfig(filename='script.log', level=logging.INFO,
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

tot_count = 0
cp_count = 0
ext_count = 0

def fileCount(dir, tot_count):
    count = 0
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        count = count + 1
    logging.info('No of printouts in ' + VERSION + ' :' + str(count))
    tot_count = count

def copyFiles(dir, fragment, cp_count):
    count = 0
    os.makedirs(DEST + '\\' + fragment)
    logging.info('Fragment Folder Created: ' + DEST + '\\' + fragment)
    fileNames = os.listdir(dir)
    for fileName in fileNames:         
        if fileName.endswith(fragment + '.z'):
            count = count + 1
            FILE = os.path.abspath(os.path.join(PRINTOUTS, fileName))
            logging.debug('File Found: ' + FILE)
            shutil.copy(FILE, DEST + '\\' + fragment)
            logging.debug('Copied ' + fileName + ' to ' + DEST + '\\' + fragment)
    logging.info('No of ' + fragment + ' printouts copied :' + str(count))
    cp_count = cp_count + count
            
def unzipFile(dir, fragment, ext_count):
    count = 0
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        count = count + 1
        f_Name , f_Ext = os.path.splitext(fileName)
        path = DEST + '\\' + fragment + '\\' + f_Name
        os.mkdir(path)
        logging.debug('Folder Created: ' + path)
        zip_ref = zipfile.ZipFile(DEST + '\\' + fragment + '\\' + fileName,'r')
        zip_ref.extractall(path)
        logging.debug('Extracted ' + fileName + ' to ' + path)
    logging.info('No of ' + fragment + ' printouts extracted :' + str(count))
    ext_count = ext_count + count
        
if __name__=='__main__':
    fileCount(PRINTOUTS, tot_count)
    for fragment in FRAGMENTS:
        copyFiles(PRINTOUTS, fragment, cp_count)
        logging.info('Copied all ' + fragment + ' files to ' + DEST + '\\' + fragment)
        unzipFile(DEST + '\\' + fragment, fragment, ext_count)
        logging.info('Extracted all ' + fragment + ' files under ' + DEST + '\\' + fragment)
    if tot_count == cp_count:
        logging.info('Copied all printouts Successfully.')
        if tot_count == ext_count:
            logging.info('Extracted all printouts Successfully.')
        else:
            logging.info('All printouts were copied but all were not extracted.')
    else:
        logging.info('All printouts were not copied.')    
    logging.info('Script Execution Completed Successfully.')
    print('EOF')