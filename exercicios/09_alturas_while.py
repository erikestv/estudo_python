# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas

#%%
soma = 0 # valor final
qtde_entrada = 4 # o contador de entrada

while qtde_entrada > 0: # enquanto ainda houver entradas de altura para digitar
    altura = input("Entre com a altura: ") # pede para o usuário digitar uma altura
    altura = float(altura) # transforma o valor digitado em número decimal
    soma += altura# soma a altura na variável soma
    qtde_entrada -= 1 # diminui 1 da quantidade de entradas

print("Soma das alturas:", soma) # mostra a soma total das alturas

# > 0  → continua enquanto ainda tem números positivos
# 3 > 0  → continua
# 2 > 0  → continua
# 1 > 0  → continua
# 0 > 0  → falso → o laço para