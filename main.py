import streamlit as st
import time
import fitz

def pdf_to_text(file_path):
    start_time = time.time()  # Record the start time
    doc = fitz.open(file_path)  # Open a document
    text = ""
    for page in doc:  # Iterate through the document pages
        text += page.get_text()
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    return text, elapsed_time

def main():
    st.title("Fast PDF Text Processing App")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        temp_file_path = f"/tmp/{uploaded_file.name}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.read())

        # Extract text and measure time
        text, elapsed_time = pdf_to_text(temp_file_path)

        # Display results
        st.subheader(f"Time to load PDF: {elapsed_time:.2f} seconds")
        st.subheader("Original Text:")
        st.text(text)

if __name__ == "__main__":
    main()
