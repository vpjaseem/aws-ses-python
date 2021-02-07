import boto3
region = 'ap-south-1'

SourceAddress = 'ajlabs110@gmail.com'
ToAddresses = ['vpjaseem@gmail.com',]
CcAddresses = ['vpjaseem@gmail.com',]
ReplyToAddresses = ['ajlabs110@gmail.com',]
Subject = "AJClassRoom Direct Email"

CharSet = "UTF-8"
BodyText = (
    "AJClassRoom Direct Email\r\n"
    "This email was sent with Amazon SES"
    )

BodyHTML = """<html>
<head>
	<title>AWS SES Sample Email</title>
</head>
<body>
	<h1>AJClassRoom AWS Training</h1>
	<p>AJClassRoom provides industry standard AWS Training.</p>
	<p>Subscribe our YouTube Channel <br/>
	   <a href="https://www.youtube.com/watch?v=vq_hBqS1Yyg&list=PLGTrjI6v74MBCphTOUoomZAxL6M1OaLx6" target="_blank">English</a>
	   <a href="https://www.youtube.com/watch?v=20sxMs7oyHI&list=PLbB6UW7gIJdAm3weMTBhRu_YaRjDLlvSk" target="_blank">  Malayalam</a>
	</p>
	<p>Contact: <a href="https://www.linkedin.com/in/abdul-jaseem" target="_blank">LinkedIn</a></p>
</body>
</html>
"""  


ses = boto3.client('ses', region_name=region)
response = ses.send_email(
  Source=SourceAddress,
  Destination={
    'ToAddresses': ToAddresses,
    'CcAddresses': CcAddresses
  },
  ReplyToAddresses=ReplyToAddresses,

  Message={
            'Body': {
                'Html': {
                    'Charset': CharSet,
                    'Data': BodyHTML,
                },
                'Text': {
                    'Charset': CharSet,
                    'Data': BodyText,
                },
            },
            'Subject': {
                'Charset': CharSet,
                'Data': Subject,
            },
        },
  
)

print(response)
