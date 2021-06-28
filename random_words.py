import random

words = ['Кот',
         'Мышь',
         'Крокодил',
         'Слон',
         'Жираф']

length = len(words)

listing = ''

while length != 0:
    rand = random.choice(words)
    listing += rand
    print(listing)
    listing = ''
    words.remove(rand)
    length = len(words)
