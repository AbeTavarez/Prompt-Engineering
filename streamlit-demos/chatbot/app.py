import streamlit as st

# sidebar menu
st.sidebar.title('Chats')

with st.container(height=100, border=True):
  st.page_link('./pages/chat.py', label='Chat')
  st.page_link('./pages/chat.py', label='About')

# header
st.title('Chatbot Home')
st.write('Chatbot powered by OpenAI')
st.divider()


