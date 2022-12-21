import streamlit as st
import requests
import datetime

st.title("Test Session State")

col1, col2, col3, col4 = st.columns(4)

col1.write (st.session_state)

col1.write('items found:')
for itm in st.session_state.items():
    col1.write(itm)

if 'keyName' not in st.session_state:
    st.session_state.keyName = 'Paul'

butUpd = col3.button("update" , )
butRes = col3.button("reset")

if butRes:
   st.session_state.keyName = "Marie"
   col4.write('reset !') 
    
if butUpd:
   col4.write('updated !') 

col2.text_input("Change name:" , key='keyName' ,)

col4.write('Name is: ' + st.session_state.keyName )   

st.markdown('### Bonjour **' + st.session_state.keyName  + '** !')
