# Author: Joao Joseph Evenunye Baeta
# Date: 2023-08-09

ReadMe File for TestScript.sh and TestScriptVer2.py


# Overview
This is a script that checks all the log files in a given directory to see if they exceed a size of 100mb. If they do, they are renamed.


# Running the program
The script can be ran either from an IDE or command prompt depending on the file that is selected (TestScriptVer2.py files or the TestScript.sh file). The TestScript.sh file is a bash script that runs the TestScriptVer2.py file. The TestScriptVer2.py file can be ran from any IDE that supports python such as Pycharm or VScode however the TestScript.sh file can be run from the command line using the following command:
```sh

prompt> ./TestScript.sh

```

Before running either the python script or the bash script, the user must specify the following variables in the script:
    Variable                     Description
    DirPath                      This is the path to the directory that contains the files that need to be checked


The user must specify the path to the directory containing the files with the necessary naming conventions. 
Here is an example of the path to the directory containing the files:
```sh

DirPath = "/path/to/your/source/folder"

```

# Results
After running the script, the user should see the following output in the command line or log file:

1.Whether a match was found or not
2.Whether the File is in an acceptable range or not
3.Initialization of name chnaging process
4.Confirmation of name change


Below is an example of the output from the script: 
```sh

    2023-08-07 14:54:29,478 - INFO - File Match Found
    2023-08-07 14:54:29,478 - INFO - Search Criteria: 07Aug23.log
    2023-08-07 14:54:29,478 - WARNING - File size has exceeded threshold
    2023-08-07 14:54:29,478 - INFO - Initializing name change process.........
    2023-08-07 14:54:29,478 - INFO - File name has been successfully changed to: /path/to/your/source/folder/07Aug2314h54

```
or

```sh

    2023-08-07 14:53:53,180 - INFO - File Match Found
    2023-08-07 14:53:53,180 - INFO - Search Criteria: 07Aug23.log
    2023-08-07 14:53:53,180 - INFO - File size is in the acceptable range

```






     