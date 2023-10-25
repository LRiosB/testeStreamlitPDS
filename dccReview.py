import streamlit as st
from init import init
init()
from showPages import atualizarEstado
atualizarEstado(st.session_state["estado do usuario"])

#st.set_page_config(initial_sidebar_state="collapsed")


# declaração das páginas


# ocultação das páginas
atualizarEstado("deslogado")

#add_page_title()

if st.button("deslogado"):
    st.session_state["estado do usuario"] = "deslogado"
if st.button("logado"):
    st.session_state["estado do usuario"] = "logado"
if st.button("admin"):
    st.session_state["estado do usuario"] = "admin"


st.write("Hello world")