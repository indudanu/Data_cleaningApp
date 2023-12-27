import streamlit as st
import pdfplumber
# Function to convert PDF to text using pdfplumber
def pdf_to_text(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Streamlit app
def main():
    st.title("PDF Text Processing App")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        text = pdf_to_text(uploaded_file)

        st.subheader("Original Text:")
        st.text(text)

if __name__ == "__main__":
    main()
