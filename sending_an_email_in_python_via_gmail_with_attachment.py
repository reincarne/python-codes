import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#The content
mail_message = """Hello,
I'm sending you a Python test!
Have a good day.
"""

#The mail addresses and password
sender_address = 'XXX@gmail.com' #use your email
sender_pass = 'XXX' #use your password
receiver_address = 'XXX@gmail.com'

#Setup the MIME (Multipurpose Internet Mail Extensions)
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'

#The body and the attachments for the mail
message.attach(MIMEText(mail_message, 'plain'))

#Send with attachment
filename = 'PATH_TO_FILE' #modify the path to the file
attachment = open(filename,'rb')

attach = MIMEBase('application','octet-stream')
attach.set_payload((attachment).read())
encoders.encode_base64(attach)
attach.add_header('Content-Disposition',"attachment; filename= "+filename)

message.attach(attach)

#SMTP server and session settings
session = smtplib.SMTP('smtp.gmail.com', 587) #SMTP server settings
session.starttls() #Secure the session
session.login(sender_address, sender_pass) #Login
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
