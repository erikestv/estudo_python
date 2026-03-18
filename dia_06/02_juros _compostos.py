#%%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:

    # define uma função chamada "juros_compostos"
    # aporte: valor inicial (inteiro)
    # taxa: taxa de juros (decimal, ex: 0.05 para 5%)
    # anos: tempo em anos (inteiro)
    # -> float: indica que a função retorna um número com casas decimais

    """juros_composto serve para calcular o retorno financeiro a partir de um aporte.
Deve-se considerar o valor, a taxa de jutos atual e o tempo (em anos) para calculo do valor a ser retornado.

aporte:
    um numero inteiro, que presente o valor em R$

taxa:
    um numero float entre 0 e 1 que represente o valor de juros

anos:
    um numero inteiro >= 1 que representa o tempo que o investimento tera liquidez
"""
    # descrição da função: explica o que ela faz, parâmetros e retorno

    return aporte * (1 + taxa) ** anos

    # calcula e retorna o valor final com juros compostos

#%%
juros_compostos(taxa=0.13, anos=5, aporte=1000)

#%%