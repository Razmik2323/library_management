from dataclasses import dataclass

@dataclass
class Book:
    """Класс, представляющий книгу в библиотеке."""
    id: int      # Уникальный идентификатор книги
    title: str   # Название книги
    author: str  # Автор книги
    year: int    # Год издания книги
    status: str = "в наличии"  # Статус книги (по умолчанию "в наличии")

