list = []
while True:
    game = input('Введите настольную игру:').lower()
    if game in list:
        print('Эта игра уже записана')
    elif game == '0':
        list.sort()
        print(list)
        break
    else:
        list.append(game)
