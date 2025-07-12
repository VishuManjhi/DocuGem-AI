import streamlit as st  
from functions import *
import base64
import os

# Initialize the API key in session state if it doesn't exist
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''

def display_pdf(uploaded_file):
    bytes_data = uploaded_file.getvalue()
    base64_pdf = base64.b64encode(bytes_data).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def load_streamlit_page():
    st.set_page_config(layout="wide", page_title="LLM PDF Reader (Gemini)")

    col1, col2 = st.columns([0.5, 0.5], gap="large")

    with col1:
        st.header("🔑 Input your Gemini API key")
        st.text_input('Gemini API key', type='password', key='api_key', label_visibility="collapsed")
        st.header("📄 Upload a PDF file")
        uploaded_file = st.file_uploader("Please upload your PDF document:", type="pdf")

    return col1, col2, uploaded_file

# Layout
col1, col2, uploaded_file = load_streamlit_page()

if uploaded_file is not None:
    with col2:
        display_pdf(uploaded_file)

    documents = get_pdf_text(uploaded_file)
    st.session_state.vector_store = create_vectorstore_from_texts(
        documents,
        api_key=st.session_state.api_key,
        file_name=uploaded_file.name
    )
    st.success("✅ PDF processed and embedded.")

# Query the vector store
with col1:
    if st.button("✨ Generate Answer"):
        with st.spinner("Working..."):
            answer = query_document(
                vectorstore=st.session_state.vector_store,
                query="Give me the title, summary, publication date, and authors of the research paper.",
                api_key=st.session_state.api_key
            )
            st.success("✅ Done!")
            st.write(answer)
