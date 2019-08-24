import pandas as pd

data_base = pd.read_csv('data/2004-2019.tsv',delimiter='\t',encoding='utf-8')
data_base = data_base.drop(['Unnamed: 0'], axis=1)

#Funções
def dados_regioes_intervalo_ano_criterio(ano, variavel):
    return data_base[data_base['ANO'] <= ano].groupby(['ANO', 'REGIÃO', 'PRODUTO'],as_index=False).agg({variavel:['mean']})

def dados_regioes_ano_criterio(ano, variavel):
    return data_base[data_base['ANO'] == ano].groupby(['ANO', 'MÊS', 'REGIÃO', 'PRODUTO'],as_index=False).agg({variavel:['mean']})

def dados_estados_intervalo_ano_criterio(ano, variavel):
    return data_base[data_base['ANO'] <= ano].groupby(['ANO', 'ESTADO', 'PRODUTO'],as_index=False).agg({variavel:['mean']})

def dados_estados_ano_criterio(ano, variavel):
    return data_base[data_base['ANO'] == ano].groupby(['ANO', 'MÊS', 'ESTADO', 'PRODUTO'],as_index=False).agg({variavel:['mean']})

def dados_pais_intervalo_ano_criterio(ano, variavel):
    return data_base[data_base['ANO'] <= ano].groupby(['ANO', 'PRODUTO'],as_index=False).agg({variavel:['mean']})

def dados_pais_ano_criterio(ano, variavel):
    return data_base[data_base['ANO'] == ano].groupby(['ANO', 'PRODUTO'],as_index=False).agg({variavel:['mean']})

def estados():
    estados = data_base['ESTADO'].unique()
    estados.sort()
    return estados   

def anos():
    return data_base['ANO'].unique()

def ano_min():
    return data_base['ANO'].min()

def ano_max():
    return data_base['ANO'].max()

def produtos():
    return data_base['PRODUTO'].unique()

def regioes():
    return data_base['REGIÃO'].unique()    

def filtra_produto(data_set, produto):
    return data_set[data_set['PRODUTO'] == produto]

def retornar_valores_coluna(df, coluna):
    return df[coluna]

def retorna_variaveis():
    return ['PREÇO MÉDIO REVENDA', 'DESVIO PADRÃO REVENDA', 'PREÇO MÍNIMO REVENDA', 'PREÇO MÁXIMO REVENDA', 'COEF DE VARIAÇÃO REVENDA']

def retorna_meses():
    return ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
