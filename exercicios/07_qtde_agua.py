## ALTERE O PROGRAMA ANTERIOR PARA CONSIDERA R A QUANTIDADE DE AGUA

# %%
texto = "Digite 1 para Água natural ou 2 para Água com gás: "

opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Entre com a opcao correta, por favor.")

else:
    qtde = input("Quantas garrafas? ")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("Sua conta deu: R$", valor_total)