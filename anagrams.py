import random

WORDS = ('ручка',
         'консоль',
         'ботаник',
         'средневековье',
         'астронавт',
         'колейдоскоп',
         'жимолость',
         'бактерия',
         'подставка',
         'корабль')

word = random.choice(WORDS)
correct = word
jumble = ''
score = 0

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
 '''
                      Добро пожаловать в игру 'Анаграммы'!
         Надо переставить буквы так, чтобы получилось осмысленное слово.
                    За правильный ответ, вы получите 10 очков.   
     У вас будет 0 очков на старте. За каждую подсказку с вас будут снимать по 1 баллу.
     UPDATE: В игре появились подсказки. В игре появилась система подсчёта очков.
 '''
)
print('Вот анаграмма:', jumble)

guess = input('\nПопробуйте отгадать исходное слово: ')
while guess != correct and guess != '':
    print('К сожалению, вы неправы.')
    prompt = input('Сейчас вам пологается подсказка, если хотите ей воспользоваться, то напишите слово "Да": ')

    if prompt == 'да' or prompt == 'Да':
        if correct == 'ручка':
            score -= 1
            print('Подсказка: она содержит пасту.')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'консоль':
            score -= 1
            print('Подсказка: это окно помогает программисту.')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'батаник':
            score -= 1
            print('Подсказка: те кто ходит в очках их так и называют.')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'средневековье':
            score -= 1
            print('Подсказка: замки, битвы, мечи, щиты...')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'астронавт':
            score -= 1
            print('Подсказка: аналог Юрия Гагарина.')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'колейдоскоп':
            score -= 1
            print('Подсказка: аналог подзорной трубы.')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'жимолость':
            score -= 1
            print('Подсказка: отвратительная синяя ягода живущая в тайге...')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'бактерия':
            score -= 1
            print('Подсказка: руки помыла Танюшка, а? а? а?')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'подставка':
            score -= 1
            print('Подсказка: Fast Charge.')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
        if correct == 'корабль':
            score -= 1
            print('Подсказка: The last sh...')
            guess = input('Попробуйте отгадать исходное слово ещё раз: ')
    else:
        guess = input('Хорошо, если вам не нужна подсказка то пробуйте отгадать исходное слово ещё раз: ')

if guess == correct:
    score += 10
    print('Да, именно так! Вы отгадали слово', '\'', guess, '\'', 'и заработали', score, 'из 10', 'очков.', '\n')

print('Спасибо за игру.')
