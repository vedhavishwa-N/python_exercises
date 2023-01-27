"""Explore standard library modules to help us compress files and folders into tar or zip archives.
 Write 2 sample programs to demonstrate the use of these modules
 to create a tar archive and zip archive from a local folder on your computer
"""
import zipfile


file = ["hi.txt"]
archive = "test_zip.zip"
password = b"verysecret"

with zipfile.ZipFile(archive, "w") as zip_file:
    for content in file:
        zip_file.write(content)

    zip_file.setpassword(password)
    print("converted to a zipfile")

with zipfile.ZipFile(archive, "r") as zip_file:
    crc_test = zip_file.testzip()
    if crc_test is not None:
        print(f"Bad CRC or file headers: {crc_test}")

    info = zip_file.infolist()
    print(info)
    file = info[0]
    with zip_file.open(file) as f:
        print(f.read().decode())


    zip_file.extract(file, "/tmp", pwd=password)

import os
import tarfile
# r − reads a TAR file by opening it.
# r − Reads an uncompressed TAR file when it is opened.
# w or w − Opens a TAR file for uncompressed writing
# a or a − Opens a TAR file for appending without compression.
# r:gz − opens a TAR file that has been compressed with gzip for reading.
# w:gz − opens a TAR file that has been compressed with gzip for writing.
# r:bz2 − opens a TAR file with bzip2 compression for reading.
# w:bz2 − opens a TAR file with bzip2 compression for writing.

#Creating the tar file
with tarfile.open("TutorialsPoint.tar", 'w') as File:
    files = os.listdir(".")
    for x in files:
        File.add(x)

    #Listing the files in tar
    for x in File.getnames():
        print (f"added the files {x}")
