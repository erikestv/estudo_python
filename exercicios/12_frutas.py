# Escreva um programa que crie um dicionário com nomes de frutas
# como chaves e seus respectivos preços como valores.
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

#%%
fruta = input("Entre com o nome da fruta:")

frutas = {
    "Maçã": "R$1,50",
    "Pera": "R$1,25",
    "Goiaba": "R$2,15",
    "Banana": "R$2,75",
    "Laranja": "R$0,65",
    "Abacaxi": "R$3,20",
    "Uva": "R$1,90",
    "Limão": "R$1,25",
    "Jaca": "R$5,8",
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor valido!")
    
# JEITO DIFICIL

#fruta = input("Entre com o nome da fruta ")

# if fruta == "Maçã":
#   print("R$1,50")
# elif fruta == "Pera":
#   print("R$1,25")
# elif fruta == "Goiaba":
#   print("R$2,15")
# elif fruta == "Banana":
#   print("R$2,75")
# elif fruta == "Laranja":
#   print("R$0,65")
# elif fruta == "Abacaxi":
#   print("R$3,20")
# elif fruta == "Uva":
#   print("R$1,90")
# elif fruta == "Limão":
#   print("R$1,25")
# elif fruta == "Jaca":
#   print("R$5,80")

# else:
#   print("Entre com uma fruta valida")

