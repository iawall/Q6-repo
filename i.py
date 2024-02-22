
 #Original
'''class Library:
    def __init__(self,title, author, genre, registered):
        self.title = title
        self.author = author
        self.genre = genre
        self.registered = registered

    def searchBookTitle(title):
        print(f"Searching for books with title {title}")

    def searchBookAuthor(author):
        print(f"Searching for books with author {author}")

    def searchBookTitle(genre):
        print(f"Searching for books with genre {genre}")

    def borrowBook(title, registered):
        if(registered == True):
            print(f"Borrowing: {title}")
        else:
            print("invalid")
    
    def returnBook(title, registered):
        if(registered == True):
            print(f"Returning book: {title}")
        else:
            print("invalid")

    def reports():
        print("Generating reports")

'''

# ISP

class Searchable:
    def search_book_by_title(self, title):
        print(f"Searching for books with title '{title}'")

    def search_book_by_author(self, author):
        print(f"Searching for books by author '{author}'")

    def search_book_by_genre(self, genre):
        print(f"Searching for books in genre '{genre}'")


class Borrowable:
    def borrow_book(self, title, registered):
        if (registered == True):
            print(f"Borrowing: {title}")
        else:
            print("invalid")


class Returnable:
    def return_book(self, title, registered):
        if (registered == True):
            print(f"Returning book: {title}")
        else:
            print("invalid")


class Reportable:
    def generate_reports(self):
        print("Generating reports")


class Library(Searchable, Borrowable, Returnable, Reportable):
    def __init__(self, title, author, genre, registered):
        self.title = title
        self.author = author
        self.genre = genre
        self.registered = registered

    def main(self):
        self.search_book_by_title("Diary of a Wimpy Kid")
        self.borrow_book("Diary of a Wimpy Kid", True)
        self.generate_reports()


def main():
    # Creating an instance of Library with dummy values
    library = Library("Diary of a Wimpy Kid", "Jeff Kinney", "Kids Comedy", True)
    library.main()


if __name__ == "__main__":
    main()
