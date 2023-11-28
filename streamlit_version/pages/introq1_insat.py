import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from configurate import *

create_top(big_text_title=f'{st.session_state["q0"]}? Essa nota foi baixa :(', subtitle='Parece que você não está muito contente com a estrutura do seu ambiente de trabalho...', subsubtitle='Para conseguirmos encontrar uma solução, precisamos descobrir o que está causando desconforto. Assim será possível propor soluções para tornar o seu ambiente trabalho mais adequado para a realização das suas atividades.',img_url='https://github.com/Zac-Milioli/Quest_Luiza/blob/master/static/Q1insat.png?raw=true')

if next_page_button(name='Combinado', phrase='Você pode nos ajudar a descobrir qual é o problema respondendo as questões a seguir'):
    switch_page('QAI.py')
