#%%
# Define o nome do arquivo que será aberto
arquivos = "data.csv"

# Abre o arquivo no modo leitura (padrão)
# O "with" garante que o arquivo será fechado automaticamente depois
with open(arquivos) as open_file:

# Lê todas as linhas do arquivo e armazena em uma lista
# Cada item da lista representa uma linha do arquivo
    lines = open_file.readlines()

# Percorre cada linha da lista
for l in lines:
    
# Imprime a linha na tela
# Obs: cada linha já vem com "\n", então pode pular uma linha extra
    print(l)

#%%

# Cria um dicionário vazio
# Ele vai armazenar os dados organizados por colunas
dados = dict()

# Pega a primeira linha do arquivo (geralmente o cabeçalho do CSV)
# strip("\n") remove a quebra de linha no final
# split(";") separa a linha em partes usando ";" como separador
# Resultado: uma lista com os nomes das colunas (chaves)
chaves = lines[0].strip("\n").split(";")

# Percorre cada nome de coluna (cada chave)
for c in chaves:

# Para cada chave, cria uma lista vazia dentro do dicionário
# Isso vai servir para armazenar os valores daquela coluna
    dados[c] = []

dados
#%%
# Percorre todas as linhas do arquivo, EXCETO a primeira
# lines[1:] significa "do índice 1 até o final"
# (pulamos o cabeçalho, que já usamos antes)
for l in lines[1:]:

# Remove a quebra de linha no final
# e separa os valores usando ";" como separador
# Resultado: uma lista com os dados da linha
    valores = l.strip("\n").split(";")

# Percorre os índices dos valores (0, 1, 2, ...)
    for i in range(len(valores)):

# Adiciona cada valor na lista correspondente dentro do dicionário
# chaves[i] pega o nome da coluna
# valores[i] pega o valor daquela coluna na linha atual
        dados[chaves[i]].append(valores[i])

# Exibe o dicionário final com os dados organizados por coluna
dados

#%%
# Cria uma lista vazia para armazenar as idades como números inteiros
idades = []

# Percorre a lista de idades que veio do dicionário (como strings)
for i in dados["idade"]:

# Converte cada idade de string para inteiro e adiciona na lista
    idades.append(int(i))

# Calcula a média:
# sum(idades) soma todos os valores
# len(idades) pega a quantidade de elementos
media = sum(idades)/ len(idades)

# Mostra o valor da média
media

#%%
nome = "erik estevam"
nome.split(" ")
