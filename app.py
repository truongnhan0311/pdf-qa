from dotenv import load_dotenv
import streamlit as st
from htmlTemplates import css, bot_template, user_template
from PyPDF2 import PdfReader


def handle_userinput(user_question):
    res = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = res['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extractText()
    return text


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

    with st.sidebar:
        st.subheader("Your Pdf")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)


if __name__ == '__main__':
    main()
