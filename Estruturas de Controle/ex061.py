#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razão
    contador = contador + 1
print('Acabou')

