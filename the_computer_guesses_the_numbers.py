from random import randint

print('Загадайте любое число компьютеру от 1 до 100.')

user = int(input('Загадайте число компьютеру: '))

number = randint(0, 100) # комп отгадывает число
attempt = 1

while number != user:
    if number < user:
        print('Хм... Пробую число побольше...')
        number += 1
        attempt += 1
    else:
        print('Хм... Пробую число поменьше...')
        number -= 1
        attempt += 1
print('Пфф... Изи ваще, это число', user)
print('Мне всего лишь то понадобилось', attempt, 'попыток, чтобы угадать!')
