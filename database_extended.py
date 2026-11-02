from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "sqlite:///analytics_library.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    nationality = Column(String(100))
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publication_year = Column(Integer)
    genre = Column(String(100))
    price = Column(Float)
    author = relationship("Author", back_populates="books")
    orders = relationship("Order", back_populates="book")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    customer_name = Column(String(255))
    order_date = Column(Date)
    quantity = Column(Integer, default=1)
    book = relationship("Book", back_populates="orders")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
