# %%

idade = 80

if idade >= 70:  # TESTA A PRIMEIRA CONDIÇÃO
    print("Cuidado com a bebida.")
    print("Consulte o médico!")

# ELIF PODE TER QUANTOS QUISER

elif idade >= 18:  # TESTA OUTRA CONDIÇÃO SE O IF FOR FALSO
    print("Você pode beber cerveja!")
    print("Beba com moderação.")

elif idade == 17:  # TESTA OUTRA CONDIÇÃO SE O IF FOR FALSO
    print("Você ainda não pode beber cerveja!")
    print("Fique no refri!")

else:  # EXECUTA SE NENHUMA CONDIÇÃO ANTERIOR FOR VERDADEIRA
    print("Você não pode beber cerveja!")
    print("Vá pra casa beber leite!")