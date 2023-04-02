#Juego de Piedra, Papel o Tijera

import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

print('¡Bienvenido humano al Juego de Piedra, Papel o Tijera!')

while True:
    print('---' * 10)
    print('Round', rounds)
    print('---' * 10)

    print('Hasta ganado', user_wins, 'rondas.')
    print('La computadora ha ganado', computer_wins, 'rondas.')

    user_option = input('Elije una: ¿Piedra, Papel o Tijera?: ')
    user_option = user_option.lower()
    rounds += 1

    if not user_option in options:
        print('Porfavor escribe una opción valida.')
        continue

    computer_option = random.choice(options)

    print('Opción del Usuario => ', user_option)
    print('Opción de la Computadora => ', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('Le Ganaste a la Computadora!!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Gana la Computadora, sigue intentando!')
            computer_wins +=1 
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('Le Ganaste a la Computadora!!')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('Gana la Computadora, sigue intentando!')
            computer_wins +=1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('Le Ganaste a la Computadora!!')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('Gana la Computadora, sigue intentando!')
            computer_wins +=1
    if computer_wins == 2:
        print('---' * 10)
        print('El ganador es la computadora, mejor suerte a la proxima!')
        print('---' * 10)
        break
    if user_wins == 2:
        print('---' * 10)
        print('Eres el Ganador del Juego: ¡Felicidades!')
        print('---' * 10)
        break

    
