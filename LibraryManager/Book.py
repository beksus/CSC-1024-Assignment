class Book:

    # This dictionary was made to be utilized for getter Method
    index = {
        1:'id',
        2:'title',
        3:'author',
        4:'publisher',
        5:'genre',
        6:'date_pubclished',
        7:'date_purchased',
        8:'type'
        }
    # this is constructor for initalizing and saving values of Book
    def __init__(self, id, author, title, publisher, genre, date_published, date_purchased, type ):
        self.id = id
        self.author = author
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.date_published = date_published
        self.date_purchased = date_purchased
        self.type = type
        self.index.update({1:id, 2:author, 3:title, 4:publisher, 5:genre, 6:date_published, 7:date_purchased, 8:type})


    #idk how to use it, it was generated from BlackBox AI so idk how to utilize it

    def __str__(self):
        return f"{self.title} by {self.author} was published by {self.publisher} in {self.genre} in {self.date_published} and purchased on {self.date_purchased}"
       
    
    
    #this is Getting item Funtion for accessing value of book e.g. title, author etc.
    def getter(self, i):
        return self.index[i]