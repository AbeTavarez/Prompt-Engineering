import streamlit as st
from groq import Groq

# Create Groq client
client = Groq(api_key=st.secrets['GROQ_API_KEY'])

# Session State Dictionary
print(st.session_state)

# Set a default model
if "default_model" not in st.session_state:
  st.session_state['default_model'] = "llama3-8b-8192"


# Create messages collection in session state
if 'messages' not in st.session_state:
  st.session_state.messages = []

# Sidebar menu
st.sidebar.title('Chat')

# Page Header
st.title('Chat')
st.write('Chatbot powered by OpenAI')
st.divider()


# Display messages
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Chat input prompt
if prompt := st.chat_input():
  # st.write(f"You said: {prompt}")
  # Add the message to the messages
  st.session_state.messages.append({'role': 'user', 'content': prompt})

  # display user message
  with st.chat_message('user'):
    st.markdown(prompt)
  
 # Display assistant response in chat message container
  with st.chat_message("assistant"):
      response_text = st.empty()

      completion = client.chat.completions.create(
          model=st.session_state.default_model,
          messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
          ],
          stream=True,
        )
      full_response = ''
      for chunk in completion:
        print(chunk.choices[0].delta.content)
        full_response += chunk.choices[0].delta.content or ''
        response_text.markdown(full_response)

      print(full_response)
      # st.write(full_response)
      st.session_state.messages.append({"role": "assistant", "content": full_response})