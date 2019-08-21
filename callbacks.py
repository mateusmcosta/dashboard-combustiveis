from dash.dependencies import Input, Output
from app import app
import plotly.graph_objs as go
from plotly import tools
import data_base as db

@app.callback(
    Output('graph-with-slider', 'figure'),
    [
        Input('tipo_selecao_regiao_ano', 'value'), 
        Input('ano_regiao_ano', 'value'), 
        Input('produtos_regiao_ano', 'values'), 
        Input('variável_regiao_ano', 'value'), 
        Input('regiao_regiao_ano', 'values')
    ])    
def update_figure_regioes(tipo_selecao, selected_year, produtos, variavel, regioes):
  df = retorna_valores_regiao(tipo_selecao, selected_year, variavel)
  nome_eixo_x = retonar_nome_eixo_x(tipo_selecao)
  
  fig = go.Figure()
 
  for produto in produtos:
      for regiao in regioes:
        filtered = df.loc[(df['PRODUTO'] == produto) & (df['REGIÃO'] == regiao)]
        titulo = '{} - Produto {}'.format(regiao, produto)
        fig.add_trace(go.Scatter(x= retorna_valores_eixo_x(tipo_selecao, df), y=filtered[variavel]['mean'],
                  mode='lines+markers',
                  name=titulo))


  fig.update_layout(title='{} por Região'.format(variavel),
              xaxis_title=nome_eixo_x,
              yaxis_title=variavel)                    

  return fig


@app.callback(
    Output('graph-with-slider-estado', 'figure'),
    [
        Input('tipo_selecao_estado_ano', 'value'), 
        Input('ano_estado_ano', 'value'), 
        Input('produtos_estado', 'values'), 
        Input('variável_estado', 'value'), 
        Input('estados', 'values')
    ])    
def update_figure_estados(tipo_selecao, selected_year, produtos, variavel, estados):
  df = retorna_valores_estado(tipo_selecao, selected_year, variavel)
  nome_eixo_x = retonar_nome_eixo_x(tipo_selecao)
  
  fig = go.Figure()
 
  for produto in produtos:
      for estado in estados:
        filtered = df.loc[(df['PRODUTO'] == produto) & (df['ESTADO'] == estado)]
        titulo = '{} - Produto {}'.format(estado, produto)
        fig.add_trace(go.Scatter(x= retorna_valores_eixo_x(tipo_selecao, df), y=filtered[variavel]['mean'],
                  mode='lines+markers',
                  name=titulo))


  fig.update_layout(title='{} por Estado'.format(variavel),
              xaxis_title=nome_eixo_x,
              yaxis_title=variavel)                    

  return fig


def retonar_nome_eixo_x(tipo_selecao):
  if(tipo_selecao == 1):
    return 'ANO'

  return 'Mês'

def retorna_valores_regiao(tipo_selecao, ano, variavel):
  if(tipo_selecao == 1):
    return db.dados_regioes_intervalo_ano_criterio(ano, variavel)

  return db.dados_regioes_ano_criterio(ano, variavel)

def retorna_valores_estado(tipo_selecao, ano, variavel):
  if(tipo_selecao == 1):
    return db.dados_estados_intervalo_ano_criterio(ano, variavel)

  return db.dados_estados_ano_criterio(ano, variavel)


def retorna_valores_eixo_x(tipo_selecao, df):
  if(tipo_selecao == 1):
    return df['ANO'].unique()

  return db.retorna_meses()
  
