 # FAÇA UM PROGRAMA QUE VENDE UMA GARRAGA DE AGUA:
 # SE O CLIENTE ESCOLHER AGUA MINERAL MINERAL NATURAL, SERA COBRADO R$1,50
 # SE O CLIENTE ESCOLHER AGUA MINERAL MINERAL COM GÁS, SERA COBRADO R$1,50

#%%
texto = """
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
    print("Sua conra deu: R$1.50")

elif opcao == "2":
    print("Sua conta deu: R$2.50")

else:
    print("Entre com a opcao correta, por favor.")

# %%
texto = """
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 1.5
elif opcao == "2":
    conta = 2.5

if conta == 0:
    print("Enre com a opcao correta, por favor.")

else:
    print("Sua conta é: R$,", conta)
