"""Prompt the user to enter the name of a city and email ID
-Download the wikipedia page of that specific city using "requests" library and pickup the html content
-Using "BeautifulSoup4", process the html to identify the src of the
 first image that shows up on the page ( Please ignore logos, images in banners if any etc. )
Download the image using requests library and save the image temporarily in the local filesystem
Send the image as an attachment to the email ID provided by the user with
an appropriate subject and body. ( smtp, email )
"""
import requests
import bs4

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from email.message import EmailMessage
import smtplib


print("enter the name of the city : ")
city=input()
url = "https://en.wikipedia.org/wiki/{}".format(city)
response = requests.get(url)
html_text = response.content

soup = bs4.BeautifulSoup(html_text,'html.parser')
infobox = soup.find("table", {"class":"infobox"})
image_tag = infobox.find("img")
src = image_tag.attrs["src"]
if src.startswith("//"):
   src = url.split("//")[0] + src
img_url=src
print (img_url)
file_name = "{}.jpg".format(city)
fw = open(file_name,"wb")
print("downloading {}".format(file_name))
response = requests.get(img_url)
content = response.content
fw.write(content)



email_sender="onetester60@gmail.com"
message= EmailMessage()
email_password="fhlmavlzuzrgcxqj"
email_reciever="vedhavishwa@tivonaglobal.com"#input("enter reciever email")
subject="test"  #input("enter the email subject")
body="hi"#input("enter the email content")

message=MIMEMultipart()
message['from']=email_sender
message['to']=email_reciever
message['subject']=subject

message.attach(MIMEText(body, 'plain'))
attach_file_name = 'chennai.jpg'
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('image','jpg',filename='chennai.jpg')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(email_sender, email_password) #login with mail_id and password
text = message.as_string()
session.sendmail(email_sender, email_reciever, text)
session.quit()

print('Mail Sent')

