import sys
import logging
from application.services import LibraryService
from infrastructure.repositories import BookRepository
from infrastructure.data_storage import DataStorage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_menu() -> None:
    """Отображает меню приложения."""
    menu_options = [
        "1. Добавить книгу",
        "2. Удалить книгу",
        "3. Искать книгу",
        "4. Отобразить все книги",
        "5. Изменить статус книги",
        "6. Выход"
    ]
    print("\nВыберите опцию:")
    print("\n".join(menu_options))


def add_book(library_service: LibraryService) -> str:
    """Добавляет книгу в библиотеку и возвращает сообщение."""
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")

    try:
        year = int(input("Введите год издания книги: "))
        library_service.add_book(title, author, year)
        logging.info(f"Книга '{title}' успешно добавлена.")
        print("Книга успешно добавлена.")
    except ValueError:
        logging.error("Ошибка: год должен быть числом.")


def remove_book(library_service: LibraryService) -> str:
    """Удаляет книгу из библиотеки по ID и возвращает сообщение."""
    try:
        book_id = int(input("Введите ID книги для удаления: "))
        library_service.remove_book(book_id)
        logging.info(f"Книга с ID {book_id} успешно удалена.")
        print("Книга успешно удалена.")
    except ValueError:
        logging.error("Ошибка: ID должен быть числом.")
    except Exception as e:
        logging.error(f"Ошибка при удалении книги: {e}")


def search_books(library_service: LibraryService) -> None:
    """Ищет и отображает книги по запросу."""
    query = input("Введите название или автора для поиска: ")
    results = library_service.search_books(query)

    if results:
        for book in results:
            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
    else:
        logging.info(f"Книги не найдены по запросу '{query}'.")
        print("Книги не найдены.")


def display_books(library_service: LibraryService) -> None:
    """Отображает все книги в библиотеке."""
    books = library_service.display_books()

    if books:
        for book in books:
            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
    else:
        logging.info("В библиотеке нет книг.")
        print("В библиотеке нет книг.")


def update_status(library_service: LibraryService) -> str:
    """Обновляет статус книги по ID и возвращает сообщение."""
    try:
        book_id = int(input("Введите ID книги для изменения статуса: "))
        new_status = input("Введите новый статус (в наличии/выдана): ").strip().lower()

        if new_status not in ["в наличии", "выдана"]:
            raise ValueError("Статус должен быть 'в наличии' или 'выдана'.")

        library_service.update_status(book_id, new_status)
        logging.info(f"Статус книги с ID {book_id} успешно обновлен на '{new_status}'.")
        print("Статус книги успешно обновлен.")

    except ValueError as e:
        logging.error(f"Ошибка: {e}")
        print(f"Ошибка: {e}")
    except Exception as e:
        logging.error(f"Ошибка при обновлении статуса книги: {e}")

def exit_program(library_service: LibraryService) -> None:
    """Сохраняет книги в файл и завершает программу."""
    DataStorage.save_to_file('library.json', library_service.display_books())
    logging.info("Выход из приложения.")
    print("Выход из приложения.")
    sys.exit(0)

def main() -> None:
    """Основная функция для запуска приложения управления библиотекой."""

    repository = BookRepository()

    # Загрузка книг из файла при старте приложения
    books = DataStorage.load_from_file('library.json')
    for book in books:
        repository.add(book)

    library_service = LibraryService(repository)

    actions = {
        '1': lambda: add_book(library_service),
        '2': lambda: remove_book(library_service),
        '3': lambda: search_books(library_service),
        '4': lambda: display_books(library_service),
        '5': lambda: update_status(library_service),
        '6': lambda: exit_program(library_service)
    }

    while True:
        display_menu()

        choice = input("Выберите опцию (1-6): ")

        action = actions.get(choice)
        if action:
            action()
        else:
            logging.warning("Ошибка: неверный выбор. Пожалуйста, выберите опцию от 1 до 6.")
            print("Ошибка: неверный выбор. Пожалуйста, выберите опцию от 1 до 6.")


if __name__ == "__main__":
    main()
