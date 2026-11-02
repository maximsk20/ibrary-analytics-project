import csv
from datetime import date
from database_extended import session, Author, Book, Order

def populate_sample_data():
    """Заполняем базу тестовыми данными."""
    # Авторы
    author1 = Author(name="Лев Толстой", nationality="Русский")
    author2 = Author(name="Джейн Остин", nationality="Английский")
    session.add_all([author1, author2])
    session.commit()

    # Книги
    book1 = Book(title="Война и мир", author_id=author1.id, publication_year=1869, genre="Роман", price=500.0)
    book2 = Book(title="Гордость и предубеждение", author_id=author2.id, publication_year=1813, genre="Роман", price=300.0)
    session.add_all([book1, book2])
    session.commit()

    # Заказы
    order1 = Order(book_id=book1.id, customer_name="Иван Иванов", order_date=date(2023, 10, 1), quantity=2)
    order2 = Order(book_id=book2.id, customer_name="Мария Петрова", order_date=date(2023, 10, 5), quantity=1)
    session.add_all([order1, order2])
    session.commit()

def sales_analysis():
    """Анализируем продажи по жанрам."""
    result = session.execute("""
        SELECT b.genre, SUM(o.quantity) as total_sold, SUM(o.quantity * b.price) as revenue
        FROM books b
        JOIN orders o ON b.id = o.book_id
        GROUP BY b.genre
    """)
    print("\n--- Анализ продаж по жанрам ---")
    for row in result:
        print(f"Жанр: {row[0]}, Продано: {row[1]}, Выручка: {row[2]:.2f} руб.")

    # Экспорт в CSV
    with open('sales_report.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Жанр', 'Продано', 'Выручка (руб)'])
        for row in result:
            writer.writerow([row[0], row[1], f"{row[2]:.2f}"])
    print("Отчёт сохранён в sales_report.csv")

if __name__ == "__main__":
    populate_sample_data()
    sales_analysis()
    session.close()
