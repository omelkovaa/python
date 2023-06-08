"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника, всех работников по должности, всех работников определенной должности со стажем больше 5.
"""


from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

employee_position_association = Table(
    'employee_position_association',
    Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('position_id', Integer, ForeignKey('positions.id'))
)

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(Integer)
    positions = relationship("Position", secondary=employee_position_association, back_populates="employees")

class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", secondary=employee_position_association, back_populates="positions")

engine = create_engine('sqlite:///company.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

positions = [
    Position(name="Software Engineer"),
    Position(name="Data Analyst"),
    Position(name="Project Manager"),
    Position(name="UI/UX Designer")
]
session.add_all(positions)
session.commit()

employees = [
    Employee(name=" Ignat Peskovatckov", experience=3, positions=[positions[0], positions[1]]),
    Employee(name="Yana Margacheva", experience=7, positions=[positions[1], positions[2]]),
    Employee(name="Anna Omelkova", experience=5, positions=[positions[2], positions[3]]),
    Employee(name="Vitaliy Suranov", experience=2, positions=[positions[3], positions[0]])
]
session.add_all(employees)
session.commit()

def get_employee_positions(employee_name):
    employee = session.query(Employee).filter_by(name=employee_name).first()
    if employee:
        positions = employee.positions
        if positions:
            print(f"Должности работника {employee_name}:")
            for position in positions:
                print(position.name)
        else:
            print("У работника нет должностей.")
    else:
        print("Работник не найден.")

def get_employees_by_position(position_name):
    position = session.query(Position).filter_by(name=position_name).first()
    if position:
        employees = position.employees
        if employees:
            print(f"Работники с должностью {position_name}:")
            for employee in employees:
                print(employee.name)
        else:
            print("На данной должности нет работников.")
    else:
        print("Должность не найдена.")

def get_employees_by_position_and_experience(position_name):
    employees = session.query(Employee).join(employee_position_association).join(Position).filter(Position.name == position_name, Employee.experience > 5).all()
    if employees:
        print(f"Работники на должности {position_name} со стажем больше 5:")
        for employee in employees:
            print(f"Имя: {employee.name}, Стаж: {employee.experience}")
    else:
        print(f"На должности {position_name} нет работников со стажем больше 5.")

employee_name = input("Введите имя работника: ")
get_employee_positions(employee_name)

position_name = input("Введите название должности: ")
get_employees_by_position(position_name)

position_name = input("Введите название должности: ")
get_employees_by_position_and_experience(position_name)