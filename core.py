import streamlit as st

isAuth = False


def login(login, psswd):
    if login == st.secrets["db_username"] and psswd == st.secrets["db_password"]:
        return True
    else:
        return False


st.write('''
# Создание отчета ДДС
''')

if not isAuth:
    login = st.text_input('Логин')
    passwd = st.text_input('Пароль', type='password')
    st.button('Войти')

    if login(login, passwd):
        st.success('Успешно')
        isAuth = True

if isAuth:
    with st.form(key='my_form'):
        st.header('Создание отчета')
        st.subheader('Выбор промежутка')
        text_input = st.text_input(label='Выберите промежуток')
        submit_button = st.form_submit_button(label='Создать')
        # st.button('Создать')
