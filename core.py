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
        st.text('Успешно')
        isAuth = True

if isAuth:
    st.header('Создание отчета')