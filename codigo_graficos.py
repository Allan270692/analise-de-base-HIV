import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('dados_aids_hiv_excel_1.xlsx')  #foi criado um arquivo excel com os dados que foram retirados do site do DATASUS sobre AIDS/


# LIMPEZA DE DADOS

df['DT_OBITO'] = df['DT_OBITO'].fillna('Vivo') # substitui os valores nulos da coluna pelo string 'vivo'
df.replace('Ignorado', np.nan, inplace=True) # substitui todos os valores 'Ignorado' por um valor nulo
df.dropna(inplace=True) # remove linhas com valores ausentes

# MUDANÇA DE FONTE GERAL 

plt.rcParams['font.family'] = 'serif'
plt.rcParams["font.serif"] = ["Times New Roman"]
plt.rcParams['font.size'] = 11.5

# GRÁFICO DE OCORRÊNCIA POR IDADE

plt.hist(df['NU_IDADE_N'], color='plum') #criamos um histograma e personalizamos
intervalo = list(range(10, 120, 10)) #intervalo
plt.title("Ocorrência por Idade") #atribui um título ao gráfico
plt.xlabel("Idade") #nomeia o eixo x
plt.xticks(intervalo) #eixo x terá os elementos descritos em intervalo
plt.ylabel("Número de Casos") #nomeia o eixo y

plt.tight_layout()
plt.savefig("distribuicao_idades.png") #gera um pdf da análise
plt.show() #exibe o gráfico

# GRÁFICO DE DISTRUIÇÃO POR RAÇA E SEXO

dataset = df.groupby(['CS_RACA', 'CS_SEXO']).size().unstack() # contando as combinações entre as colunas
raça = dataset.index # rótulos das linhas
num_Masculino = dataset['Masculino']
num_Feminino = dataset['Feminino']

x = np.arange(len(raça))

fig, ax = plt.subplots(figsize=(10,6)) # cria a figura e o eixo

# criação das barras

width = 0.4
p1 = ax.bar(x - width/2, num_Masculino, width, label='Masculino', color='steelblue')
p2 = ax.bar(x + width/2, num_Feminino, width, label='Feminino', color='plum')
ax.bar_label(p1, padding=3)
ax.bar_label(p2, padding=3)

# nomeando os demais elementos

ax.set_ylabel('Número de Casos')
ax.set_title('Distribuição dos Casos de HIV por Sexo e Raça')
ax.set_xticks(x)
ax.set_xticklabels(raça)
ax.legend() # adiciona a legenda

plt.tight_layout() # ajusta os parâmetros do gráfico
plt.savefig("raça_sexo.png")
plt.show()

# GRÁFICO DE ANO DO DIAGNÓSTICO

df['ano_DIAG'] = df['DT_DIAG'].dt.year
df['ano_DIAG'].value_counts().sort_index().plot(color="plum", marker='o', linestyle="--")
plt.title("Número de Casos ao Longo dos Anos") #atribui um título ao gráfico
plt.xlabel("Ano de Diagnóstico") #nomeia o eixo x
plt.ylabel("Número de Casos") #nomeia o eixo y

plt.tight_layout()
plt.savefig("ano_DIA.png")
plt.show()

# CASOS POR CRITÉRIO

fig, ax = plt.subplots(figsize=(8,6))

contagem = df['CRITERIO'].value_counts()
ax.barh(contagem.index, contagem, color="plum")

ax.set_xlabel('Número de Casos')
ax.set_ylabel('Critério')
ax.set_title('Distribuição dos Casos por Critério de Diagnóstico')

plt.tight_layout()
plt.savefig("casos_CRI.png")
plt.show()

# DIFERENÇA ENTRE DIAGNÓSTICO E OBITO

df_Obito = df[df['DT_OBITO'] != 'Vivo'].copy()

df_Obito['DT_OBITO'] = pd.to_datetime(df_Obito['DT_OBITO'], format='%Y-%m-%d')
df_Obito['DT_DIAG'] = pd.to_datetime(df_Obito['DT_DIAG'], format='%Y-%m-%d')
df_Obito['DT_OBITO'] = df_Obito['DT_OBITO'].dt.year
df_Obito['DT_DIAG'] = df_Obito['DT_DIAG'].dt.year

df_Obito['diferença'] = (df_Obito['DT_OBITO'] - df_Obito['DT_DIAG'])
df_Obito['diferença'].astype(int).value_counts().sort_index().plot(kind='bar', color="plum")
plt.title('Tempo, em Anos, entre Diagnóstico e Óbito')
plt.xlabel('Anos')
plt.ylabel('Número de casos')

plt.tight_layout()
plt.savefig("diferenca_DIA_OB.png")
plt.show()

# GRÁFICO DE ESCOLARIDADE
#A PARTIR DAQUI: renomeando para facilitação do entendimento do gráfico

df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('5ª a 8ª série incompleta do EF', 'E.F incompleto'))
df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('1ª a 4ª série incompleta do EF', 'E.F incompleto'))
df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('4ª série completa EF', 'E.F incompleto'))
df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('Não se aplica', 'E.F incompleto'))
df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('Educação superior incompleta', 'E.S incompleto'))
df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('Ensino médio incompleto', 'E.M incompleto'))
df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('Ensino fundamental completo', 'E.F completo'))
df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('Educação superior completa', 'E.S completo'))
df['CS_ESCOL_N'] = df['CS_ESCOL_N'].map(lambda x: str(x).replace('Ensino médio completo', 'E.M completo'))

#criando a figura

fig = plt.figure(figsize =(10, 6))  #tamanho da figura
explode = [0.1, 0, 0 , 0, 0, 0]    #destacando uma das fatias
#criando o gráfico
plt.pie(df['CS_ESCOL_N'].value_counts(),
         labels = df['CS_ESCOL_N'].unique(),
         autopct='%1.1f%%',
           explode=explode,
             shadow = True)

plt.title("Nível de escolaridade") 
plt.legend(df['CS_ESCOL_N'], title = "Escolaridade", loc = "upper left", bbox_to_anchor =(1.0, 1)) #criando a legenda do gráfico
plt.savefig("nivel_escolaridade.png") #gera um pdf da análise
plt.show() #exibe o gráfico

