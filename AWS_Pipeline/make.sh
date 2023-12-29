#!/bin/bash

# The new zip file name passed as an argument
NEW_ZIP_FILE=$1

# Check if an argument is provided
if [ -z "$NEW_ZIP_FILE" ]; then
    echo "Usage: $0 <zip_file_name>"
    exit 1
fi

# Create formation.yaml
cat << EOF > format.yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  lambdafunction:
    Type: 'AWS::Lambda::Function'
    Properties:
      FunctionName: DataXcelerator_lambda
      Runtime: python3.8
      Handler: ETL.lambda_handler
      Role: arn:aws:iam::476844305051:role/lambda-execution-role
      Code:
        S3Bucket: hassan786
        S3Key: $NEW_ZIP_FILE
EOF

echo "format.yaml created with S3Key: $NEW_ZIP_FILE"
