import streamlit as st

# Title
st.title('Hello World!')
st.write('My app demo.')

# Sidebar
st.sidebar.header('Sidebar Menu')
# sidebar checkbox
st.sidebar.checkbox('main')


# Slider
slider_value = st.slider("Please select the temperature:", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

# write slider value
st.write(f"You selected {slider_value} using the slider.")

# st.container(20, True)
st.checkbox('GPT')
st.checkbox('Bert')
st.checkbox('LLama')

# sidebar checkbox
if st.sidebar.checkbox("Show more info."):
  st.write("More info from checkbox")

# Select Box
option = st.selectbox("Choose you model", ['gpt-2', 'gpt-3', 'gpt-4'])

st.write(f"You selected the {option} model.")

# Date Picker
date = st.sidebar.date_input('Select a date')

if date:
  st.write(f'You selected {date}')

# Multipage simulation with radio buttons
page = st.radio('Navigate to:', ['Home', 'About', 'Chatbot'], horizontal=True)

if page == 'Home':
  st.write('Home Page')
elif page == 'About':
  st.write('About Page')
else:
  st.write('Chatbot Page')

# Session State
if 'counter' not in st.session_state:
  st.session_state.counter = 0

incrementBtn = st.button('Increment')

if incrementBtn:
  st.session_state.counter += 1

st.write(f'Counter: {st.session_state.counter}')
