import streamlit as st
import json, requests 

st.markdown("Welcome to **MyDictionary**")



keyword = st.text_input('Enter a word:', 'sky')
option = st.selectbox('What are you looking for?',('Meaning', 'Synonyms', 'Antonyms'))

url_a = 'https://api.datamuse.com/words?ml=' + keyword + '&max=5'
url_b = 'https://api.datamuse.com/words?rel_syn=' + keyword + '&max=5'
url_c = 'https://api.datamuse.com/words?rel_ant=' + keyword + '&max=5'

response_a = requests.get(url_a)
dataFromDatamuse_a = json.loads(response_a.text) 
response_b = requests.get(url_b)
dataFromDatamuse_b = json.loads(response_b.text)
response_c = requests.get(url_c)
dataFromDatamuse_c = json.loads(response_c.text)

if option == 'Meaning':
  st.write(dataFromDatamuse_a)
elif option == 'Synonyms':
  st.write(dataFromDatamuse_b)
elif option == 'Antonyms':
  st.write(dataFromDatamuse_c)
else:
  pass
