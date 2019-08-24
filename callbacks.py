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
def desenha_grafico_regioes(tipo_selecao, selected_year, produtos, variavel, regioes):
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


  fig.update_layout(title='{} POR REGIÃO'.format(variavel),
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
def desenha_grafico_estados(tipo_selecao, selected_year, produtos, variavel, estados):
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


  fig.update_layout(title='{} POR ESTADO'.format(variavel),
              xaxis_title=nome_eixo_x,
              yaxis_title=variavel)                    

  return fig

def retonar_nome_eixo_x(tipo_selecao):
  if(tipo_selecao == 1):
    return 'ANO'

  return 'MÊS'

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

@app.callback(
    Output('graph-estabelecimentos-pesquisados', 'figure'),
    [
        Input('tipo_selecao_regiao_ano', 'value'), 
        Input('ano_regiao_ano', 'value'), 
        Input('produtos_regiao_ano', 'values'), 
        Input('regiao_regiao_ano', 'values')
    ])
def desenha_grafico_postos_regiao(tipo_selecao, selected_year, produtos, regioes):
  return desenha_grafico_nro_postos(tipo_selecao, selected_year, produtos, regioes, 'REGIÃO')

@app.callback(
    Output('graph-estabelecimentos-pesquisados-estados', 'figure'),
    [
        Input('tipo_selecao_estado_ano', 'value'), 
        Input('ano_estado_ano', 'value'), 
        Input('produtos_estado', 'values'),
        Input('estados', 'values')
    ])
def desenha_grafico_postos_estados(tipo_selecao, selected_year, produtos, estados):
  return desenha_grafico_nro_postos(tipo_selecao, selected_year, produtos, estados, 'ESTADO')

def desenha_grafico_nro_postos(tipo_selecao, selected_year, produtos, linhas, agrupamento):
  variavel = 'NÚMERO DE POSTOS PESQUISADOS'
  df = retorna_postos_df(agrupamento ,tipo_selecao, selected_year, variavel)
  nome_eixo_x = retonar_nome_eixo_x(tipo_selecao)

  fig = go.Figure()
  for produto in produtos:
      for linha in linhas:
        filtered = df.loc[(df['PRODUTO'] == produto) & (df[agrupamento] == linha)]
        titulo = 'MÉDIA DE POSTOS PESQUISADOS'
        titulo = '{} - Produto {}'.format(linha, produto)
        fig.add_trace(go.Scatter(x= retorna_valores_eixo_x(tipo_selecao, df), y=filtered[variavel]['mean'],
                  mode='lines+markers',
                  name=titulo))
  
  fig.update_layout(title='MÉDIA DE POSTOS PESQUISADOS',
              xaxis_title=nome_eixo_x,
              yaxis_title=variavel)
  return fig


def desenha_media_pais(tipo_selecao, selected_year, produtos, variavel, regioes): 
  fig = go.Figure()
  nome_eixo_x = retonar_nome_eixo_x(tipo_selecao)
  for produto in produtos:
      titulo = '{} - PRODUTO {}'.format('MÉDIA NACIONAL', produto)
      df_nacional = retorna_media_nacional(tipo_selecao,selected_year, variavel)
      df_nacional_filtrado = db.filtra_produto(df_nacional, produto)
      fig.add_trace(go.Scatter(x= retorna_valores_eixo_x(tipo_selecao, df_nacional_filtrado), y=df_nacional_filtrado[variavel]['mean'],
                  mode='lines+markers',
                  name=titulo))
    
  fig.update_layout(title='MÉDIA NACIONAL - {}'.format(variavel),
              xaxis_title=nome_eixo_x,
              yaxis_title=variavel)
  return fig

@app.callback(
    Output('graph-media-estados', 'figure'),
    [   Input('tipo_selecao_estado_ano', 'value'), 
        Input('ano_estado_ano', 'value'), 
        Input('produtos_estado', 'values'), 
        Input('variável_estado', 'value')])
def desenha_media_estados(tipo_selecao, selected_year, produtos, variavel):
  return grafico_media_pais(tipo_selecao, selected_year, produtos, variavel)

@app.callback(
    Output('graph-media-pais', 'figure'),
    [
        Input('tipo_selecao_regiao_ano', 'value'), 
        Input('ano_regiao_ano', 'value'), 
        Input('produtos_regiao_ano', 'values'), 
        Input('variável_regiao_ano', 'value')])
def desenha_media_pais(tipo_selecao, selected_year, produtos, variavel): 
  return grafico_media_pais(tipo_selecao, selected_year, produtos, variavel)

def grafico_media_pais(tipo_selecao, selected_year, produtos, variavel): 
  fig = go.Figure()
  nome_eixo_x = retonar_nome_eixo_x(tipo_selecao)
  for produto in produtos:
      titulo = 'MÉDIA NACIONAL - PRODUTO {}'.format(produto)
      df_nacional = retorna_media_nacional(tipo_selecao, selected_year, variavel)
      df_nacional_filtrado = db.filtra_produto(df_nacional, produto)
      fig.add_trace(go.Scatter(x= retorna_valores_eixo_x(tipo_selecao, df_nacional_filtrado), y=df_nacional_filtrado[variavel]['mean'],
                  mode='lines+markers',
                  name=titulo))
    
  fig.update_layout(title='MÉDIA NACIONAL - {}'.format(variavel),
              xaxis_title=nome_eixo_x,
              yaxis_title=variavel)
  return fig 
  
def retorna_media_nacional(tipo_selecao, selected_year, variavel):
  if(tipo_selecao == 1):
    return db.dados_pais_intervalo_ano_criterio(selected_year, variavel)

  return db.dados_pais_ano_criterio(selected_year, variavel)
    

def retorna_postos_df(agrupamento, tipo_selecao, selected_year, variavel):
  if(agrupamento == 'REGIÃO'):
    return retorna_valores_regiao(tipo_selecao, selected_year, variavel)
  
  return retorna_valores_estado(tipo_selecao, selected_year, variavel)
