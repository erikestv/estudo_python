#%%
numero_secreto = 7

palpite = int(input("Escolha um numero de 1 a 10: "))

if palpite < numero_secreto:
    print("Muito baixo!")

elif palpite > numero_secreto:
    print("Muito alto!")

else:
    print("Acertou o numero!!")

#%% 
numero = input("digite um numero: ")
print("Seu numero e", numero)

## COM INPUT A PESSOA PODE DIGITAR QUALQUER COISA

#%%
numero = int(input("Digite um numero: "))
print("Seu numero e: ",numero)

# input() → pega texto
# int() → transforma em número
# números → podem somar, subtrair, multiplicar, dividir
#%%
## outro exemplo

numero = input("Entre com um número inteiro para calcular o dobro: ")
numero = int(numero)
dobro = numero * 2
print("O dobro de", numero, "é:", dobro)

# int transforma o texto digitado em número
# depois o programa calcula o dobro