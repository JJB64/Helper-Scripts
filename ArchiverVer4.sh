#!/bin/bash

# Configure logging
touch LogFile.log
exec > >(while IFS= read -r line; do echo "$(date +"%Y-%m-%d %H:%M") - $line"; done | tee -a LogFile.log)
exec 2> >(while IFS= read -r line; do echo "$(date +"%Y-%m-%d %H:%M") - $line" >&2; done | tee -a LogFile.log)

dir_path="/mnt/c/Users/Joao Joseph Baeta/Documents/Fidelity/TestFiles"
destination_path="/mnt/c/Users/Joao Joseph Baeta/Documents/Fidelity/Archive"

# Set Date data
end_date=$(date +"%Y-%m-%d")
end_date_str="$end_date"
start_date=$(date -d "-10 days" +"%Y-%m-%d")
start_date_str="$start_date"

filelist=()
moved_files_list=()

# Create folder path
date_range_str="${start_date//-/}"
folder_path="$dir_path/$date_range_str"

delete_folder() {
  rm -rf "$folder_path"
  echo "Folder '$folder_path' deleted successfully."
}

zip_files() {
  zip -q "$folder_path.zip" -j "${moved_files_list[@]}"
  echo "Zip file created successfully."
}

gather_files() {
  if [ -d "$dir_path" ]; then
    file_count=0

    for file_path in "$dir_path"/*; do
      file_creation_date=$(date -r "$file_path" +%Y-%m-%d)

      if [ "$(date -d $file_creation_date +%s)" -lt "$(date -d $start_date +%s)" ]; then
        ((file_count++))
        filelist+=("$file_path")
      fi
    done

    if [ "$file_count" -eq 0 ]; then
      echo "No files found before the start date"
      exit
    else
      echo "$file_count File(s) found before the start date"

      mkdir -p "$folder_path"
      echo "Folder '$folder_path' created successfully."

      for filepath in "${filelist[@]}"; do
        base_name=$(basename "$filepath")
        mv "$filepath" "$folder_path/$base_name"
        moved_files_list+=("$folder_path/$base_name")
        echo "File moved successfully."
      done

      zip_files
      echo "Files moved and zipped successfully."
    fi
  else
    echo "The given filepath does not exist"
    exit
  fi
}

gather_files
mv "$folder_path.zip" "$destination_path"
echo "Zip file moved successfully."
delete_folder
