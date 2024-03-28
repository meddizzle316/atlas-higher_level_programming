#!/usr/bin/bash

file="$1"
if [ -z "$file" ]; then
    echo "No file given"
    exit 1
fi 
semistandard --fix $file
echo "File fixed"
semistandard | grep $file
echo "Searching for remaining syntax errors"
chmod +x $file
echo "Giving Executable Permissions to file"
