import boto3
region = 'ap-south-1'

SourceAddress = 'ajlabs110@gmail.com'
ToAddresses = ['vpjaseem@gmail.com',]
CcAddresses = ['vpjaseem@gmail.com',]
ReplyToAddresses = ['ajlabs110@gmail.com',]
Template = 'SAMPLE_TEMPLATE'


ses = boto3.client('ses', region_name=region)
response = ses.send_templated_email(
  Source=SourceAddress,
  Destination={
    'ToAddresses': ToAddresses,
    'CcAddresses': CcAddresses
  },
  ReplyToAddresses=ReplyToAddresses,
  Template=Template,
  TemplateData='{ \"REPLACEMENT_TAG_NAME\":\"REPLACEMENT_VALUE\" }'
)

print(response)
