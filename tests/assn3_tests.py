import pytest
import requests

BASE_URL = "http://localhost:5001/books"

book1 = {"title": "Adventures of Huckleberry Finn", "ISBN": "9780520343641", "genre": "Fiction"}
book2 = {"title": "The Best of Isaac Asimov", "ISBN": "9780385050784", "genre": "Science Fiction"}
book3 = {"title": "Fear No Evil", "ISBN": "9780394558783", "genre": "Biography"}
book4 = {"title": "No such book", "ISBN": "0000001111111", "genre": "Biography"}
book5 = {"title": "The Greatest Joke Book Ever", "authors": "Mel Greene", "ISBN": "9780380798490", "genre": "Jokes"}
book6 = {"title": "The Adventures of Tom Sawyer", "ISBN": "9780195810400", "genre": "Fiction"}
book7 = {"title": "I, Robot", "ISBN": "9780553294385", "genre": "Science Fiction"}
book8 = {"title": "Second Foundation", "ISBN": "9780553293364", "genre": "Science Fiction"}

def test_create_books():
    response1 = requests.post(BASE_URL, json=book1)
    response2 = requests.post(BASE_URL, json=book2)
    response3 = requests.post(BASE_URL, json=book3)
    assert response1.status_code == 201
    assert response2.status_code == 201
    assert response3.status_code == 201
    assert response1.json()["ID"] != response2.json()["ID"]
    assert response1.json()["ID"] != response3.json()["ID"]
    assert response2.json()["ID"] != response3.json()["ID"]

def test_get_book():
    response = requests.post(BASE_URL, json=book1)
    book_id = response.json()["ID"]
    response = requests.get(f"{BASE_URL}/{book_id}")
    assert response.status_code == 200
    assert response.json()["authors"] == "Mark Twain"

def test_get_books():
    response1 = requests.post(BASE_URL, json=book1)
    response2 = requests.post(BASE_URL, json=book2)
    response3 = requests.post(BASE_URL, json=book3)
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_invalid_book():
    response = requests.post(BASE_URL, json=book4)
    assert response.status_code in [400, 500]

def test_delete_book():
    response = requests.post(BASE_URL, json=book2)
    book_id = response.json()["ID"]
    response = requests.delete(f"{BASE_URL}/{book_id}")
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/{book_id}")
    assert response.status_code == 404

def test_invalid_genre():
    response = requests.post(BASE_URL, json=book5)
    assert response.status_code in [400, 422]

def test_create_additional_books():
    response4 = requests.post(BASE_URL, json=book6)
    response5 = requests.post(BASE_URL, json=book7)
    response6 = requests.post(BASE_URL, json=book8)
    assert response4.status_code == 201
    assert response5.status_code == 201
    assert response6.status_code == 201
