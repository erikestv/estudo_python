#%%
idades = [] # Lista vazia

while True: # Laço pedindo input do usuario
    idade = input("Entre com a idade: ")

    if idade == "": # Se o usuário não digitar nada, o laço será interrompido
        break

    idades.append(int(idade)) # Se colocar a idade será convertida a inteiro e depois adicionada a lista

#estatistica
media = sum(idades) / len(idades)     
minimo = min(idades)      
maximo = max(idades)      
qtde = len(idades)    

# imprimir na tela
print(idades)
print("MEDIA", media)
print("MINIMO", minimo)
print("MAXIMO", maximo)
print("QTDE", qtde)