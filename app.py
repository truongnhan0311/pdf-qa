from dotenv import load_dotenv
import streamlit as st
from htmlTemplates import css, bot_template, user_template


def handle_userinput(user_question):
    res = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = res['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Ask multi PDF content", page_icon=":books")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Ask about multiple PDFs Books :books:")
    user_question = st.text_input("Ask a question about your pdf:")
    if user_question:
        handle_userinput(user_question)


if __name__ == '__main__':
    main()
