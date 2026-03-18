#%%

numero = 2 # guarda o número 2
print("2 x 1 = ", numero * 1 )  # imprime e multiplica 
print("2 x 2 = ", numero * 2 )  
print("2 x 3 = ", numero * 3 )  
print("2 x 4 = ", numero * 4 )
print("2 x 5 = ", numero * 5 )
print("2 x 6 = ", numero * 6 )
print("2 x 7 = ", numero * 7 )
print("2 x 8 = ", numero * 8 )
print("2 x 9 = ", numero * 9 )
print("2 x 10 = ", numero * 10 )

#%%
count = 1 # cria a variável count começando com valor 1
while count <= 10: # enquanto count for menor ou igual a 10, o laço continua
    print("entrei no laço!", count) # mostra a mensagem e o valor atual de count

# count e menor ou igual a 10 o programa continua repetindo

#%%
count = 1
while count <= 10:
    print("entrei no laço!", count)
    count = count + 1 # soma 1 ao valor atual de count, fazendo ele aumentar a cada repetição

# count = 1
# count = count + 1 → 2
# count = count + 1 → 3
# count = count + 1 → 4
# ...
# até chegar em 10
#%%
numero = 2 # variável que guarda o número da tabuada
count = 1  # variável usada como contador, começa em 1

while count <= 100: # enquanto count for menor ou igual a 100, o laço continua
    print(numero, "X", count, "=", numero * count) # mostra a multiplicação do número pela contagem atual
    count = count + 1 # aumenta o contador em 1 a cada repetição

print("Acabou!") # mensagem exibida quando o laço termina