#%%

dados_erik= [22, 1, "casado", "analista", "python"]
dados_erik

#%%

dados_erik.append("1350")
dados_erik

#%%

# declara tupla

# tupla_erik= 22, 1, "casado", "analista", "python"
tupla_erik = (22, 1, "casado", "analista", "python", ["celular","notbook"])

print(type(tupla_erik))
print(tupla_erik)

#%%

tupla_erik[0] = 28

# tupla e uma lista que não podem ser alterada
# a lista nao mutavel
# mas se tiver um elemento exemplo a lista pode alterar
#%%

tupla_erik[-1].append("pc")

# a lista e mutavel
#%%

tupla_erik