"""
PIP — Gerenciador de pacotes
 O que é: ferramenta padrão do Python para instalar bibliotecas externas.
 Uso principal: instalar, atualizar ou remover pacotes.
Comandos mais comuns:
    Pip install nome_projeto
    Pip install nome_projeto==versão
    Pip install --upgrade nome_projeto
    Pip uninstall nome_projeto
    Pip list
    Pip freeze > requirements.txt
    Pip install -r requirements.txt

    VENV — Ambiente virtual

 O que é: cria um ambiente isolado de pacotes para cada projeto.
 Por que usar: evita conflitos de versões entre projetos.


Criando e ativando um ambiente virtual:

python -m venv .venv
.venv\Scripts\Activate
Desativar ambiente virtual:
Deactivate
Excluir ambiente virtual:
 Basta deletar a pasta .venv 
"""