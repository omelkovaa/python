def get_reg(reg):
    if "расп" in reg.lower():
        schedule()

    elif "направ" in reg.lower():
        training()

    elif "конт" in reg.lower():
        contact()

    elif "плат" in reg.lower():
        price()

    elif "тренеры" in reg.lower():
        coaches()

def schedule():
    print("Пн - 18:00-21:00,"
          "Ср - 16:30-19:30,"
          "Пт - 15:00-21:00,")


def price():
    print("Цена занятий : 3400")


def training():
    print("Направления: Силовая тренировка, Растяжка, TRX, МФР")


def contact():
    print("Контакты: +79242887465")


def coaches():
    print("Тренеры: Иванова Мария, Трубова Дарья, Сергеев Алексей")