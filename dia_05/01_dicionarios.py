#%%

lista = [2, 123, "erik", ["da", "de", "di",], True]

lista[2] # Mostra o segundo elemento da lista começando de 0
#%%

# pares de chave/valor

dados_erik = {
        "nome":"erik",
        "filhos":True,
        "sobrenome":"estevam",
        "formacao":["sistemas", "dados"],
        "cargos":[
                {"nome": "repositor", "empresa": "havan"},
                {"nome": "atendente_01", "empresa": "drogasil"},
                {"nome": "atendente_02", "empresa": "drogasil"},                
                {"nome": "crm", "empresa": "est.ar"},                
        ]
}


print(dados_erik) # Imprime todo o dicionário
print(dados_erik["formacao"][-1]) # Acessa a lista "formacao" e mostra o último elemento
print(dados_erik["cargos"][-1]["empresa"]) # Acessa a lista "cargos", pega o último cargo e mostra a empresa

#%%
dados_erik["estado civil"] = "casado" # adiciona a chave "estado civil" no dicionário e define o valor como "casado"

#%%

print("Chaves:", dados_erik.keys())
print("Valores:", dados_erik.values())
print("Items:", dados_erik.items())

#%%

for i in [10,20,45,28,"erik"]:
        print(i)

#%%

for i in dados_erik:
        print(i, "=>",dados_erik[i])


#%%

for chaves, valor in dados_erik.items():
        print(chaves,"=>", valor)

#%%

dados_erik["estado civil"] = "solteiro"
dados_erik
