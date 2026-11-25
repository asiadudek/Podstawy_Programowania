
class Ebook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True
    
    def close_book(self):
        self.is_open = False

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def show_status(self):
        print(f"Current number of page: {self.current_page}")
        if self.is_open:
            print("The book is open")
        else:
            print("The book is closed")

    def next_page(self):
        if not self.is_open:
            print("Book is closed, open it first")
        elif self.current_page < self.pages:
            self.current_page += 1
        else:
            print("This is the last page")

    def previous_page(self):
        if not self.is_open:
            print("Book is closed, open it first")
        elif self.current_page > 1:
            self.current_page -= 1
        else:
            print("This is the first page")