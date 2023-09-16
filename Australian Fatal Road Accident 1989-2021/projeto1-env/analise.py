import pandas as pd 
import matplotlib.pyplot as plt

#Buscando Dataset com os dados em csv
dataset_csv = '.\dataset\Crash_Data.csv'


#lendo os dados do arquivo csv
dados = pd.read_csv(dataset_csv)

#Manipulando o dataframe para insrir a quantidade de acidentes por ano 
#contando quantos acidadentes teve em cada ano
contagem_anos = dados['Year'].value_counts()

df_contagem = pd.DataFrame({'Year': contagem_anos.index, 'Count': contagem_anos.values})

#fazendo o merge dos dataset atualizado
dados = pd.merge(dados, df_contagem, on='Year', how='left')
#salvando
dados.to_csv('.\dataset\crash_Data_contagem.csv', index=False)


#Respondendo a pergunta 1 
plt.figure(figsize=(10, 10))  # Ajuste o tamanho da figura conforme necessário
plt.plot(dados['Year'], dados["Count"], marker='o', linestyle='-')
plt.title('Tendência de Acidentes Rodoviários Fatais na Austrália (1989-2021)')
plt.xlabel('Ano')
plt.ylabel('Acidentes')
plt.grid(True)
plt.show()

#Respondendo a pergunta 2
contagem_anos = dados.groupby('Year')['Count'].count()
ano_maior_numero_acidentes = contagem_anos.idxmax()
maior_numero_acidentes = contagem_anos.max()
# Encontre o ano com o menor número de acidentes fatais
ano_menor_numero_acidentes = contagem_anos.idxmin()
menor_numero_acidentes = contagem_anos.min()

anos = [ano_maior_numero_acidentes, ano_menor_numero_acidentes]
contagens = [maior_numero_acidentes, menor_numero_acidentes]

plt.bar(anos, contagens, color=['red', 'blue'])
plt.xlabel('Ano')
plt.ylabel('Número de Acidentes Fatais')
plt.title('Anos com Maior e Menor Número de Acidentes Fatais')
plt.xticks(anos)
plt.show()
