class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        print('Имя питомца:', self.name)
        print('Голод питомца на данный момент:', self.hunger)
        print('Усталость питомца на данный момент:', self.boredom)

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'прекрасно'
        elif 5 <= unhappiness <= 10:
            m = 'неплохо'
        elif 11 <= unhappiness <= 15:
            m = 'не сказать чтобы хорошо'
        else:
            m = 'ужасно'
        return m

    def talk(self):
        print('Меня зовут', self.name, ', и сейчас я чувствую себя', self.mood, '\n')
        self.__pass_time()

    def eat(self, food=4):
        eat_value = int(input('Сколько кусочков колбаски вы дадите своему питомцу? '))
        food += eat_value
        print('Мррр... Спасибо!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('Уиии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input('Как вы назовёте свою зверюшку? ')
    crit = Critter(crit_name)

    choice = None
    while choice != '0':
        print("""
        Меню игры
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        4 - Секретная кнопка
        """)
        choice = input('Ваш выбор: ')
        print()
        if choice == '0':
            print('До свидания.')
        elif choice == '1':
            crit.talk()
        elif choice == '2':
            crit.eat()
        elif choice == '3':
            crit.play()
        elif choice == '4':
            crit.__str__()
        else:
            print('Извините, в меню нет пункта', choice)


main()
input('\n\nНажмите Enter, чтобы выйти.')