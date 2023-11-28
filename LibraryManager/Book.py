class Book:

    # This dictionary was made to be utilized for getter Method
    index = {
        1: 'id',
        2: 'title',
        3: 'author',
        4: 'publisher',
        5: 'genre',
        6: 'date_published',
        7: 'date_purchased',
        8: 'type'
        }
    # this is constructor for initialising and saving values of Book

    def __init__(self, isbn, author, title, publisher, genre, date_published, date_purchased, status):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.date_published = date_published
        self.date_purchased = date_purchased
        self.status = status
        self.index.update({1: isbn,
                           2: author,
                           3: title,
                           4: publisher,
                           5: genre,
                           6: date_published,
                           7: date_purchased,
                           8: status})


    # I don't know How to use it, it was generated from BlackBox AI so I don't know how to utilize it
    # assume it is a test function


    def __str__(self):
        return (f"{self.title}"
                f" by {self.author}"
                f" was published by "
                f"{self.publisher} in"
                f" {self.genre} in"
                f" {self.date_published}"
                f" and purchased on"
                f" {self.date_purchased}")
       
#this is Getting item Funtion for accessing value of book e.g. title, author etc.

    def getter(self, i):
        return self.index[i]
