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
import os
import smtplib


print("enter the name of the city : ")
city=input()
print("enter your email id")
email=input()
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
fw.close()


from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
EMAIL_ADDRESS = "onetester60@gmail.com"#input('enter your email address')
EMAIL_PASSWORD = "fhlmavlzuzrgcxqj"#input('enter password')
msg=MIMEMultipart()
msg['subject']='check out the image'
msg['From'] = EMAIL_ADDRESS
msg['To']  = "vedha.natarajan3@gmail.com"#input('enter your receiver email address')

with open('chennai.jpg','rb')as f:
    mime =MIMEBase('image','jpg',filename='chennai1.jpg')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

with smtplib.SMTP_SSL( "smtp.gmail.com",465)as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    print("sucessfil login",)
    smtp.sendmail('sender email',"vedha0943@gmail.com",msg.as_string())
    print("done")