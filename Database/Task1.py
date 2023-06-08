"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

sqlite_database = "sqlite:///films.sql"

engine = create_engine(sqlite_database)


class Base (DeclarativeBase):
    pass


class Films(Base):

    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    create_year = Column(Integer)
    genre = Column(String)
    rating = Column(Integer)


Base.metadata.create_all(bind=engine)


def create(f_name, f_create_year, f_genre, f_rating):
    with Session(autoflush=False, bind=engine) as db:
        # создаем объект film для добавления в бд
        film = Films(name=f_name, create_year=f_create_year, genre=f_genre, rating=f_rating)
        db.add(film)                # добавляем в бд
        db.commit()                 # сохраняем изменения или db.refresh()


def info_by_name(name_film):
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Films).filter(Films.name == name_film).all()
        for i in films:
            print(f"Информация о фильме: {i.name}, {i.genre}, {i.create_year}, в рейтинге: {i.rating}")


def info():
    with Session(autoflush=False, bind=engine) as db:
        films = db.query(Films).all()
        print("Весь список фильмов:")
        for i in films:
            print(i.name)
        print("_" * 20)


def change_by_id(id_change, name, create_year, genre, rating):
    with Session(autoflush=False, bind=engine) as db:       # получаем один объект, у которого id=1
        film = db.query(Films).filter(Films.id == id_change).first()

        if film != None:
            film.name = name
            film.create_year = create_year
            film.genre = genre
            film.rating = rating
            db.commit()
            print(f"Изменено: {id_change}")


def delete(id_del):
    with Session(autoflush=False, bind=engine) as db:
        del_film = db.query(Films).filter(Films.id == id_del).first()
        db.delete(del_film)      # удаляем обьект
        db.commit()              # сохраняем изменения
        print(f"Удалено: {id_del}")


create("Beauty and the Beast", 2017, 'Фентези', 15)
create("Euphoria", 2019, 'Драма ', 6)
create("The great", 2020, 'Комедия', 8)
info()
info_by_name('Euphoria')
change_by_id(3, "Птичий короб", 2018, 'Ужас', 9)
info()
delete(3)
info()
