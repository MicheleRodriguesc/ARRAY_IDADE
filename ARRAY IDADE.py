# Declarando um array de números inteiros com anos de nascimento
anos_nascimento = [1980, 1995, 2002, 1975, 2010]

# Imprimindo o array de anos de nascimento
print("Anos de nascimento:")
print(anos_nascimento)

# Imprimindo a idade de cada pessoa em 2024
for ano in anos_nascimento:
    idade = 2024 - ano
    print(f"- {idade} anos (nascido em {ano})")
