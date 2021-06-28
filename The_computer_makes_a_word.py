import random

WORDS = ('логопед',
         'князь',
         'задира',
         'многоножка',
         'человек',
         'салфетка',
         'август',
         'гений',
         'татьяна',
         'моряк')

attempts = 0

word = random.choice(WORDS)
word_len = len(word)

print('В загаданном слове', word_len, 'букв.')
print('У тебя есть 5 поптыток чтобы угадать загаданное слово.')

while attempts != 10:
    letter = input('Назови букву: ')

    if letter not in word:
        print('К сожалению в загаданном слове нет буквы', letter.upper())
    if letter in word:
        print('Да, буква', letter.upper(), 'есть в слове.')

    print('Ты хочешь назвать слово полностью?')
    yes_no = input('Введи да - если хочешь ввести слово или нет - если хочешь продолжить угадывать буквы: ')

    if yes_no == 'Да' or yes_no == 'да':
        word_answer = input('\nВведите слово:')
        if word_answer == word:
            print('\nПоздравляем, вы угадали слово', word.upper())
            exit()
        else:
            print('\nУвы, вы не угадали слово. На этом игра для вас закончена. ЛУЗЕР!')
            exit()

    if yes_no == 'Нет' or yes_no == 'нет':
        attempts += 1
        continue

word_answer = input('Ты исчерпал лимит попыток, говори слово: ')
if word_answer == word:
    print('\nПоздравляем, вы угадали слово', word.upper())
    exit()
else:
    print('\nУвы, вы не угадали слово. На этом игра для вас закончена. ЛУЗЕР!')
    exit()