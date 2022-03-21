import streamlit as st
st.header("hello world! :)")
title = st.text_input('Gimme a movie title:', 'insert here your title')
st.write('The current movie title is', title)
