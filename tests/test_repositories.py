import unittest
from infrastructure.repositories import BookRepository
from domain.models import Book


class TestBookRepository(unittest.TestCase):

    def setUp(self):
        self.repository = BookRepository()

    def test_add_book(self):
        book = Book(id=1, title="1984", author="George Orwell", year=1949)
        self.repository.add(book)

        self.assertEqual(len(self.repository.books), 1)
        self.assertEqual(self.repository.books[0].title, "1984")

    def test_add_duplicate_book(self):
        book = Book(id=1, title="1984", author="George Orwell", year=1949)
        self.repository.add(book)

        with self.assertRaises(ValueError):
            self.repository.add(book)  # Попытка добавить книгу с дублирующимся ID

    def test_remove_book(self):
        book = Book(id=1, title="1984", author="George Orwell", year=1949)
        self.repository.add(book)

        self.repository.remove(1)

        self.assertEqual(len(self.repository.books), 0)

    def test_remove_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.repository.remove(999)  # Попытка удалить несуществующую книгу

    def test_search_books(self):
        book1 = Book(id=1, title="1984", author="George Orwell", year=1949)
        book2 = Book(id=2, title="Animal Farm", author="George Orwell", year=1945)

        self.repository.add(book1)
        self.repository.add(book2)

        results = self.repository.search("1984")

        self.assertEqual(len(results), 1)

        results = self.repository.search("George Orwell")

        self.assertEqual(len(results), 2)


if __name__ == '__main__':
    unittest.main()
