# notification: this is main field of Delete

class Delete:

    # this function is for deleting the books 
    def delete_book(self, book_list, book:str):
        
        for i in book_list:
            if i.getter(7) == str(book) or i.getter(0) == str(book) or i.getter(1) == str(book):
                book_list.remove(i)
                break
        # if there is no book exists
        return -1
                