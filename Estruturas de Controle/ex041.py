#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date

ano = int(input("Qual ano você nasceu? "))
idade = date.today().year - ano
print(f'Você tem {idade} anos, LOGO...')
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria será JÚNIOR.')
elif idade <= 25:
    print('Sua categoria será SÊNIOR.')
else:
    print('Sua categoria será MASTER.')


