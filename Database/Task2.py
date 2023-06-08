"""
Создайте базу данных пользователя состояющую из следующих столбцов: id,username,password(В виде хэша).
Создайте программу которая предлагает пользователю зарегистрироваться или авторизироваться.
При регистрации программа запрашивает логин и пароль и добавляет в базу данных нового пользователя.
При авторизации программа запрашивает логин и пароль и выводит сообщение об успешной/неуспешной авторизации.
"""
from werkzeug. security import generate_password_hash
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
import sqlite3
import hashlib

class Base (DeclarativeBase):
    pass

conn = sqlite3.connect('users.sql')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT)''')


action = input("Вы хотите зарегистрироваться (R) или войти (L)? ").lower()

if action == 'r':  # Регистрация нового пользователя
    username = input("Введите имя: ")
    password = input("Введите пароль: ")


    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()


    c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    print('Аккаунт успешно создан')

elif action == 'l':
    username = input("Введите имя: ")
    password = input("Введите пароль: ")


    c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = c.fetchone()

    if result is None:
        print("Неправильный логин или пароль")
    else:
        password_hash = result[0]

        if hashlib.sha256(password.encode('utf-8')).hexdigest() == password_hash:
            print("Вы вошли успешно")
        else:
            print("Неправильный логин или пароль")

conn.close()
