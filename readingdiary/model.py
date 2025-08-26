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

    def __init__(self, isbn: str, tittle: str,author: str, pages: int, rating: int ,notes: list):
        self.isbn: str = isbn
        self.tittle: str = tittle
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list = []








