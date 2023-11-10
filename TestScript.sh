#!/bin/bash

DirPath="/path/to/source/directory"
Threshold=$((100*1024*1024)) # 100 MB in bytes

function ChangeName() {
    DirPath='/path/to/source/directory'
    local oldpath="$DirPath/$1"
    local newpath="$DirPath/${1}$(date +'%Hh%M')"
    mv "$oldpath" "$newpath"
    echo "$newpath"
}

function Crosscheck() {
    if [ -d "$DirPath" ]; then
        DirectoryList=$(ls "$DirPath")
        for file in $DirectoryList; do
            filePath="$DirPath/$file"
            filesize=$(stat -c%s "$filePath")
            Justfilename=$(date +'%d%b%y')
            filename=$(date +'%d%b%y').log
            if [ "$file" == "$Justfilename" ]; then
                echo "File Match Found"
                echo "Search Criteria: $filename"
                if [ "$filesize" -ge "$Threshold" ]; then
                    echo "File size has exceeded threshold"
                    echo "Initializing name change process........."
                    Path=$(ChangeName "$Justfilename")
                    echo "File name has been successfully changed to:"
                    echo "$Path"
                    exit
                else
                    echo "File size is in the acceptable range"
                    exit
                fi
            fi
        done
    else
        echo "The given filepath does not exist"
        exit
    fi
}

Crosscheck "$DirPath"




