# notification: this is main field of Delete

class Delete:

    # this function is for deleting the books 
    def delete_book(self, book_list, book:str):
        
        for i in book_list:
            if i.getter(7) == book or i.getter(0) == book or i.getter(1) == book:
                book_list.remove(i)
                return 1
        # if there is no book exists
        return -1

     #so can delete more than one book
    def delete_books(self, book_list, book:str, num:int):
        count = 0
        books_to_delete = [i for i in book_list if (i.getter(7) == book or i.getter(0) == book or i.getter(1) == book) and count < num]
    
        for book in books_to_delete:
                book_list.remove(book)
                count += 1
        return count  # returns the number of books deleted
                    

  
