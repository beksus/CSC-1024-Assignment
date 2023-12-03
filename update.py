class update
    def update_book():
        isbn_or_title = input("Enter the ISBN or book title and author: ")
        matching_books = [book for book in book_data if isbn_or_title in book]
        if len(matching_books) == 0:
            print("No matching books found.")
        else:
            print("The following book(s) will be updated:")
            for book in matching_books:
                print(book)
            new_book_details = []
            new_book_details.append(input("Enter the new book title: "))
            new_book_details.append(input("Enter the new book author: "))
            new_book_details.append(input("Enter the new book ISBN: "))
            updated_book = ','.join(new_book_details)
            while True:
                update_confirmation = input("Are you sure you want to update these book(s)? (y/n): ").lower()
                if update_confirmation == 'y':
                    for book in matching_books:
                        book_data.remove(book)
                        book_data.append(updated_book)
                    break
                elif update_confirmation == 'n':
                    break