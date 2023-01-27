import csv
import requests
csv_file = "bk.csv"

with open(csv_file,"r") as file:

    data = csv.DictReader(file)
    # print(data)
    for row in data:
        book_dict = dict(row)
        url = book_dict["image_url"]
        file_name = url.split("/")[-1]
        file_write = open(file_name,"wb")
        print("downloading {}".format(file_name))
        response = requests.get(url)
        content = response.content
        file_write.write(content)
        file_write.close()