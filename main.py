import random

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", 
"g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["{", "}", "[", "]", "(", ")", "?", "/", ";", ":", ".", ">", "<", ",", "|", "\\"]

print('Bem-vindo!')
num_caracteres = (input('Por favor, informe o número de caracteres (entre 8 e 32) que deve compor a sua senha:\n'))
check = num_caracteres.isdigit()

while check == False:
    num_caracteres = input('Isso não é um número.\nPor favor, informe o número de caracteres(entre 8 e 32) que deve compor a sua senha:\n')
    check = num_caracteres.isdigit()

num_caracteres = int(num_caracteres)
while num_caracteres < 8 or num_caracteres > 32:
        if num_caracteres < 8:
            print('Você digitou um número menor do que o recomendado.')
            num_caracteres = int((input('Por favor, informe o número de caracteres (entre 8 e 32) que deve compor a sua senha:\n')))
        elif num_caracteres > 32:
            print('Você digitou um número maior que o recomendado.')
            num_caracteres = int((input('Por favor, informe o número de caracteres (entre 8 e 32) que deve compor a sua senha:\n')))

print()
print(f'Muito bem. Você escolheu uma senha contendo {num_caracteres} caracteres.')

adicionar_numeros = input('\nAgora, informe se sua senha deve conter números (Sim/Não):\n').lower()

while adicionar_numeros != 'sim' and adicionar_numeros != 'não':
    adicionar_numeros = input('Você deve digitar "Sim" ou "Não" para concluir esta etapa.\nAgora, informe se sua senha deve conter números:\n').lower()

if adicionar_numeros == 'sim':
    print('Você optou por adicionar números a sua senha.')
else:
    print('Você optou por não adicionar números a sua senha.')

adicionar_simbolos = input('\nPor fim, informe se deseja que sua senha contenha símbolos (Sim/Não):\n').lower()
while adicionar_simbolos != 'sim' and adicionar_simbolos != 'não':
    adicionar_simbolos = input('Você deve digitar "Sim" ou "Não" para concluir esta etapa.\nAgora, informe se sua senha deve conter símbolos:\n').lower()

if adicionar_simbolos == 'sim':
    print('\nVocê optou por adicionar símbolos a sua senha.')
else:
    print('\nVocê optou por não adicionar símbolos a sua senha.')

if adicionar_numeros == 'sim' and adicionar_simbolos == 'não':
    caracteres_senha = letras + numeros
elif adicionar_numeros == 'sim' and adicionar_simbolos == 'sim':
    caracteres_senha = letras + numeros + simbolos
elif adicionar_numeros == 'não' and adicionar_simbolos == 'sim':
    caracteres_senha = letras + simbolos
else:
    caracteres_senha = letras

senha_final = []
for i in range (num_caracteres):
    senha_final.append(random.choice(caracteres_senha))

senha = ''.join(senha_final)
print()
print(f'Sua senha é: {senha}')