from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаём движок для SQLite
DATABASE_URL = "sqlite:///library.db"
engine = create_engine(DATABASE_URL, echo=True)

# База для декларативного описания таблиц
Base = declarative_base()

# Описываем таблицу Books
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year = Column(Integer)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', year={self.year})>"

# Создаём таблицы
Base.metadata.create_all(engine)

# Создаём сессию для работы с БД
Session = sessionmaker(bind=engine)
session = Session()
