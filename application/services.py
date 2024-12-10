from domain.models import Book


class LibraryService:
    """Сервис для управления библиотекой книг."""

    def __init__(self, repository):
        """
        Инициализирует сервис библиотеки.

        :param repository: Репозиторий для хранения книг.
        """
        self.repository = repository

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет книгу в библиотеку.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        """
        book_id = self.repository.get_next_id()
        new_book = Book(id=book_id, title=title, author=author, year=year)
        self.repository.add(new_book)

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу из библиотеки по ID.

        :param book_id: Уникальный идентификатор книги для удаления.
        """
        self.repository.remove(book_id)

    def search_books(self, query: str) -> list:
        """Ищет книги по названию, автору или году.

        :param query: Запрос для поиска книг.
        :return: Список найденных книг.
        """
        return self.repository.search(query)

    def display_books(self) -> None:
        """Отображает все книги в библиотеке.

        :return: Список всех книг в библиотеке.
        """
        return self.repository.get_all()

    def update_status(self, book_id: int, new_status: str) -> None:
        """Обновляет статус книги по ID.

        :param book_id: Уникальный идентификатор книги.
        :param new_status: Новый статус книги ("в наличии" или "выдана").
        """
        self.repository.update_status(book_id, new_status)
