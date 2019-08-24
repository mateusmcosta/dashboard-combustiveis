# DASHBOARD Preço dos combustíveis no Brasil

Trabalho da disciplina de Visualização de Dados. Criação de um Dashboard interativo que possibilite a visualização e entendimento da base de dados.
O trabalho foi desenvolvido em Python versão 3.7.4, e utilizando as libs:

    - Dash
    - Plotly
    - Flask
    - Pandas

## Passos para execução

O trabalho pode ser executar o trabalho de três formas:

### Instalação local
    - Ter o Python 3
    - No termial navegar até a pasta do projeto
    - Rodar o comando 
            pip install -r requirements.txt  
    - Rodar o comando
            python index.py
    - 

### Execução via Docker
    - Uma imagem docker foi disponibilizada e publicada no DockerHub. Tendo o docker instalado na máquina executar:

            sudo docker run -p 8050:8050 -it docker.io/mmdcosta/python:python-unisinos-dashboard

### Acessando o DashBoard
    http://0.0.0.0:8050/dashboard/preco-combustiveis-brasil/