# Escreva um programa que receba uma lista de números
# do usuário e conte quantas vezes um número
# específico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.

#%%

lista = [1,2,9,4,5,1,2,3,9,8,2,1,5,2,6,1] # lista de números

numero = input("Entre com um número: ") # pede um número ao usuário
numero = int(numero)  # converte o valor para inteiro

contador = 0 # inicia o contador
for i in lista: # percorre cada número da lista
    if i == numero: # verifica se é igual ao número digitado
        contador += 1  # soma 1 ao contador

# mostra quantas vezes o número aparece
print("Quantidade de", numero, ":", contador)