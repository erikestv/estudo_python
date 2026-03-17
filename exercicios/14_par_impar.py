# Faça um programa que receba um número.
# Verifique se o numero informado e par ou impar.
# Exiba o resultado da seguinte maneira:

# O nuemro x é impar
# ou
# O numero x é par

#%%
def par_impar(numero:int):
    # função que verifica se um número é par ou ímpar

    if numero % 2 == 0: # verifica se o resto da divisão por 2 é 0
        return "par" # se for, é par
     
    else:
        return "impar" # senão, é ímpar



numero = input("Entre com um numero: ") # recebe como texto
numero = int(numero) # converte para inteiro

# chamada da função
resultado = par_impar(numero)

# saída
print("O valor", numero, "é", resultado) # mostra o resultado