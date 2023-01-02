import random

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", 
"g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["{", "}", "[", "]", "(", ")", "?", "/", ";", ":", ".", ">", "<", ",", "|", "\\"]

caracteres_senha = []
print('Bem-vindo!')
print('')
adicionar_letra = input('Por favor, informe se deseja que sua senha contenha letras. Digite "Sim" ou "Não":\n').lower()

while adicionar_letra != 'sim' and adicionar_letra != 'não':
    adicionar_letra = input('\nATENÇÃO: Você deve digitar "Sim" ou "Não" para concluir esta etapa.\nAgora, informe se sua senha deve contar letras:\n').lower

numero_letra = 0
if adicionar_letra == 'sim':
    print('\nVocê optou por adicionar letras a sua senha.')
    numero_letra = input('Por favor, informe a quantidade de letras que devem compor a sua senha:\n')
    check = numero_letra.isdigit()

    while check == False:
        numero_letra = input('ATENÇÃO: O valor digitado não é um número.\nPor favor, informe a quantidade de letras que deve compor a sua senha:\n')
        check = numero_letra.isdigit()

    numero_letra = int(numero_letra)

    for char in range(1, numero_letra + 1):
        caracteres_senha.append(random.choice(letras))
    print()
    print(f'Muito bem. Você escolheu uma senha contendo {numero_letra} letras.')
else:
    print('Você optou por não adicionar letras a sua senha.')

adicionar_numero = input('\nAgora, informe se sua senha deve conter números (Sim/Não):\n').lower()
while adicionar_numero != 'sim' and adicionar_numero != 'não':
    adicionar_numero = input('\nATENÇÃO: Você deve digitar "Sim" ou "Não" para concluir esta etapa.\nAgora, informe se sua senha deve conter números:\n').lower()

quantidade_numero = 0
if adicionar_numero == 'sim':
    print('\nVocê optou por adicionar números a sua senha.')
    quantidade_numero = input('Por favor, informe quantos números deverão compor sua senha:\n')
    check = quantidade_numero.isdigit()

    while check == False:
        quantidade_numero = input('ATENÇÃO: O valor digitado não é um número.\nPor favor, informe quantos números deverão compor sua senha:\n')
        check = quantidade_numero.isdigit()

    quantidade_numero = int(quantidade_numero)
    
    for char in range(1, quantidade_numero + 1):
        caracteres_senha += random.choice(numeros)
else:
    print('\nVocê optou por não adicionar números a sua senha.')



adicionar_simbolo = input('\nPor fim, informe se deseja que sua senha contenha símbolos (Sim/Não):\n').lower()
while adicionar_simbolo != 'sim' and adicionar_simbolo != 'não':
    adicionar_simbolo = input('\nATENÇÃO: Você deve digitar "Sim" ou "Não" para concluir esta etapa.\nAgora, informe se sua senha deve conter símbolos:\n').lower()

quantidade_simbolo = 0
if adicionar_simbolo == 'sim':
    print('\nVocê optou por adicionar símbolos a sua senha.')
    quantidade_simbolo = input('Por favor, informe quantos símbolos deverão compor a sua senha:\n')
    check = quantidade_simbolo.isdigit()

    while check == False:
        quantidade_simbolo = input('ATENÇÃO: O valor digitado não é um número.\nPor favor, informe quantos símbolos deverão compor sua senha:\n')
        check = quantidade_simbolo.isdigit()
    
    quantidade_simbolo = int(quantidade_simbolo)

    for char in range(1, quantidade_simbolo + 1):
        caracteres_senha += random.choice(simbolos)
else:
    print('\nVocê optou por não adicionar símbolos a sua senha.')

random.shuffle(caracteres_senha)
senha = ''.join(caracteres_senha)
print()
print(f'Sua senha é: {senha}')
print('Obrigado por utilizar este programa.\n')