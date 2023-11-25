class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.book = book

    def __str__(self):
        return f"{self.title} by {self.author} was published by {
            self.publisher} in {self.genre} in {self.date_published
                                                } and purchased on {self.date_purchased}"
                    