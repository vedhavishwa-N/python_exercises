import csv
class Book(object):
    def __init__(self,book_id,	title,	author,	binding, pages,	price,	isbn,	image_url):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.binding=binding
        self.pages=pages
        self.price=price
        self.isbn=isbn
        self.image_url=image_url

    def __str__(self):
            return "book_id-{}\ntitle-{}\nauthor-{}\nbinding-{}\n pages-{}\nprice-{}\nisbn-{}\nimage_url-{}\n".format(
                self.book_id, self.title, self.author, self.binding, self.pages, self.price, self.isbn,
                self.image_url, )


filename = "100b.csv"

fields = []
rows = []
with open(filename, 'r') as file1:
    r = csv.reader(file1)

    fields = next(r)

    for row in r:

        rows.append(row)

num=1
for row in rows:

    a=row[0]
    b=row[1]
    c=row[2]
    d=row[3]
    e=row[4]
    f=row[5]
    g=row[6]
    h=row[7]


    OBJECT=Book(a,b,c,d,e,f,g,h)
    print("""object-{} - 
          {}""".format(num,OBJECT),'\n')
    num=num+1

