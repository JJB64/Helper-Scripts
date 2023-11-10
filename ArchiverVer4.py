# File: ArchiverVer4.py
# Author: Joao Joseph Evenunye Baeta
# Date: 2023-08-09
# Description: Script that archives old files.


import os
import shutil
import zipfile
import logging
from datetime import datetime, timedelta


# Configure logging
logging.basicConfig(filename='LogFile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


DirPath = "C:\\Users\\Joao Joseph Baeta\\Documents\\Fidelity\\TestFiles"                              
DestinationPath = "C:\\Users\\Joao Joseph Baeta\\Documents\\Fidelity\\Archive" 

#Setting Date data
EndDate = datetime.now().date()
EndDate_str = EndDate.strftime("%Y-%m-%d")
StartDate = EndDate - timedelta(days=10)
StartDate_str = StartDate.strftime("%Y-%m-%d")


Filelist = []
MovedFileslist = []
StartDate = datetime.strptime(StartDate_str, "%Y-%m-%d").date()
EndDate = datetime.strptime(EndDate_str, "%Y-%m-%d").date()
date_range_str = StartDate.strftime("%Y-%m-%d") 
FolderPath = DirPath + "\\" + date_range_str

def DeleteFolder():
    try:
        shutil.rmtree(FolderPath)
        logging.info(f"Folder '{FolderPath}' deleted successfully.")
    except OSError as e:
        logging.error(f"Error: Unable to delete folder '{FolderPath}'. Reason: {e}")
        exit()

def ZipFiles():
    try:
        zip_file = zipfile.ZipFile(FolderPath + ".zip", 'w')
        for filepath in MovedFileslist:
            filename = os.path.basename(filepath)
            zip_file.write(filepath, filename)  # Add the file to the zip archive
        zip_file.close()
        logging.info("Zip file created successfully.")
    except OSError as e:
        logging.error(f"Error: Unable to create zip file. Reason: {e}")
        exit()


def GatherFiles(DirPath):
    if(os.path.exists(DirPath)):                                    
        DirectoryList = os.listdir(DirPath)                         
        FileCount = 0                                                                           #Keeping track of number of files that fall within date range
        for file in DirectoryList:
            filePath = os.path.join(DirPath,file)
            File_CreationTimestamp = os.path.getctime(filePath)
            File_CreationDate = datetime.fromtimestamp(File_CreationTimestamp).date()           # Convert timestamp to datetime.date
            if(File_CreationDate < StartDate):
                FileCount += 1
                Filelist.append(filePath)
        if(FileCount == 0):
            logging.info("No files found in the given date range")
            exit()
        else:
            logging.info(str(FileCount) + " File(s) found in the given date range") 
            try:
                os.mkdir(FolderPath)                                                            #Creating the folder
                logging.info(f"Folder '{FolderPath}' created successfully.")
            except OSError as e:
                logging.error(f"Error: Unable to create folder '{FolderPath}'. Reason: {e}")
                exit()

            for filepath in Filelist:
                    try:
                        shutil.move(filepath, FolderPath)
                        moved_filepath = os.path.join(FolderPath, os.path.basename(filepath))   # New file path after moving
                        MovedFileslist.append(moved_filepath)                                        
                        logging.info("File moved successfully.")
                    except FileNotFoundError:
                        logging.error("Error: Source file not found.")
                    except shutil.Error as e:
                        logging.error(f"Error: Failed to move file. Reason: {e}")
                        exit()   
            ZipFiles()      
    else:
        logging.error("The given filepath does not exist")
        exit() 
        

GatherFiles(DirPath)
shutil.move( FolderPath + ".zip", DestinationPath)
logging.info("Zip file moved successfully.")
DeleteFolder()



#Without Json file