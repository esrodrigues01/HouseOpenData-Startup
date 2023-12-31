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

#Respodendo a pergunta 3

contagem_por_estado = dados.groupby('State')['Count'].count()
estados = [dados['State']]
contagem_por_estado.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Estado')
plt.ylabel('Número de Acidentes Fatais')
plt.title('Distribuição de Acidentes Rodoviários Fatais por Estado na Austrália')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()
#print(contagem_por_estado)


#Respodendo a pergunta 4
#Criar uma função para determinar a faixa etária de cada cidadão

def categorizar_faixa_etaria(idade):
    if idade <= 25:
        return 'Jovem'
    elif 26 <= idade <= 60:
        return 'Adulto'
    else:
        return 'Idoso'


dados['Faixa_etaria'] = dados['Age'].apply(categorizar_faixa_etaria)
contagem_por_faixa_etaria = dados['Faixa_etaria'].value_counts()
contagem_por_faixa_etaria.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Faixa Etária')
plt.ylabel('Número de Acidentes Fatais')
plt.title('Distribuição de Acidentes Rodoviários Fatais por Faixa Etária na Austrália')
plt.xticks(rotation=0)  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()


#Respodendo a pergunta 5
contagem_por_periodo = dados['Time of day'].value_counts()
contagem_por_periodo.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Perido')
plt.ylabel('Número de Acidentes Fatais')
plt.title('Distribuição de Acidentes Rodoviários Fatais por Período na Austrália')
plt.xticks(rotation=0)  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

#Respodendo a pergunta 6
total_acidentes = dados['Count'].count()
qtd_anos = 32
media = total_acidentes/qtd_anos
print('Média de Acidentes Rodoviários Fatais por ano na Austrália: ', media)


#Respodendo a pergunta 7
contagem_por_genero = dados.groupby('Gender')['Count'].count()
contagem_por_genero.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Gênero')
plt.ylabel('Acidentes')
plt.title('Quantidade de Acidentes Rodoviários Fatais por Gênero e na Austrália')
plt.xticks(rotation=0)  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

#Respodendo a pergunta 8
contagem_por_genero = dados.groupby('Road User')['Count'].count()
contagem_por_genero.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Tipo de Veículo')
plt.ylabel('Acidentes')
plt.title('Tipos de Veículo que se envolve em acidentes Rodoviários Fatais na Austrália')
plt.xticks(rotation=0)  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

#Respodendo a pergunta 9 

soma_idade = dados['Age'].sum()
qtd_pessoas = dados['Age'].count()
mediaIdade = soma_idade/qtd_pessoas
print("A Média de Idade é: ", mediaIdade)


#Respodendo a pergunta 10
somaFeriado_natal_SIM = (dados['Christmas Period'] == 'Yes').sum()
somaFeriado_pascoa_SIM = (dados['Easter Period'] == 'Yes').sum()
totais = dados['Christmas Period'].count()
porcentagemAcidentesNatal = ((somaFeriado_natal_SIM * 100) / totais)
porcentagemAcidentesPascoa = ((somaFeriado_pascoa_SIM * 100) / totais)
print("Total de acidentes no período de Natal: ", porcentagemAcidentesNatal, "%")
print("Total de acidentes no período de Páscoa: ", porcentagemAcidentesPascoa, "%")

#pergunta extra qual dia da semana tem mais acidente por ano #Melhorar
contagem_acidentes = dados.groupby(['Year', 'Dayweek'])['Crash ID'].count().reset_index()
dia_mais_acidentes = contagem_acidentes.groupby('Year')['Crash ID'].idxmax()
dia_mais_acidentes = contagem_acidentes.loc[dia_mais_acidentes]['Dayweek']
plt.figure(figsize=(12, 6))
for ano in contagem_acidentes['Year'].unique():
    dados_ano = contagem_acidentes[contagem_acidentes['Year'] == ano]
    plt.bar(dados_ano['Year'], dados_ano['Dayweek'], label=f'Year {ano}')

plt.xlabel('Ano')
plt.ylabel('Dia da Semana')
plt.title('Dia da Semana com Mais Acidentes por Ano')
plt.legend()
plt.xticks(rotation=45)
plt.show()



