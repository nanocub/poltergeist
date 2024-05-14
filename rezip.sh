#!/bin/bash

# Set the name of the folder and zip file
folder_name="poltergeist"
zip_file_name=$folder_name

# Delete the old zip file
find "./" -type f -name '*.zip' -exec grep -q $zip_file_name {} \; -delete


# Set the file path
file_path="$folder_name/__init__.py"

# Use grep and sed to extract the contents of the first set of parentheses
version=$(grep -oP '\([^()]*\)' "$file_path" | head -n 1 | sed 's/[(|)]//g')

# Replace commas with dots
version=${version//,/\.}

# Print the modified contents
echo "$zip_file_name-$version.zip"

zip_file_name="$zip_file_name-$version.zip"

# Create a new zip file from the folder
powershell Compress-Archive $folder_name -DestinationPath $zip_file_name