# spanish-app
Flask application

Main page
![Main](https://drive.google.com/uc?export=view&id=1xH4zRVTEV0wFWwRGmmS59TsmmzZLIMI-)

Quiz page
![Quiz](https://drive.google.com/uc?export=view&id=170vh38RG0vQDJsecRJNFSN3c_AbEzzvQ)

Vocabulary page
![Vocabulary](https://drive.google.com/uc?export=view&id=124pdKAszhPmNvxe05yPgdS_BcaENvKoR)

## Getting Started

These instructions will help you deploy the application.

### Prerequisites

You need to have AWS account.

### Deploying

First deploy the Flask application to EC2 and create the AMI. Include the AMI in the spanishapp.yaml file. Create the CloudFormation stack using the spanishapp.yaml. The stack creates AutoScaling group, DynamoDB and AWS Lambda. There is some sample data for DynamoDB available in dynamodb.json. Upload that file to the S3 bucket created via the stack. It will trigger the Lambda to populate the DynamoDB table.
