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
        8: 'status'
        }
    
    # this is constructor for initialising and saving values of Book

    

    def __init__(self, list):
        """for i in range(len(list)+1):
            self.index.update({i+1: list[i]})
"""
        self.index.update({1: list[0],
                           2: list[1],
                           3: list[2],
                           4: list[3],
                           5: list[4],
                           6: list[5],
                           7: list[6],
                           8: list[7]})

        

        


    # I don't know How to use it, it was generated from BlackBox AI ,so I don't know how to utilize it
    # assume it is a test function


    
       
# this is Getting item Funtion for accessing value of book e.g. title, author etc.

    def getter(self, i):
        return self.index[i]
