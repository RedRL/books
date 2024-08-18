# import pytest
# import requests

# BASE_URL = "http://localhost:5001/books"

# book1 = {"title": "Adventures of Huckleberry Finn", "ISBN": "9780520343641", "genre": "Fiction"}
# book2 = {"title": "The Best of Isaac Asimov", "ISBN": "9780385050784", "genre": "Science Fiction"}
# book3 = {"title": "Fear No Evil", "ISBN": "9780394558783", "genre": "Biography"}
# book4 = {"title": "No such book", "ISBN": "0000001111111", "genre": "Biography"}
# book5 = {"title": "The Greatest Joke Book Ever", "authors": "Mel Greene", "ISBN": "9780380798490", "genre": "Jokes"}
# book6 = {"title": "The Adventures of Tom Sawyer", "ISBN": "9780195810400", "genre": "Fiction"}
# book7 = {"title": "I, Robot", "ISBN": "9780553294385", "genre": "Science Fiction"}
# book8 = {"title": "Second Foundation", "ISBN": "9780553293364", "genre": "Science Fiction"}

# # Global variable to store the IDs of created books
# book_ids = {}


# def test_create_books():
#     response1 = requests.post(BASE_URL, json=book1)
#     response2 = requests.post(BASE_URL, json=book2)
#     response3 = requests.post(BASE_URL, json=book3)
#     assert response1.status_code == 201
#     assert response2.status_code == 201
#     assert response3.status_code == 201

#     # Store the IDs globally
#     book_ids['book1_id'] = response1.json()["ID"]
#     book_ids['book2_id'] = response2.json()["ID"]
#     book_ids['book3_id'] = response3.json()["ID"]

#     assert book_ids['book1_id'] != book_ids['book2_id']
#     assert book_ids['book1_id'] != book_ids['book3_id']
#     assert book_ids['book2_id'] != book_ids['book3_id']


# def test_get_book():
#     book_id = book_ids['book1_id']  # Reuse the ID from the previous test
#     response = requests.get(f"{BASE_URL}/{book_id}")
#     assert response.status_code == 200
#     assert response.json()["authors"] == "Mark Twain"


# def test_get_books():
#     response = requests.get(BASE_URL)
#     assert response.status_code == 200

#     # Expecting the number of books created so far
#     assert len(response.json()) == 3


# def test_invalid_book():
#     response = requests.post(BASE_URL, json=book4)
#     assert response.status_code in [400, 500]


# def test_delete_book():
#     book_id = book_ids['book2_id']  # Reuse the ID from the previous test
#     response = requests.delete(f"{BASE_URL}/{book_id}")
#     assert response.status_code == 200

#     # Confirm the book has been deleted
#     response = requests.get(f"{BASE_URL}/{book_id}")
#     assert response.status_code == 404


# def test_invalid_genre():
#     response = requests.post(BASE_URL, json=book5)
#     assert response.status_code == 422


# def test_create_additional_books():
#     response4 = requests.post(BASE_URL, json=book6)
#     response5 = requests.post(BASE_URL, json=book7)
#     response6 = requests.post(BASE_URL, json=book8)
#     assert response4.status_code == 201
#     assert response5.status_code == 201
#     assert response6.status_code == 201

# ----- NIR TEST ------ 

import requests

BASE_URL = "http://localhost:5001/books"

book6 = {
    "title": "The Adventures of Tom Sawyer",
    "ISBN": "9780195810400",
    "genre": "Fiction"
}

book7 = {
    "title": "I, Robot",
    "ISBN": "9780553294385",
    "genre": "Science Fiction"
}

book8 = {
    "title": "Second Foundation",
    "ISBN": "9780553293364",
    "genre": "Science Fiction"
}

books_data = []


def test_post_books():
    books = [book6, book7, book8]
    for book in books:
        res = requests.post(BASE_URL, json=book)
        assert res.status_code == 201
        res_data = res.json()
        assert "ID" in res_data
        books_data.append(res_data)
        books_data_tuples = [frozenset(book.items()) for book in books_data]
    assert len(set(books_data_tuples)) == 3


def test_get_query():
    res = requests.get(f"{BASE_URL}?authors=Isaac Asimov")
    assert res.status_code == 200
    assert len(res.json()) == 2


def test_delete_book():
    res = requests.delete(f"{BASE_URL}/{books_data[0]['ID']}")
    assert res.status_code == 200


def test_post_book():
    book = {
        "title": "The Art of Loving",
        "ISBN": "9780062138927",
        "genre": "Science"
    }
    res = requests.post(BASE_URL, json=book)
    assert res.status_code == 201



def test_get_new_book_query():
    res = requests.get(f"{BASE_URL}?genre=Science")
    assert res.status_code == 200
    res_data = res.json()
    assert res_data[0]["title"] == "The Art of Loving"
