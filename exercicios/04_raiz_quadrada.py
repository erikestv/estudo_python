# FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INTEIRO
# E CALCULE SUA RAIZ QUADRADA E EXIBA O RESULTADO.

numero = input ("Entre com um número inteiro para calcular a sua raiz quadrada: ")
numero = int (numero)

raiz = numero ** (1/2) # numero * 0.5
raiz = round (raiz, 4)

print("Raiz quadrada de", numero, "é:", raiz)
