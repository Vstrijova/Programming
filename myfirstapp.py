import streamlit as st
st.header("hello world! :)")
title = st.text_input('Gimme a movie title:', 'insert here your title')
st.write('The current movie title is', title)

genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'), help='click on one of the 3 options')
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
