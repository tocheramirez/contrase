import random

options=('piedra','papel','tijera')
computer_wis=0
user_wis=0

rounds=1

while True:
    #bienbenida
    print('*' * 10)
    print('round', rounds)
    print('*' * 10)


    print('computer_wins', computer_wis)
    print('user_wins', user_wis)


    
    # selccion
    user_option = input( 'piedra, papel o tijera => ')
    user_option= user_option.lower()

    rounds+=1

    if not user_option in options:
        print('esa opcion no es valida')
        continue
    
    computer_option = random.choice(options)


    print('user option =>', user_option)
    print('computer option =>,',computer_option)
    #condiciones
    if user_option==computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option== 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wis+=1
        else:
            print('papel gana a tijera')
            print('computer gano!')
            computer_wis+=1
            
    elif user_option == 'papel':
        if computer_option== 'piedra':
            print('papel gana a piedra')
            print('user gano!')
            user_wis+=1
        else:
            print('tijera gana a papael')
            print('computer gano!')
            computer_wis+=1

    elif user_option == 'tijera':
        if computer_option== 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wis+=1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wis+=1
    
    if computer_wis == 2:
        print('El ganador es la computadora')
        break
    if user_wis == 2:
        print('El ganador es el usuario')
        break



    
