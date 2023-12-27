import streamlit as st
import time
import fitz
import tempfile

def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        _, temp_file_path = tempfile.mkstemp(suffix=".pdf")
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.read())
        return temp_file_path
    return None

# Function to convert PDF to text using pdfplumber
def pdf_to_text(file_path):
    start_time = time.time()  # Record the start time
    doc = fitz.open(file_path) # open a document
    text = ""
    for page in doc: # iterate the document pages
        text += page.get_text()
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    return text, elapsed_time

# Streamlit app
def main():
    st.title("PDF Text Processing App")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    uploaded_file_path = save_uploaded_file(uploaded_file)

    if uploaded_file_path is not None:
        text, elapsed_time = pdf_to_text(uploaded_file_path)
        st.subheader(f"Time to load PDF: {elapsed_time:.2f} seconds")
        st.subheader("Original Text:")
        st.text(text)

if __name__ == "__main__":
    main()
