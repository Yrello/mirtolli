import streamlit as st

def login(a):
    if a == '1':
        return True
    else:
        return False


st.write('''
# Создание отчета ДДС
''')

passwd = st.text_input()
st.button('Войти')

if login(passwd):
    st.text('Успешно')
