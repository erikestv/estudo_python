#%%
nome = "Erik Estevam"

for letra in nome: # percorre o texto da variável nome, pegando uma letra por vez
    print(letra)

#%%

numero = 2
max_numero = 100

for i in range(1, max_numero+1):# repete o laço começando em 1 até o valor de max_numero
    print(numero, "x", i, "=", numero * i)

# for → significa “para cada” (cria um laço de repetição)
# i → é uma variável do loop (recebe os números da repetição)
# in → significa “em / dentro de”
# range → significa “intervalo de números”

#%%

# Quais numeros são divisiveis por 4 
# no intervalo [4 - 100] ?

for numero in range(4, 101):  # percorre os números de 4 até 100
    if numero % 4 ==0: # verifica se o número é divisível por 4
        print(numero)  # mostra o número na tela

#%%
# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas

soma = 0         # valor final
qtde_entrada = 4 # o contador de entrada

for i in range (qtde_entrada): # repete o código a quantidade de vezes informada em qtde_entrada
    altura = input("Entre com a altura: ") # pede para o usuário digitar uma altura
    altura = float(altura) # transforma o valor digitado em número decimal
    soma += altura # soma a altura digitada na variável soma

print("Soma das alturas:", soma) # mostra a soma total das alturas

