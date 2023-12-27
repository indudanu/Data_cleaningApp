import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
import time

# Function to convert PDF to text using pdfplumber
def pdf_to_text(file_path):
    loader = PyMuPDFLoader(file_path)
    start_time = time.time()  # Record the start time
    pages = loader.load()
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    return pages[0].page_content, elapsed_time

# Streamlit app
def main():
    st.title("PDF Text Processing App")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        text, elapsed_time = pdf_to_text(uploaded_file)

        st.subheader("Original Text:")
        st.text(text)

        st.subheader(f"Time to load PDF: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
