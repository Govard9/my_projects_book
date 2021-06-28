import random

class Location:
    COUNTRY = ['1) Россия'], ['2) Африка'], ['3) Испания'], ['4) Аргентина'], ['5) США']

    COUNTRY_TELEPORT = [['1) Россия']], \
                       [['2) Африка']], \
                       [['3) Испания']], \
                       [['4) Аргентина']], \
                       [['5) США']]
    clone_name = ''

    def named(self):
        """Имя игрока"""
        name = input('Введите ваше имя: ')
        print('Добро пожаловать в игру', name)
        Location.clone_name += name


class Dialogue():
    choices = ''
    choices_new = ''
    trim_countrys = ''

    def dialog_country(self, choice):
        """Показ меню"""
        self.choice = choice

        Dialogue.choices += self.choice

        if self.choice == '1':
            print('Окей,', Location.clone_name, 'вы телепортировались в Россию, не завидую я вам конечно...')

        elif self.choice == '2':
            print('О мой бог, ', Location.clone_name + ',', 'вы попали в ад под названием Африка, берегите себя...')

        elif self.choice == '3':
            print('Хорошо,', Location.clone_name, 'вы телепортировались в королевство Испания, ох уж эти колонисты!')

        elif self.choice == '4':
            print('Добро пожаловать', Location.clone_name + ',',
                  'вы оказались в Аргентине, ничего об этой стране сказать не могу.')

        elif self.choice == '5':
            print('Еее', Location.clone_name + ',', 'вы попали в США, это почти рай для людей, но берегите свою голову, пуля попадёт на пустом месте...')

        else:
            print('Такой страны нет в списке куда можно телепортироваться')

    def new_dialog_country(self, choice_new):
        """Показ меню"""
        self.choice_new = choice_new

        Dialogue.choices_new += self.choice_new

        if self.choice == 'Россия':
            print('Окей,', Location.clone_name, 'вы телепортировались в Россию, не завидую я вам конечно...')

        elif self.choice == 'Африка':
            print('О мой бог, ', Location.clone_name + ',', 'вы попали в ад под названием Африка, берегите себя...')

        elif self.choice == 'Испания':
            print('Хорошо,', Location.clone_name, 'вы телепортировались в королевство Испания, ох уж эти колонисты!')

        elif self.choice == 'Аргентина':
            print('Добро пожаловать', Location.clone_name + ',',
                  'вы оказались в Аргентине, ничего об этой стране сказать не могу.')

        elif self.choice == 'США':
            print('Еее', Location.clone_name + ',', 'вы попали в США, это почти рай для людей, но берегите свою голову, пуля попадёт на пустом месте...')

        else:
            print('Такой страны нет в списке куда можно телепортироваться')

    def where_now(self):
        """Местоположение человека"""
        for i in Location.COUNTRY:
            if Dialogue.choices in " ".join(i):
                trim_country = " ".join(i)[3:]
                Dialogue.trim_countrys += trim_country
                print('Сейчас вы находитесь в', trim_country)


class RandomKM:
    """Класс для создания рандомных значений. Для списка стран, а именно киллометров"""
    rand_value = []
    add_km = []

    def rand_int(self):
        """Создаёт рандомное число и добавляет его как киллометры. Убирает лишние символы со строки."""
        for i in Location.COUNTRY_TELEPORT:
            add = [random.choice(range(1000, 10000))]
            RandomKM.add_km.append(add)
            i.append(add)
            if Dialogue.trim_countrys in " ".join(str(x)[5:] for x in i):
                continue
            RandomKM.rand_value.append('\n' + " ".join(str(x) for x in i) + ' км от вас.')
        join = " ".join(RandomKM.rand_value).replace('[', '').replace(']', '').replace("'", "")
        print(join)

    def check(self):
        """Проверяет правильный ответ"""
        for j in Dialogue.trim_countrys:
            if j in Dialogue.choices_new:
                for i in RandomKM.rand_value:
                    if " ".join(str(x) for x in min(RandomKM.add_km)) in i:
                        print('Вы успешно телепортировались в ближащее место к вам.')
                        break




class Teleport:
    countries = []

    def country_selection(self):
        """Изменение первого списка стран"""
        for i in Location.COUNTRY:
            Teleport.countries.append('\n' + " ".join(i))
        print(" ".join(Teleport.countries))


loc_name = Location()
tel = Teleport()
dia = Dialogue()
rand = RandomKM()


# Спрашиваем имя человека
loc_name.named()
# Вычисляем страны в первый раз (без км)
tel.country_selection()
# Вызываем диалог о странах
dia.dialog_country(input('\nВыберите любую страну в которую вы хотите телепортироваться: '))
# Говорим где мы сейчас находимся
dia.where_now()
# Создаёт рандомное число для киллометров.
rand.rand_int()
# Вызываем диалог о странах
dia.new_dialog_country(input('\nВыберите страну которая ближе к вам (напишите её название): '))
rand.check()

