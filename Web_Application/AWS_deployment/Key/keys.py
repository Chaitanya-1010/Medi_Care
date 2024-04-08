import boto3

access_key="AKIA3FLD5YR6JFSG5IGQ"
secret_access_key= "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"
dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'us-east-2',
              aws_access_key_id = access_key,
              aws_secret_access_key = secret_access_key)

appointment_history_table=dynamo_client.Table("Appointments_History")
patients_record_table=dynamo_client.Table("Patient_Records")

