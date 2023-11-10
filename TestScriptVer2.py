import os
import tkinter
from tkinter import messagebox
from datetime import date
from datetime import datetime

# "C:\\Users\\jjebaeta\\Documents\\LOGS"

DirPath = "C:\\Users\\Joao Joseph Baeta\\Documents\\Fidelity\\TestFiles"
Threshold = 100*1024*1024                                           #100mb in bytes

def ChangeName(filename):                                   #Function that changes the name of the file 
    DirPath = DirPath                                  
    oldpath = os.path.join(DirPath,filename)
    NewFileName = filename + datetime.now().strftime('%Hh%M') 
    newpath = os.path.join(DirPath,NewFileName)
    os.rename(oldpath, newpath)
    return newpath

def Crosscheck(DirPath):
    if(os.path.exists(DirPath)):                                    #Checks to see if the directory path exists
        DirectoryList = os.listdir(DirPath)                         #List of all the files in the directory
        for file in DirectoryList:
            filePath = os.path.join(DirPath,file)
            filesize = os.path.getsize(filePath)
            Justfilename=datetime.now().strftime('%d%b%y')
            filename= datetime.now().strftime('%d%b%y') + ".log"
            if(file == Justfilename):
                print("File Match Found")
                print("Search Criteria: " + filename)
                if(filesize >= Threshold):
                    print("File size has exceeded threshold")
                    print("Initializing name change process.........")
                    Path=ChangeName(Justfilename)
                    print("File name has been successfully changed to: \n" + Path)
                    exit()
                else:
                    print("File size is in the acceptable range")
                    exit()
    else:
        tkinter.messagebox.showinfo("Fidelity Bank ",  "The given filepath does not exist")
        exit()    
            
    
Crosscheck(DirPath)









