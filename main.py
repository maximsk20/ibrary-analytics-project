from database import session, Book

def add_book(title, author, year):
    """Добавляет новую книгу в базу данных."""
    new_book = Book(title=title, author=author, year=year)
    session.add(new_book)
    session.commit()
    print(f"Книга '{title}' успешно добавлена!")

def show_books():
    """Выводит все книги из базы данных."""
    books = session.query(Book).all()
    if not books:
        print("В библиотеке пока нет книг.")
    else:
        print("Список книг в библиотеке:")
        for book in books:
            print(f"- {book.title} ({book.author}, {book.year})")

if __name__ == "__main__":
    # Добавляем несколько книг
    add_book("Мастер и Маргарита", "Михаил Булгаков", 1966)
    add_book("1984", "Джордж Оруэлл", 1949)
    add_book("Преступление и наказание", "Фёдор Достоевский", 1866)

    # Показываем все книги
    show_books()

    # Закрываем сессию
    session.close()
