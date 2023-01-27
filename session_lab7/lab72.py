"""Prompt the user to enter the name of a city and email ID
-Download the wikipedia page of that specific city using "requests" library and pickup the html content
-Using "BeautifulSoup4", process the html to identify the src of the
 first image that shows up on the page ( Please ignore logos, images in banners if any etc. )
Download the image using requests library and save the image temporarily in the local filesystem
Send the image as an attachment to the email ID provided by the user with
an appropriate subject and body. ( smtp, email )
"""
#the requests library id used to use urls in the program
import requests
#bs4 is used for using the returned html content
import bs4

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from email.message import EmailMessage
import smtplib


print ("enter the name of the city : ")
city = input ()
url = "https://en.wikipedia.org/wiki/{}".format (city)
response = requests.get (url)
html_text = response.content

soup = bs4.BeautifulSoup (html_text, 'html.parser')
info_box = soup.find ("table", {"class": "infobox"})
image_tag = info_box.find ("img")
src = image_tag.attrs ["src"]
if src.startswith ("//"):
   src = url.split ("//")[0] + src
img_url = src
print (img_url)
file_name = "{}.jpg".format (city)
with open (file_name, "wb") as file_write:
   print ("downloading {}".format (file_name))
   response = requests.get (img_url)
   content = response.content
   file_write.write (content)

print("{} downloaded sucessfully".format(file_name))

message= EmailMessage()
email_sender = "onetester60@gmail.com"
email_password="fhlmavlzuzrgcxqj"
email_reciever=input("enter reciever email")
subject=input("enter the email subject")
body=input("enter the email content")

message=MIMEMultipart()
message['from']=email_sender
message['to']=email_reciever
message['subject']=subject

message.attach(MIMEText(body, 'plain'))
attach_file_name = file_name
# Open the file as binary mode
with open(attach_file_name, 'rb') as attach_file:
   payload = MIMEBase('image','jpg',filename='chennai.jpg')
   payload.set_payload((attach_file).read())
   #encode the attachment
   encoders.encode_base64(payload) 

   #add payload header with filename
   payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
   message.attach(payload)

#Create SMTP session for sending the mail
with smtplib.SMTP('smtp.gmail.com', 587) as session:
   #use gmail with port
   session.starttls() #enable security
   #login with mail_id and password
   session.login(email_sender, email_password) 
   text = message.as_string()
   session.sendmail(email_sender, email_reciever, text)

print('Mail Sent')

