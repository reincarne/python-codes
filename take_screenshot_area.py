#Instructions:
# 1) This script works with Python3*
# 2) Need to install missing modules, Example: "G:\Python3\python.exe -m pip install pyautogui"
# The reuired modules to be installed are: pyautogui , smtplib
# 3) It is possible that more modules will be missing, they can be installed the same way.
# 4) Top stop this script, simply click CTRL+C or just close the window.

import pyautogui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import sys
import time
import glob
import os

#Define parameters for screenshot name and path for files
screenshotName = "screenshot"
path = "c:/Users/reinc/Desktop/atch/"

#Define screenshot position on screen, the area that will be taken as screenshot.
x_start_point = 245
y_start_point = 70
x_area = 1675
y_area = 790

#Get current date values to use as suffix for file name & email
now = datetime.datetime.now()
now_two_params = str(now).split(" ")
date = str(now_two_params[0])
raw_time = str(now_two_params[1]).split(".")
time_raw = str(raw_time[0])
time_clean = time_raw.replace(':', '')

#Take a screenshot
try:
    print("Taking a screenshot...")
    screenshot = 
    .screenshot(path + screenshotName + date + "_" + time_clean +".png",region=(x_start_point,y_start_point, x_area, y_area))
except Exception as e:
    print(e)
print("Screenshot taken, parameters of the file is: " + str(screenshot))
files_path = os.path.join(path, '*')
files = sorted(
    glob.iglob(files_path), key=os.path.getctime, reverse=True)

last_screenshot = files[0]
print("Latest screenshot is " + str(last_screenshot))


#Sender email address parameters
email_user = 'YOUR@EMAIL'
email_password = 'YOURPASSWORD'

#Destination address (to whom I should send the email)
email_send = 'EMAIL HERE'

#Define the email subject here
subject = 'MetaTrader Screenshot email'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

#Define body text here
body = 'This is an automated email, sending this email from local PC'

msg.attach(MIMEText(body,'plain'))

filename = last_screenshot
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachmentattachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

try:
    print("Sending email to: " + str(email_send))
    server.sendmail(email_user,email_send,text)
except Exception as e:
    print(e)
print("Email sent succesfully")
server.quit()
