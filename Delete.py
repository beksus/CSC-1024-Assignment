class Delete:

    # this function is for deleting the books 
    def delete_book(self, book_list, book):
        #de = str(input("enter book to delete: "))
        try:
            for i in book_list:
                if i.getter(7) == book or i.getter(0) == book or i.getter(1) == book:
                    book_list.remove(i)
        except Exception:
            print("this book doesn't exist")
        else:
            print('deleted')
                