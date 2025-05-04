import re
import streamlit as st
from transformers import pipeline

# page config
st.set_page_config(
    page_title='Reflective AI Chat',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# config
CONV_MODEL_NAME = 'facebook/blenderbot-400M-distill'

@st.cache_resource(show_spinner=False)
def load_conversation_pipeline():
    return pipeline(
        'text2text-generation',
        model=CONV_MODEL_NAME,
        tokenizer=CONV_MODEL_NAME
    )

conv_pipe = load_conversation_pipeline()

# init chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# tit
st.title('A little bit trained AI')
st.write('It\'s still dumb a bit.')

# input field
user_input = st.text_input('User:')

if user_input:
    # append user message
    st.session_state.chat_history.append({'speaker': 'user', 'text': user_input})

    # sos message
    if re.search(r"\b(kill myself|suicide|end my life|i will die)\b", user_input, re.IGNORECASE):
        crisis_msg = (
            "I’m really sorry you’re feeling like this. You deserve support—please reach out to a crisis line or someone you trust right now."
        )
        st.session_state.chat_history.append({'speaker': 'bot', 'text': crisis_msg})
        st.warning(crisis_msg)
    else:
        # generate bot response
        result = conv_pipe(user_input, max_length=100)
        # normalize result format
        if isinstance(result, list):
            response = result[0].get('generated_text', '')
        else:
            response = result.get('generated_text', '')

        # append bot message
        st.session_state.chat_history.append({'speaker': 'bot', 'text': response})

# render chat history
for turn in st.session_state.chat_history:
    if turn['speaker'] == 'user':
        st.markdown(f"**User:** {turn['text']}")
    else:
        st.markdown(f"**AI:** {turn['text']}")
