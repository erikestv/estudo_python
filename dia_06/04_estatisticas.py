#%%

def soma(a:float, b:float, *args)->float:
    # junta todos os valores em uma lista
    valores = [a,b] + list(args) 

    return sum(valores) # soma todos os valores

def media(a:float, b:float, *args)->float:
    # calcula a média usando a função soma
     return soma(a, b, *args) / (len(args)+2)

# entrada de dados
a = float(input("Entre com valor de a: "))
b = float(input("Entre com valor de b: "))
c = float(input("Entre com valor de c: "))
d = float(input("Entre com valor de d: "))

# saídas
print("Media:", media(a,b,c,d))

