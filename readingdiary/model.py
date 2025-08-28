from datetime import datetime


class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date



    def __str__(self)   -> str:
        pass


class Book:

    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, tittle: str,author: str, pages: int):
        self.isbn: str = isbn
        self.tittle: str = tittle
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self,text: str, page:int, date: datetime)-> bool:
        if page > self.pages:
            return False

        n_note = Note(text, page, date)
        self.notes.append(n_note)
        return True


    def set_rating(self, rating: int) -> bool:
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        self.rating = rating
        return True

    def get_notes_of_page (self, page: int) -> list[Note]:
        notes_of_page = []

    def page_with_most_notes (self) -> int:
        if not self.notes:
            return -1


    def __str__ (self) -> str:
        rating_str = {
            Book.EXCELLENT: "excellent",
            Book.GOOD: "good",
            Book.BAD: "bad",
            Book.UNRATED: "unrated"
        }[self.rating]

        return (f"ISBN: {self.isbn}\n"
                f"Title: {self.tittle}\n"
                f"Author: {self.author}\n"
                f"Pages: {self.pages}\n"
                f"Rating: {rating_str}")



class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn not in self.books:
            return false
        self.books[isbn] = Book(isbn, title, author, pages)
        return True

    def search_by_isbn(self, isbn: str) -> Book











