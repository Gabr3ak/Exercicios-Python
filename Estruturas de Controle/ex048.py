#Faça um programa que calcule a soma entre todos os números que são múltiplos de três
#e que se encontram no intervalo de 1 até 500.

soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
print(f'A soma de todos os números múltiplos de 3 é {soma}')
