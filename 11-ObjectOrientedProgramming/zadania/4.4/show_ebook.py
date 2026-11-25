from ebook import Ebook

def main():
    book = Ebook("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 223)
    
    book.open_book()
    book.show_info()
    book.next_page() #czytamy kilka stron
    book.next_page()
    book.next_page()
    book.show_status()
    book.close_book()

    book.next_page() #proba czytania zamknietej ksiazki

if __name__ == "__main__":
    main()