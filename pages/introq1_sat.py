import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from configurate import *

create_top(big_text_title=f'{st.session_state["q0"]} é uma ótima avaliação!', subtitle='Aparentemente, não há problemas com a estrutura do seu ambiente de trabalho :)', img_url=r'static\Q1sat.png')

if next_page_button(name='Combinado', phrase='Vamos apenas fazer algumas perguntas para ter certeza que está tudo bem, ok?'):
    switch_page('q1a')