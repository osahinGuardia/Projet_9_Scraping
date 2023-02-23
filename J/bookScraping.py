import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
from J.scraper import Scraping

from J.Book import Book

base_url = "https://www.decitre.fr"
uri = "/livres/nouveautes.html?p="
last_page = 30


def swoup(url):
    return BeautifulSoup(requests.get(url).text, "lxml")


def format_book(book_array):
    books_data = []
    for book in book_array:
        if book:
            book_dict = {
                'name': book.get_name(),
                'author': book.get_author(),
                'price': book.get_price()
            }
            books_data.append(book_dict)
    return books_data


def extract_book_data(book_cards):
    books = []
    for book_card in book_cards:
        name = (book_card.find("a", class_="product-title").text.replace(" ", "").strip())
        author = (book_card.find("div", class_="authors").find("a").text.strip())
        price = (book_card.find("span", class_="final-price").text.strip())
        books.append(Book(name, author, price))
    return books


def main():
    books = [extract_book_data(soup.findAll("li", class_="dct-product clearfix fiche-produit product-availability-01"))
             for soup in [swoup(base_url + uri + str(page)) for page in range(1, last_page + 1)]]

    books = [book for sublist in books for book in sublist]
    books = format_book(books)
    data_frame = pd.DataFrame(books)
    data_frame.to_csv("books.csv", index=False)


main()
