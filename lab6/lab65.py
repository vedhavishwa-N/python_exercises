

    


class EBook(Book):
    def __init__(self, book_id, title, author, binding, pages, price, isbn, image_url, formats, size_in_kb, is_drm_protected):
        self.format = formats
        self.size_in_kb = size_in_kb
        self.is_drm_protected = is_drm_protected
        super().__init__( book_id, title, author, binding, pages, price, isbn, image_url)

    def __str__(self):
        return "book_id-{}\ntitle-{}\nauthor-{}\nbinding-{}\n pages-{}\nprice-{}\nisbn-{}\nimage_url-{}\nformat-{}\nsize-{}\ndrm-{}".format(self.book_id, self.title, self.author, self.binding, self.pages, self.price, self.isbn, self.image_url, self.format, self.size_in_kb, self.is_drm_protected)

book = EBook('book_id', 'title', 'author', 'binding', 'pages', 'price', 'isbn', 'image_url', 'formats', 'size_in_kb', 'is_drm_protected')
print(book)
