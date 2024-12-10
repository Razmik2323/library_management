import unittest
from application.services import LibraryService
from infrastructure.repositories import BookRepository
from domain.models import Book


class TestLibraryService(unittest.TestCase):

    def setUp(self):
        self.repository = BookRepository()
        self.library_service = LibraryService(self.repository)

    def test_add_book(self):
        self.library_service.add_book("1984", "George Orwell", 1949)

        books = self.library_service.display_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "1984")

    def test_remove_book(self):
        self.library_service.add_book("1984", "George Orwell", 1949)

        books_before_removal = self.library_service.display_books()
        self.assertEqual(len(books_before_removal), 1)

        self.library_service.remove_book(1)

        books_after_removal = self.library_service.display_books()
        self.assertEqual(len(books_after_removal), 0)

    def test_remove_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library_service.remove_book(999)  # Попытка удалить несуществующую книгу

    def test_search_books(self):
        self.library_service.add_book("1984", "George Orwell", 1949)
        self.library_service.add_book("Animal Farm", "George Orwell", 1945)

        results = self.library_service.search_books("1984")
        self.assertEqual(len(results), 1)

        results = self.library_service.search_books("George Orwell")
        self.assertEqual(len(results), 2)

    def test_update_status(self):
        self.library_service.add_book("1984", "George Orwell", 1949)

        books_before_update = self.library_service.display_books()
        self.assertEqual(books_before_update[0].status, "в наличии")

        self.library_service.update_status(1, "выдана")

        books_after_update = self.library_service.display_books()
        self.assertEqual(books_after_update[0].status, "выдана")


if __name__ == '__main__':
    unittest.main()
