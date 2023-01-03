"""import csv
import requests
url ="https://free4kwallpapers.com/uploads/originals/2020/09/05/ultra-violet-k-wallpaper.jpg"
file_name="walp.jpg"
fw = open(file_name,"wb")
print("downloading {}".format(file_name))
response = requests.get(url)
content = response.content
fw.write(content)
fw.close()"""

"""/////////////////////////////////////////
import os
#specify the path in os.listdir(path) or run empty for current dir checking

print(os.listdir())
list_of_dir=os.listdir()
for file in list_of_dir:
    filename=file
    file_type=file.split('.')[-1]
    print("the file {} is of type {}".format(filename,file_type))

"""
"""def get_filetype(filepath): # is not general any file /fi
    import magic
    file_type = magic.from_file(filepath)
    return file_type
print(get_filetype('cities.txt'))"""

"""import magic


def get_filetype(filepath):  # is not general any file /fi

    file_type = magic.from_file(filepath)
    return file_type



print(get_filetype())"""
"""import os
files=os.listdir()
print(files)
def getimage_directory(file):
    for x in files:
       if x.endswith(".png") or x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".gif"):
            location=os.getcwd()
            return location
image_name="ghost.jpg"
print(getimage_directory(image_name))
"""
"""import os
images=list()
def images_in_dir(path):
    all_files=os.listdir(path)
    for file in all_files:
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".gif"):
            images.append(file)
    return images
location=os.getcwd()
print("all the images in the given location is:",images_in_dir(location))
"""
import os
import smtplib

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



    print("till this")



    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    print("sucessfil login",)
    smtp.sendmail('sender email',"vedha0943@gmail.com",msg.as_string())
    print("done")