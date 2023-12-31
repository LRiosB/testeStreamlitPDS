import streamlit as st
from st_pages import Page, show_pages



def pagDeslogado():
    show_pages([
        Page("./dccReview.py", "DCC Review"),
        Page("./paginasFrontEnd/login.py", "Login"),
        Page("./paginasFrontEnd/cadastro.py", "Cadastro"),
        Page("./paginasFrontEnd/quemsomos.py", "Quem somos?"),
        Page("./paginasFrontEnd/faq.py", "FAQ")
    ])

def pagLogado():
    show_pages([
        Page("./dccReview.py", "DCC Review"),
        Page("./paginasFrontEnd/meuPerfil.py", "Meu perfil"),
        Page("./paginasFrontEnd/materias.py", "Matérias"),
        Page("./paginasFrontEnd/fazerReviews.py", "Fazer review"),
        Page("./paginasFrontEnd/quemsomos.py", "Quem somos?"),
        Page("./paginasFrontEnd/faq.py", "FAQ")
    ])

def pagAdmin():
    show_pages([
        Page("./dccReview.py", "DCC Review"),
        Page("./paginasFrontEnd/adminValidarUsuario.py", "[Admin] Validar usuário"),
        Page("./paginasFrontEnd/adminCriarRemoverMateria.py", "[Admin] Criar e remover matérias"),
        Page("./paginasFrontEnd/quemsomos.py", "Quem somos?"),
        Page("./paginasFrontEnd/faq.py", "FAQ")
    ])

def atualizarEstado(estado:str):
    if(estado == "deslogado"):
        pagDeslogado()
    elif(estado == "logado"):
        pagLogado()
    elif(estado == "admin"):
        pagAdmin()