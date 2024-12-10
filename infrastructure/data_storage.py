import json
from domain.models import Book
from typing import List

import os


class DataStorage:
    """Класс для работы с хранилищем данных (файлы)."""

    @staticmethod
    def save_to_file(filename: str, books: List[Book]) -> None:
        """Сохраняет список книг в файл в формате JSON."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump([book.__dict__ for book in books], file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Ошибка при сохранении данных в файл {filename}: {e}")

    @staticmethod
    def load_from_file(filename: str) -> List[Book]:
        """Загружает список книг из файла в формате JSON."""
        if not os.path.isfile(filename):
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump([], file)
            return []

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return [Book(**item) for item in json.load(file)]
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON в файле {filename}: {e}")
            return []