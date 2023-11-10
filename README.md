# Author: Joao Joseph Evenunye Baeta
# Date: 2023-08-09

ReadMe File for ArchiverVer4.sh


# Overview
This is a script that takes all files in a given directory that are older than a specified number of days and compresses them into a zip file. The script then moves the zipped file to a specified archive directory.


# Running the program
The script can be ran either from an IDE or command prompt depending on the file that is selected (ArchiverVer4.py files or the ArchiverVer4.sh file). The ArchiverVer4.sh file is a bash script that runs the ArchiverVer4.py file. The ArchiverVer4.py file can be ran from any IDE that supports python such as Pycharm or VScode however the ArchiverVer4.sh file can be run from the command line using the following command:

```sh

prompt> ./ArchiverVer4.sh

```

Before running either the python script or the bash script, the user must specify the following variables in the script:
    Variable                     Description
    DirPath                      This is the path to the directory that contains the files to be archived
    DestinationPath              This is the path to the directory that the zipped file will be moved to (Archive directory)
    StartDate                    This is the date that the script will start archiving files from. The format of the date is YYYY-MM-DD

With the DirPath and DestinationPath, the user must specify the path to the directory containing the files to be archived and the final archive directory with the necessary naming conventions. 

The StartDate is calulated through the difference between the current date and the number of days from which to archive from. The number of days is specified by the user in the program by changing the value of the variable "days" in the timedelta function in the StartDate Variable. An example is shown below:\

Assuming number of days is 5.
```sh

StartDate = EndDate - timedelta(days=5)

```

# Results
After running the script, the user should see the following output in the command line or log file:

1.The number of files that were found 
2.If a folder containing the Start date 
3.If the files were sucessfully moved 
4.If the zip file was sucessfully created
5.If the files were sucessfully moved to the zip file
6.If the zip file was sucessfully moved to the archive directory
7.If the original folder containing the files was sucessfully deleted

Below is an example of the output from the script: 

```sh
    2023-08-09 12:11 - 2 File(s) found before the start date
    2023-08-09 12:11 - Folder '/path/to/your/source/folder/20230730' created successfully.
    2023-08-09 12:11 - File moved successfully.
    2023-08-09 12:11 - File moved successfully.
    2023-08-09 12:11 - Zip file created successfully.
    2023-08-09 12:11 - Files moved and zipped successfully.
    2023-08-09 12:11 - Zip file moved successfully.
    2023-08-09 12:11 - Folder '/path/to/your/source/folder/20230730' deleted successfully.
```






