"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="reader")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    reader_id = Column(Integer, ForeignKey('readers.id'))
    reader = relationship("Reader", back_populates="books")

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


new_Anna = Reader(name="Анна")
session.add(new_Anna)
new_Yana = Reader(name="Яна")
session.add(new_Yana)
session.commit()

# Создание новой книги и добавление ее в базу данных для указанного читателя
new_book = Book(title="Гордость и Предубеждение", author="Джейн Остин", reader=new_Anna)
session.add(new_book)
new_book1 = Book(title="Вино из одуванчиков", author="Рэй Брэдбери", reader=new_Anna)
session.add(new_book1)
new_book2 = Book(title="Преступление и наказание", author="Федор Михайлович Достоевский", reader=new_Yana)
session.add(new_book2)
new_book3 = Book(title="Вишневый сад", author="Антон Чехов", reader=new_Yana)
session.add(new_book3)
session.commit()

def get_books_for_reader(reader_name):
    reader = session.query(Reader).filter_by(name=reader_name).first()
    if reader:
        books = reader.books
        if books:
            for book in books:
                print(f"Название: {book.title}, Автор: {book.author}")
        else:
            print("У читателя нет книг.")
    else:
        print("Читатель не найден.")


reader_name = input("Введите имя читателя: ")
get_books_for_reader(reader_name)

