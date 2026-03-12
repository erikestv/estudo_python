# Faça um programa que receba uma quantidade indefinida
#  de valores correspondentes a "saldo em conta", 
# mas quando o usuário apertar "enter" sem digitar 
# valor algum, o programa para de receber valores, e exibe 
# a soma de todos os valores digitados anteriormente.

#%%

saldo_total = 0 # variável que guarda a soma de todos os saldos

while True: # # cria um laço que repete para sempre
    saldo = input("Entre com o saldo: ") # pede para o usuário digitar um saldo

    if saldo == "": # se o usuário apertar ENTER sem digitar nada
        break # para o laço (sai do while)

    saldo_total += float(saldo) # transforma o saldo em número e soma ao saldo_total

print("saldo total: ", saldo_total) # mostra a soma final dos saldos