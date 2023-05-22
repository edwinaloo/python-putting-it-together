#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        if not isinstance(page_count, int):
            raise TypeError("page_count must be an integer")
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


# Test the Book class
try:
    book = Book("Harry Potter", 272)
except TypeError as e:
    print(str(e))

# expected_message = "page_count must be an integer"
# assert error_message == expected_message, f"Error message mismatch: {error_message} != {expected_message}

book = Book("Harry Potter", 69)
book.turn_page()
pass
    
        