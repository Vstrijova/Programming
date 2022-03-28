import streamlit as st

st.markdown("Welcome to **MyDictionary**")

import json, requests 

yourword = st.text_input('Enter a word:', 'sky')
option = st.selectbox('What are you looking for?',('Definitions', 'Synonyms', 'Antonyms'))

#st.write('You selected:', option)
url1 = 'https://api.datemuse.com/words?&md_d=' + yourword + '&max=3'
url2 = 'https://api.datemuse.com/words?&rel_syn=' + yourword + '&max=3'
url3 = 'https://api.datemuse.com/words?&rel_ant=' + yourword + '&max=3'

yourword1 = requests.get(url1)
youword2 = requests.get(url2)
yourword3 = requests.get(url3)

yourworddef = json.loads(yourword1.text)
yourwordsyn = json.loads(yourword2.text)
yourwordant = json.loads(yourword3.text)

for word in yourword:
  if option == 'Definitions':
    print(yourworddef)
  elif option == 'Synonyms':
    print(yourwordsyn)
  elif option == 'Antonyms':
    print(yourwordant)
  else:
    pass
