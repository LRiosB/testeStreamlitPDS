import streamlit as st



def init():
    if "init" not in st.session_state:
        st.session_state["init"] = True
        st.session_state["estado do usuario"] = "deslogado"