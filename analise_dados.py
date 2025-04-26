import pandas as pd

# Ler o arquivo Excel
df = pd.read_excel('data/dados-test.xlsx', header=None)

# Criar um DataFrame com as bolas
bolas = []
for index, row in df.iterrows():
    for bola in row:
        bolas.append(bola)

# Contar a frequência de cada bola
frequencia = pd.Series(bolas).value_counts().reset_index()
frequencia.columns = ['Numero', 'Frequencia']

# Imprimir as bolas e suas frequências
print(f"{'Numero':^6} | {'Frequencia':^9}")
print("-" * 18)
for index, row in frequencia.head(15).iterrows():
    print(f"{row['Numero']:^6} | {row['Frequencia']:^9}")

print("\nOs 15 números que mais se repetem:\n")
numeros = [str(row['Numero']) for index, row in frequencia.head(15).iterrows()]
print(' '.join(numeros))