import streamlit as st
from init import init
from st_pages import Page, Section, add_page_title, show_pages, hide_pages
from showPages import atualizarEstado

#st.set_page_config(initial_sidebar_state="collapsed")

# inicialização do sessionState
init()

# declaração das páginas


# ocultação das páginas
atualizarEstado("deslogado")

#add_page_title()

if st.button("deslogado"):
    atualizarEstado("deslogado")
if st.button("logado"):
    atualizarEstado("logado")
if st.button("admin"):
    atualizarEstado("admin")


st.write("Hello world")