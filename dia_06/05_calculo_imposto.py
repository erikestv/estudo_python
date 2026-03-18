#%%
def calc_imposto(preco:float, tx_imposto_base:0.3, **kwargs):
    # **kwargs recebe vários argumentos nomeados extras
    # e transforma tudo em um dicionário
    
    imposto = preco * tx_imposto_base # calcula imposto base

    for i in kwargs:
        # i é a chave (nome do imposto, ex: "federal")
        # kwargs[i] é o valor (taxa, ex: 0.1)

        print(i, kwargs[i]) # mostra nome e valor

        imposto += preco * kwargs[i] # soma imposto extra

    return imposto
#%%
impostos_gerais = {
    "municipio":0.01,
    "estadual":0.005,
    "nacional":0.001
}

calc_imposto(100, 0.03, **impostos_gerais, internacional=0.00001)

# **impostos_gerais -> "desempacota" o dicionário
# ou seja, transforma em argumentos nomeados

# é como se fosse chamado assim:
# calc_imposto(
#     100,
#     0.03,
#     municipio=0.01,
#     estadual=0.005,
#     nacional=0.001,
#     internacional=0.00001
# )
