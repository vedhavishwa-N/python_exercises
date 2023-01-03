import csv
import requests
csv_file = "bk.csv"

f = open(csv_file,"r")

dr = csv.DictReader(f)
print(dr)
for book in dr:
    book_dict = dict(book)
    url = book_dict["image_url"]
    file_name = url.split("/")[-1]
    fw = open(file_name,"wb")
    print("downloading {}".format(file_name))
    response = requests.get(url)
    content = response.content
    fw.write(content)
    fw.close()