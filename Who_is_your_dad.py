dad = {
    'Антон': ['отец Владимир', 'дед Александр'],
    'Дима': ['отец Виталий', 'дед Максим'],
    'Даша': ['отец Кирилл', 'дед Василий'],
    'Кристина': ['отец Владислав', 'дед Анатолий'],
    'Женя': ['отец Максим', 'дед Игорь']
}

menu = None

while menu != 0:

    menu = int(input('''
        1) Добавить ребенка и отца в словарь.
        2) Заменить отца ребенка в словаре.
        3) Удалить ребенка и отца со словаря.
        4) Найти пару ребенок/отец по имени ребенка.
        5) Найти пару ребенок/дед по имени ребенка.
        6) Посмотреть полный список.
        0) Выйти из программы.

        Выберите соответствующий пункт меню: 
    '''))

    if menu == 1:
        new_name_child = input('Введите имя ребенка: \n')
        new_name_dad = input('Введите имя отца: \n')
        if new_name_child not in dad:
            dad[new_name_child] = new_name_dad
            print('Вы добавили новую пару отца и сына в словарь: ', new_name_child, ':', new_name_dad)
        else:
            print('К сожалению нельзя добавить эту пару т.к. она уже есть в словаре.')

    if menu == 2:
        new_name_child = input('Введите имя ребенка у которого хотите изменить имя отца: \n')
        if new_name_child in dad:
            new_name_dad = input('Введите имя нового отца: \n')
            dad[new_name_child] = new_name_dad
            print('Вы успешно заменили отца у ребенка на', new_name_child, ':', new_name_dad)
        else:
            print('К сожалению такого имени', new_name_child, 'нет в нашем словаре.')

    if menu == 3:
        new_name_child = input('Введите имя ребенка, чтобы удалить пару "ребенок/отец" из словаря: \n')
        if new_name_child in dad:
            del dad[new_name_child]
            print('Вы успешно удалили имя ребенка', new_name_child, 'из словаря')
        else:
            print('К сожалению такого имени', new_name_child, 'нет в нашем словаре.')

    if menu == 4:
        name_child = input('Введите имя ребенка: \n')
        if name_child in dad:
            print('У', name_child, dad.get(name_child)[0])
        else:
            print('К сожалению такого имени', name_child, 'нет в нашем словаре.')

    if menu == 5:
        name_child = input('Введите имя ребенка: \n')
        if name_child in dad:
            print('У', name_child, dad.get(name_child)[1])
        else:
            print('К сожалению такого имени', name_child, 'нет в нашем словаре.')

    if menu == 6:
        print('Полный список детей и их отцов:')
        print('\n', dad, end='\n')

    if menu == 0:
        print('До свидания!')
        exit()