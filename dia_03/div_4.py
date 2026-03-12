# %%

# Quais numeros são divisiveis por 4 
# no intervalo [4 - 100] ?

count = 4 # variável usada como contador, começa em 4
while count <= 100: # enquanto count for menor ou igual a 100, o laço continua
    resto = count % 4 # calcula o resto da divisão de count por 4
   
    if resto == 0: # se o resto for 0, significa que o número é divisível por 4
        print(count) # mostra o número
    
    count += 1 # aumenta o contador em 1