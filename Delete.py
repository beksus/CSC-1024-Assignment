# notification: this is main field of Delete

class Delete:

    # this function is for deleting the books 
    def delete_book(self, book_list, book):
        #de = str(input("enter book to delete: "))
        
        for i in book_list:
            if i.getter(7) == book or i.getter(0) == book or i.getter(1) == book:
                book_list.remove(i)
                return 1
        # if there is no book exists
        return -1
                