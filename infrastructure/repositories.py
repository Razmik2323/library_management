from abc import ABC, abstractmethod
from domain.models import Book


class BookRepositoryInterface(ABC):
    """Абстрактный класс для интерфейса репозитория книг."""

    @abstractmethod
    def add(self, book: Book) -> None:
        """Добавляет книгу в репозиторий."""
        pass

    @abstractmethod
    def remove(self, book_id: int) -> None:
        """Удаляет книгу из репозитория по ID."""
        pass

    @abstractmethod
    def search(self, query: str) -> list:
        """Ищет книги по названию или автору."""
        pass

    @abstractmethod
    def get_all(self) -> list:
        """Возвращает все книги из репозитория."""
        pass

    @abstractmethod
    def get_next_id(self) -> int:
        """Генерирует уникальный идентификатор для новой книги."""
        pass

    @abstractmethod
    def update_status(self, book_id: int, new_status: str) -> None:
        """Обновляет статус книги по ID."""
        pass


class BookRepository(BookRepositoryInterface):
    """Конкретная реализация репозитория книг."""

    def __init__(self):
        """Инициализирует новый экземпляр BookRepository с пустым списком книг."""
        self.books = []

    def add(self, book: Book) -> None:
        """Добавляет книгу в репозиторий.

        :param book: Книга для добавления в репозиторий.
        :raises ValueError: Если книга с таким ID уже существует.
        """
        if any(b.id == book.id for b in self.books):
            raise ValueError(f"Книга с ID {book.id} уже существует.")
        self.books.append(book)

    def remove(self, book_id: int) -> None:
        """Удаляет книгу из репозитория по ID.

        :param book_id: Уникальный идентификатор книги для удаления.
        :raises ValueError: Если книга с указанным ID не найдена.
        """
        for i, book in enumerate(self.books):
            if book.id == book_id:
                del self.books[i]
                return
        raise ValueError(f"Книга с ID {book_id} не найдена.")

    def search(self, query: str) -> list:
        """Ищет книги по названию или автору.

        :param query: Запрос для поиска книг.
        :return: Список найденных книг.
        """
        return [book for book in self.books if query.lower() in (book.title.lower() or book.author.lower())]

    def get_all(self) -> list:
        """Возвращает все книги из репозитория.

        :return: Список всех книг.
        """
        return self.books

    def get_next_id(self) -> int:
       """Генерирует уникальный идентификатор для новой книги.

       :return: Следующий уникальный идентификатор книги.
       """
       return len(self.books) + 1  # Генерация уникального ID

    def update_status(self, book_id: int, new_status: str) -> None:
       """Обновляет статус книги по ID.

       :param book_id: Уникальный идентификатор книги.
       :param new_status: Новый статус книги ("в наличии" или "выдана").
       :raises ValueError: Если книга с указанным ID не найдена.
       """
       for book in self.books:
           if book.id == book_id:
               book.status = new_status
               return
       raise ValueError(f"Книга с ID {book_id} не найдена.")
