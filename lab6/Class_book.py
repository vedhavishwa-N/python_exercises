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

