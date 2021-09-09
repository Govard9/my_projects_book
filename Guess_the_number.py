from random import randrange, randint


RAND = randint(1, 100)
ATTEMPT = 0


def main(question, low, high, step):
    """Загадывает рандомное число"""
    global RAND
    global ATTEMPT
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
        while response != RAND:
            if ATTEMPT >= 7:
                print('\nТвои попытки закончились! Всего хо-ро-ше-го. :)')
                exit()
            elif response < RAND:
                print('Введите число побольше. ')
                ATTEMPT += 1
            else:
                print('Введите число поменьше. ')
                ATTEMPT += 1
            response = int(input('Введите число: '))
    return response


def hello():
    """Приветствие"""
    print('Добро пожаловать в игру "Угадай число".\n'
          'И так, тебе нужно угадать с 7 попыток правильное число.\n'
          'Ты готов?')


def yes_no_func():
    """Спрашиваем хочет ли начать игру. Да или нет."""
    yes_no = input('Да/Нет \n')

    while yes_no == 'Нет' or yes_no == 'нет':
        if yes_no == 'Нет' or yes_no == 'нет':
            print('Иди значит готовься, салага!')
        exit()
    print('Ну раз готов, значит погнали!!!!!!!!!!!')


def the_end():
    """Конец игры"""
    print('Отлично, вы попали прямо в цель это и есть число', RAND, '!\n')
    print('Кстати, ты всего лишь потратила ', ATTEMPT, 'попыток, молодец!')


hello()

yes_no()

main(question='Введите число из диапозона от 1 до 100: ', low=1, high=100, step=1)

the_end()
