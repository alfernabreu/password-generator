letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", 
"g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["{", "}", "[", "]", "(", ")", "?", "/", ";", ":", ".", ">", "<", ",", "|", "\\"]

print("Bem-vindo!")

num_caracteres = 0
num_caracteres = int(input("Por favor, informe o número de caracteres que deve compor a sua senha:\n"))
if num_caracteres < 8 or num_caracteres is str:
    num_caracteres = int(input("É recomendado que o número de caracteres seja um número inteiro igual ou maior que 8.\nPor favor, informe o número de caracteres que deve compor a sua senha:\n"))


adicionar_numeros = input("Agora, informe se sua senha deve conter números (Sim/Não):\n").lower
qnt_numero = 0
while adicionar_numeros != "sim" or adicionar_numeros != "não":
    adicionar_numeros = input('Você deve digitar "Sim" ou Não" para concluir esta etapa.\nAgora, informe se sua senha deve conter números:\n').lower
if adicionar_numeros == "sim":
    qnt_numero = int(input("Você optou por adicionar números a sua senha.\nInforme quantos números devem compor sua senha:\n"))

adicionar_simbolos = input("Por fim, informe se deseja que sua senha contenha simbos (Sim/Não:\n").lower