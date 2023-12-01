from configurate import *

create_top(big_text_title='Onde você passa mais tempo?', subtitle='Em um dia típico de trabalho, com que frequência você estima que utilize...')

opcoes = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca', 'não possui']

estacaodetrabalho = create_radio(large=True, phrase='sua estação de trabalho?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='estacaotrab')
estacaodetrabalhorotativa = create_radio(large=True, phrase='estações de trabalho rotativas e/ou não-fixas?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='estacaorotativa')
areagrupo = create_radio(large=True, phrase='áreas específicas para desenvolver atividades em grupo e/ou dinâmicas?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='areagrupo')
individual = create_radio(large=True, phrase='áreas específicas para desenvolver atividades individuais e/ou focadas?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='individual') 
conferencia = create_radio(large=True, phrase='salas de conferência e/ou reunião?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='conf')
fora = create_radio(large=True, phrase='fica fora do escritório, em atividades externas?', use_list_selection=True, selection=opcoes, show_values=True, two_columns_width=[1.5,2], key='fora')


if next_page_button('Próximo'):
    options = [estacaodetrabalho, estacaodetrabalhorotativa, areagrupo, individual, conferencia, fora]
    if None in options:
        st.error('Responda **todas** as questões para prosseguir') 
    else:
        PeR['id_pergunta'] += ['q1c-1', 'q1c-2', 'q1c-3', 'q1c-4', 'q1c-5', 'q1c-6']
        PeR['resposta'] += options
        switch_page('q2')
