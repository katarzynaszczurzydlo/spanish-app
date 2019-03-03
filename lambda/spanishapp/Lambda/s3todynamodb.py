import json
import boto3


def handler(event, context):
    s3 = boto3.resource('s3')
    content_object = s3.Object('spanish-app-db', 'dynamodb.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    data = json.loads(file_content)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('spanishapp')

    for Vocabulary in data["Vocabulary"]:
        english = Vocabulary['English']
        spanish= Vocabulary['Spanish']
        print("Adding translation:", english, spanish)

        table.put_item(
            Item={
                'English': english,
                'Spanish': spanish,
            }
        )
