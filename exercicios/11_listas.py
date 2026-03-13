#%%

# Uma maneira de definir listas
idades = [22, 35, 22, 40, 50,25, 22]
print (idades)

#%%

erik = ["erik", "estevam", True, 22,]
print(erik)

#%%

# serve para ver o tipo de dado (texto, número, lista, etc.)
type(erik)

#%%

erik[3] # pega um elemento de uma lista 

#%%

idades = [22, 35, 22, 40, 50, 25, 21, 40]

print("soma de idade: ", sum(idades)) # sum() = soma tudo da lista

print("qtde idades: ", len(idades))   # len() = conta quantiade de elementos da lista

print("menor idade: ", min(idades))   # min() = descobri a menor idade da lista

print("maior idade: ", max(idades))   # min() = descobri a maior idade da lista

print("media idades: ", sum(idades)/len(idades))

# print("media idades: ", sum(idades)/9)
# pode gerar um bug porque nao acompnha a lista igual o len()
#%%

erik = ["erik estevam", 
        22, 
        True,
        ["repositor", "atendente", "analista"],
        [400, 1200, 1500],        
        ["caneta", "lapis", "borracha"]]

print("Tamanho de erik", len(erik))


print(erik[5][0]) 

material = erik[5]
primeiro_material = material[0]
print(primeiro_material)
#%%

tamanho = len(erik)
pos = tamanho -1 # última posição

material = erik[pos] # pega o último elemento

erik[pos][len(material)-1] # pega a última letra desse elemento

#%%

# FATIAMENTO

# seleciono o ultimo da lista A e o ultimo da lista B  
erik[-1][-1]

#%%

# primeiros 3 elementos da lista

erik[0:3] # fatiamento

# erik [start : stop ]

#%%

# pega a posição 3 da lista erik
# e seleciona do índice 1 até antes do 3
erik[3][1:3]

#%%

# pega a lista na posição 3 de erik
# e seleciona os 2 últimos elementos

erik[3][-2:]

#%%

salarios = erik[4]
salarios[::-1] # ordem inversa

## exemplo [start : stop : step]