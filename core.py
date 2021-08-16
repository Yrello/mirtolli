import streamlit as st
isAuth = False
def login(a):
    if a == '1':
        return True
    else:
        return False


st.write('''
# Создание отчета ДДС
''')

if not isAuth:
    passwd = st.text_input('Пароль',type='password')
    st.button('Войти')

    if login(passwd):
        st.success('Успешно')
        isAuth = True

if isAuth:
    with st.form(key='my_form'):
        st.header('Создание отчета')
        st.subheader('Выбор промежутка')
        text_input = st.text_input(label='Выберите промежуток')
        submit_button = st.form_submit_button(label='Создать')
        #st.button('Создать')