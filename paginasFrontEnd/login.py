import streamlit as st
from init import init
init()
from showPages import atualizarEstado
atualizarEstado(st.session_state["estado do usuario"])
#st.set_page_config(initial_sidebar_state="collapsed")
#from dccReview import esconderPaginas
#st.experimental_rerun()
#esconderPaginas(st.session_state["estado do usuario"])