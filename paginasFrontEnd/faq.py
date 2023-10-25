import streamlit as st
from init import init
init()
from showPages import atualizarEstado
atualizarEstado(st.session_state["estado do usuario"])


import showPages

showPages.pagLogado()