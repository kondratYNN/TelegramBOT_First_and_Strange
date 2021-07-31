import random


def game():
    print('Это игра "Угадай число". Программой было загадано число, Вам необходимо его угадать.')

    levels = {1: 10, 2: 7, 3: 5}
    maximum_count = levels[int(input("Выберите уровень сложности:\n"
                                     "1 - 10 попыток\n"
                                     "2 - 7 попыток\n"
                                     "3 - 5 попыток\n"
                                     "Вы выбираете: "))]

    players_amount = int(input('Пожалуйста, введите количество игроков: '))

    players = []
    for i in range(players_amount):
        players.append(input('Имя игрока №{}: '.format(i + 1)))

    game_numbers = [random.randint(0, 100) for x in range(players_amount)]
    print('Каждому игроку было загадано число. Игра начинается!')
    is_winner = False
    count = 0
    while not is_winner:
        count += 1
        if count > maximum_count:
            print('Все пользователи проиграли')
            break
        print('Попытка №{}'.format(count))
        for i in range(players_amount):
            print('Ходит {}'.format(players[i]))
            user_number = int(input('Пожалуйста, введите число: '))
            if user_number < game_numbers[i]:
                print('Введенное Вами число меньше загаданного.')
            elif user_number > game_numbers[i]:
                print('Введенное Вами число больше загаданного.')
            else:
                print('Выйграл игрок {}! Вы молодец!'.format(players[i]))
                is_winner = True
                break
