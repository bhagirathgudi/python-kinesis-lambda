import boto3
import uuid
import json

stream_name = 'sample-example'
client = boto3.client('kinesis')

def lambda_handler(event, context):
  partition_key = uuid.uuid4()
  payload = {
    'name':'BHagirath',
    'timestamp': '2018-10-21',
    'radomData':'sdadfafasdfsa'
  }
  
  response = client.put_record(StreamName = stream_name,
  Data= json.dumps(payload),
  PartitionKey = partition_key)
  print(response)
  
  

