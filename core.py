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
    with st.form(key='login_form'):
        user = st.text_input('Логин')
        passwd = st.text_input('Пароль', type='password')
        but = st.form_submit_button(label='Войти')

    if login(user, passwd):
        st.success('Успешно')
        isAuth = True

if isAuth:
    with st.form(key='my_form'):
        st.header('Создание отчета')
        st.subheader('Выбор промежутка')
        #text_input = st.text_input(label='Выберите промежуток')
        first_date = st.date_input(label='Начало')
        second_date = st.date_input(label='Конец')
        submit_button = st.form_submit_button(label='Создать')
        # st.button('Создать')
