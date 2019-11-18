# Python code to illustrate Sending mail from 
# your Gmail account 

import smtplib 
from email.mime.text import MIMEText
# creates SMTP session 
def sendmail(to, msg):
	print("gud")
	print(to)
	print(msg)
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("helloword1965@gmail.com", "jayjayjay@143") 
	SUBJECT = 'Library Management System'
	FROM = 'helloword1965@gmail.com'
	msg = msg
	msg = MIMEText(msg)
	msg['Subject'] = SUBJECT
	msg['To'] = to
	msg['From'] = FROM
	s.sendmail("helloword1965@gmail.com", to , msg.as_string()) 
	s.quit() 

