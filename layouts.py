import dash_core_components as dcc
import dash_html_components as html
from components import Header
import data_base as db

# Efetua a leitura da base de dados
#df = pd.read_csv('data/performance_analytics_cost_and_ga_metrics.csv')

produtos = []
for produto in db.produtos():
  produtos.append({'label': produto, 'value': produto})

variaveis = []
for variavel in db.retorna_variaveis():
    variaveis.append({'label': variavel, 'value': variavel})

regioes = []
for regiao in db.regioes():
    regioes.append({'label': regiao, 'value': regiao})

estados = []
for estado in db.estados():
    estados.append({'label': estado, 'value': estado})    

layout_regioes =  html.Div([
    html.Div([
        # CC Header
        Header(),
        # Header Bar
        html.Div([
          html.H4(["Visão geral - Regiões"], className="gs-header gs-text-header padded",style={'marginTop': 15})
        ]),
        # Tipo
        html.Div([
          dcc.RadioItems(
                id="tipo_selecao_regiao_ano",
                options=[
                    {'label': 'ANOS', 'value': 1},
                    {'label': 'MESES', 'value': 2},
                ],
                value=1,
                labelStyle={'display': 'inline-block', 'width': '10%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
        )], className="row ", style={'marginTop': 30, 'marginBottom': 30}),
   
        html.Div([
          'Produtos:'
        ], className="row ", style={'marginTop': 30, 'font-size': 20}),
        # Produto
        html.Div([
          dcc.Checklist(
                id="produtos_regiao_ano",
                options=produtos,
                values=['GASOLINA COMUM'],
               labelStyle={'display': 'inline-block', 'width': '30%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
          )], className="row ", style={'marginTop': 30, 'marginBottom': 30}),
        html.Div([
          'Regiões:'
        ], className="row ", style={'marginTop': 30, 'font-size': 20, 'left-padding': '15px'}),
        # Produto
        html.Div([
          dcc.Checklist(
                id="regiao_regiao_ano",
                options=regioes,
                values=['SUL','SUDESTE'],
                labelStyle={'display': 'inline-block', 'width': '20%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
          )], className="row ", style={'marginTop': 30, 'marginBottom': 30}),
        html.Div([
          'Variável:'
        ], className="row ", style={'marginTop': 30, 'font-size': 20, 'left-padding': '15px'}),
        # Variavél
        html.Div([
          dcc.RadioItems(
                id="variável_regiao_ano",
                options=variaveis,
                value='PREÇO MÉDIO REVENDA',
                labelStyle={'display': 'inline-block', 'width': '20%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
        )], className="row ", style={'marginTop': 30, 'marginBottom': 30}),
        # Ano
        html.Div([
          dcc.Slider(
              id='ano_regiao_ano',
              min=db.ano_min(),
              max=db.ano_max(),
              value=db.ano_max(),
              marks={str(year): str(year) for year in db.anos()},
              step=None
          )
        ], className="row ", style={'marginTop': 30, 'marginBottom': 45,  'left-padding': '15px'}),
        # First Data Table
        dcc.Graph(id='graph-with-slider'),

         dcc.Graph(id='graph-estabelecimentos-pesquisados'),
        ], className="subpage", style={'border-style': 'solid;', 'left-padding': '15px'}),
    ], className="page")


layout_estados =  html.Div([
    html.Div([
        # CC Header
        Header(),
        # Header Bar
        html.Div([
          html.H4(["Visão geral - Estados"], className="gs-header gs-text-header padded",style={'marginTop': 15})
        ]),
        # Tipo
        html.Div([
          dcc.RadioItems(
                id="tipo_selecao_estado_ano",
                options=[
                    {'label': 'ANOS', 'value': 1},
                    {'label': 'MESES', 'value': 2},
                ],
                value=1,
                labelStyle={'display': 'inline-block', 'width': '10%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
        )], className="row ", style={'marginTop': 30, 'marginBottom': 30}),
   
        html.Div([
          'Produtos:'
        ], className="row ", style={'marginTop': 30, 'font-size': 20}),
        # Produto
        html.Div([
          dcc.Checklist(
                id="produtos_estado",
                options=produtos,
                values=['GASOLINA COMUM'],
                labelStyle={'display': 'inline-block', 'width': '30%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
          )], className="row ", style={'marginTop': 30, 'marginBottom': 30}),
        html.Div([
          'Estados:'
        ], className="row ", style={'marginTop': 30, 'font-size': 20}),
        # Produto
        html.Div([
          dcc.Checklist(
                id="estados",
                options=estados,
                values=['RIO GRANDE DO SUL','ACRE'],
                 labelStyle={'display': 'inline-block', 'width': '20%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
          )], className="row ", style={'marginTop': 30, 'marginBottom': 30}),
        html.Div([
          'Variável:'
        ], className="row ", style={'marginTop': 30, 'font-size': 20}),
        # Variavél
        html.Div([
          dcc.RadioItems(
                id="variável_estado",
                options=variaveis,
                value='PREÇO MÉDIO REVENDA',
               labelStyle={'display': 'inline-block', 'width': '20%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
        )], className="row ", style={'marginTop': 30, 'marginBottom': 30}),
        # Ano
        html.Div([
          dcc.Slider(
              id='ano_estado_ano',
              min=db.ano_min(),
              max=db.ano_max(),
              value=db.ano_max(),
              marks={str(year): str(year) for year in db.anos()},
              step=None
          )
        ], className="row ", style={'marginTop': 30, 'marginBottom': 30, 'left-padding': '15px'}),
        # First Data Table
        dcc.Graph(id='graph-with-slider-estado'),

         dcc.Graph(id='graph-estabelecimentos-pesquisados-estados'),
        ], className="subpage")
    ], className="page")


######################## 404 Page ########################
noPage = html.Div([ 
    # CC Header
    html.P(["404 Page not found"])
    ], className="no-page")
