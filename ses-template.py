import boto3
region = 'ap-south-1'

ses = boto3.client('ses', region_name=region)

response = ses.create_template(
  Template = {
    'TemplateName' : 'SAMPLE_TEMPLATE',
    'SubjectPart'  : 'AJClassRoom Template Email',
    'TextPart'     : 'AJClassRoom AWS Training',
    'HtmlPart'     : """<html>
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
  }
)

#ses.list_templates()
#ses.get_template(TemplateName = 'SAMPLE_TEMPLATE')
#ses.delete_template(TemplateName = 'SAMPLE_TEMPLATE')

