print('''
                Добро пожаловать в игру "Генератор персонажей"
                  У вас есть в наличии 30 свободных пунктов.
Пожалуйста распределите их по характеристикам: Сила, Здоровье, Мудрость и Ловкость.
''')

# сила
strength = 0
# здоровье
health = 0
# мудрость
wisdom = 0
# ловкость
agility = 0

point = 30

char_enter = ''

while point != 0:
    print('На данный момент у вас', point, 'свободных пунктов.')
    print('1) Сила: ', strength, '\n'
          '2) Здоровье: ', health, '\n'
          '3) Мудрость: ', wisdom, '\n'
          '4) Ловкость: ', agility, '\n')

    characteristic = int(input('Введите номер характеристики, чтобы добавить в неё пункт: '))
    if characteristic == 1:
        char_enter += '"Сила"'
        point_add = int(input('Сколько поинтов вы хотите добавить в характеристику ' + char_enter + ': '))
        print('Вы добавили', point_add, 'очков в характеристику', char_enter)
        strength += point_add
        point -= point_add

        point_return = int(
            input('Если вы ошиблись, то можете вернуть поинты из характеристики ' + char_enter + ' обратно.\n'
                  'Для этого наберите цифру 1 если хотите вернуть очки или цифру 0 если хотите продолжить: '))
        if point_return == 1:
            strength -= point_add
            point += point_add
            print('Окей, ваши очки возвращены обратно.')
        char_enter = ''

    elif characteristic == 2:
        char_enter += '"Здоровье"'
        point_add = int(input('Сколько поинтов вы хотите добавить в характеристику ' + char_enter + ': '))
        health += point_add
        point -= point_add
        char_enter = ''

        point_return = int(
            input('Если вы ошиблись, то можете вернуть поинты из характеристики ' + char_enter + ' обратно.\n'
                  'Для этого наберите цифру 1 если хотите вернуть очки или цифру 0 если хотите продолжить: '))
        if point_return == 1:
            health -= point_add
            point += point_add
            print('Окей, ваши очки возвращены обратно.')
        char_enter = ''

    elif characteristic == 3:
        char_enter += '"Мудрость"'
        point_add = int(input('Сколько поинтов вы хотите добавить в характеристику ' + char_enter + ': '))
        wisdom += point_add
        point -= point_add
        char_enter = ''

        point_return = int(
            input('Если вы ошиблись, то можете вернуть поинты из характеристики ' + char_enter + ' обратно.\n'
                  'Для этого наберите цифру 1 если хотите вернуть очки или цифру 0 если хотите продолжить: '))
        if point_return == 1:
            wisdom -= point_add
            point += point_add
            print('Окей, ваши очки возвращены обратно.')
        char_enter = ''

    elif characteristic == 4:
        char_enter += '"Ловкость"'
        point_add = int(input('Сколько поинтов вы хотите добавить в характеристику ' + char_enter + ': '))
        agility += point_add
        point -= point_add
        char_enter = ''

        point_return = int(
            input('Если вы ошиблись, то можете вернуть поинты из характеристики ' + char_enter + ' обратно.\n'
                  'Для этого наберите цифру 1 если хотите вернуть очки или цифру 0 если хотите продолжить: '))
        if point_return == 1:
            agility -= point_add
            point += point_add
            print('Окей, ваши очки возвращены обратно.')
        char_enter = ''

print('Вы распределили все очки по характеристикам!')
print('На данный момент у вас', point, 'свободных пунктов и характеристики выглядят так:')
print('Сила: ', strength, '\n'
      'Здоровье: ', health, '\n'
      'Мудрость: ', wisdom, '\n'
      'Ловкость: ', agility, '\n')