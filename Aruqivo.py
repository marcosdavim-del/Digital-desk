def calcular_idade_em_2077(ano_nascimento):
    idade_em_2077 = 2077 - ano_nascimento
    return idade_em_2077

# Solicitar o ano de nascimento ao usuário
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# Calcular a idade em 2077
idade = calcular_idade_em_2077(ano_nascimento)

print(f"Sua idade em 2077 será: {idade} anos.")
