#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 100 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} NÃO é bissexto.')


