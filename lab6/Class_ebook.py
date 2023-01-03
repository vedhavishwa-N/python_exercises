import Class_book

class EBook(Class_book.Book):
    def __init__(self, book_id, title, author, binding, pages, price, isbn, formats, size_in_kb,
                 is_drm_protected, image_url):
        self.format = formats
        self.size_in_kb = size_in_kb
        self.is_drm_protected = is_drm_protected
        super().__init__( book_id, title, author, binding, pages, price, isbn, image_url)


book = EBook('book_id', 'title', 'author', 'binding', 'pages', 'price', 'isbn', 'image_url', 'formats', 'size_in_kb', 'is_drm_protected')
print(book)
