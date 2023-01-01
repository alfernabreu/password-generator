import random

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", 
"g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["{", "}", "[", "]", "(", ")", "?", "/", ";", ":", ".", ">", "<", ",", "|", "\\"]



print('Bem-vindo!')
numero_caracteres = (input('Por favor, informe a quantidade de caracteres (entre 8 e 32) que deve compor a sua senha:\n'))

# verificar se o input é formado apenas por números.
check = numero_caracteres.isdigit()

while check == False:
    numero_caracteres = input('ATENÇÃO: O valor digitado não é um número.\nPor favor, informe a quantidade de caracteres(entre 8 e 32) que deve compor a sua senha:\n')
    check = numero_caracteres.isdigit()

numero_caracteres = int(numero_caracteres)
while numero_caracteres < 8 or numero_caracteres > 32:
        if numero_caracteres < 8:
            print('ATENÇÃO: Você digitou uma quantidade menor do que a recomendada.')
            numero_caracteres = int((input('Por favor, informe a quantidade de caracteres (entre 8 e 32) que deve compor a sua senha:\n')))
        elif numero_caracteres > 32:
            print('ATENÇÃO: Você digitou uma quantidade maior que a recomendada.')
            numero_caracteres = int((input('Por favor, informe a quantidade de caracteres (entre 8 e 32) que deve compor a sua senha:\n')))
print()
print(f'Muito bem. Você escolheu uma senha contendo {numero_caracteres} caracteres.')



adicionar_numeros = input('\nAgora, informe se sua senha deve conter números (Sim/Não):\n').lower()
while adicionar_numeros != 'sim' and adicionar_numeros != 'não':
    adicionar_numeros = input('\nATENÇÃO: Você deve digitar "Sim" ou "Não" para concluir esta etapa.\nAgora, informe se sua senha deve conter números:\n').lower()

quantidade_numeros = 0
if adicionar_numeros == 'sim':
    print('\nVocê optou por adicionar números a sua senha.')
    quantidade_numeros = input('Por favor, digite quantos números deverão compor sua senha:\n')

    check = quantidade_numeros.isdigit()

    while check == False:
        quantidade_numeros = input('ATENÇÃO: O valor digitado não é um número.\nPor favor, informe quantos números deverão compor sua senha:\n')
        check = quantidade_numeros.isdigit()

    quantidade_numeros = int(quantidade_numeros)
    while quantidade_numeros > numero_caracteres:
        print(f'Você optou por uma quantidade de números superior à quantidade de caracteres da senha ({numero_caracteres} foi o número de caracteres escolhido.).')
        quantidade_numeros = input('Por favor, digite quantos números deverão compor sua senha:\n')
        
        check = quantidade_numeros.isdigit()

        while check == False:
            quantidade_numeros = input('ATENÇÃO: O valor digitado não é um número.\nPor favor, informe quantos números deverão compor sua senha:\n')
            check = quantidade_numeros.isdigit()
            
    quantidade_numeros = int(quantidade_numeros)

    if quantidade_numeros == numero_caracteres:
        print(f'Você optou por uma quantidade de números igual à quantidade de caracteres da senha ({numero_caracteres} foi o número de caracteres escolhido.)')
        apenas_numero = input('Você deseja criar uma senha sem a presença de números? (Sim/Não):\n').lower()
        while apenas_numero != 'sim' and apenas_numero != 'não':
            print('ATENÇÃO: Você deve digitar "Sim" ou "Não" para concluir esta etapa.')
            apenas_numero = input('Por favor, digite "Sim" se desejar que sua senha seja formada sem letras ou "Não" caso opte pela presença de letras:\n')
        if apenas_numero == 'sim':
            numero_caracteres = quantidade_numeros
        else:
            quantidade_numeros = input('Por favor, digite quantos números deverão compor sua senha:\n')
            check = quantidade_numeros.isdigit()

            while check == False:
                quantidade_numeros = input('ATENÇÃO: O valor digitado não é um número.\nPor favor, informe a quantos números deverão compor sua senha:\n')
                check = quantidade_numeros.isdigit()

            quantidade_numeros = int(quantidade_numeros)
            numero_caracteres = numero_caracteres - quantidade_numeros
else:
    print('\nVocê optou por não adicionar números a sua senha.')

adicionar_simbolos = input('\nPor fim, informe se deseja que sua senha contenha símbolos (Sim/Não):\n').lower()
while adicionar_simbolos != 'sim' and adicionar_simbolos != 'não':
    adicionar_simbolos = input('\nATENÇÃO: Você deve digitar "Sim" ou "Não" para concluir esta etapa.\nAgora, informe se sua senha deve conter símbolos:\n').lower()

quantidade_simbolos = 0
if adicionar_simbolos == 'sim':
    print('\nVocê optou por adicionar símbolos a sua senha.')
    quantidade_simbolos = int(input('Por favor, informe quantos símbolos deverão compor a sua senha:\n'))

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
for i in range (numero_caracteres):
    senha_final.append(random.choice(caracteres_senha))

senha = ''.join(senha_final)
print()
print(f'Sua senha é: {senha}')
print('Obrigado por utilizar este programa.\n')