import zipfile


files = ["hi.txt"]
archive = "archive.zip"
password = b"verysecret"

with zipfile.ZipFile(archive, "w") as zf:
    for file in files:
        zf.write(file)

    zf.setpassword(password)

with zipfile.ZipFile(archive, "r") as zf:
    crc_test = zf.testzip()
    if crc_test is not None:
        print(f"Bad CRC or file headers: {crc_test}")

    info = zf.infolist()
    print(info)
    file = info[0]
    with zf.open(file) as f:
        print(f.read().decode())


    zf.extract(file, "/tmp", pwd=password)

import os
import tarfile


def py_files(members):
    for tarinfo in members:
            if os.path.splitext(tarinfo.name)[1] == ".py":
                yield tarinfo


    tar = tarfile.open("sample.tar.gz")
    tar.extractall(members=py_files(tar))
    tar.close()
py_files(archive)