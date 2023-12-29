#!/bin/bash

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <zip_file_name>"
    exit 1
fi

# List files in the current directory for debugging
echo "Listing files in the current directory:"
ls -l

# File name of the CloudFormation template
FORMATION_FILE="formation.yaml"

# The new zip file name passed as an argument
NEW_ZIP_FILE=$1

# Update S3Key in the formation.yaml file
sed -i "s|S3Key: .*|S3Key: $NEW_ZIP_FILE|" $FORMATION_FILE

# Echo a message for confirmation
echo "Updated S3Key in $FORMATION_FILE to $NEW_ZIP_FILE"

