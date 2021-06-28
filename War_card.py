import random


class Card:
    """Карты игры 'Война'"""
    CARDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    SUIT = "C"


class People:
    cards = []
    cards2 = []

    def __init__(self, name):
        self.name = name

    def to_pull(self):
        """Тянуть карту"""
        mix_card = random.choice(Card.CARDS)
        suit = Card.SUIT
        People.cards.append(mix_card + suit)
        People.cards2.append([self.name, mix_card + suit])


class Win:
    save_cards = []

    def selection_of_the_winner(self):
        res = max(Win.save_cards)
        for i in People.cards2:
            if res in i:
                print('Победил', i[0])


reop1 = People('Игорь')
reop1.to_pull()
print(reop1.name, 'тянет карту и ему выпадает:', " ".join(reop1.cards))
win = Win()
win.save_cards.append(" ".join(People.cards))
reop1.cards.clear()

reop2 = People('Вася')
reop2.to_pull()
print(reop2.name, 'тянет карту и ему выпадает:', " ".join(reop2.cards))
win.save_cards.append(" ".join(People.cards))
del reop2.cards[0]

reop3 = People('Гена')
reop3.to_pull()
print(reop3.name, 'тянет карту и ему выпадает:', " ".join(reop3.cards))
win.save_cards.append(" ".join(People.cards))
del reop3.cards[0]

win.selection_of_the_winner()