import streamlit as st
import time
import fitz

def pdf_to_text(file_path):
    doc = fitz.open(file_path)  # Open a document
    num_pages = len(doc)
    return doc, num_pages

def main():
    st.title("PDF Text Processing App")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        temp_file_path = f"/tmp/{uploaded_file.name}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.read())

        # Extract text and get the number of pages
        doc, num_pages = pdf_to_text(temp_file_path)

        # Display results
        st.subheader(f"Number of Pages: {num_pages}")

        # Page navigation
        page_number = st.slider("Select a Page", 1, num_pages, 1)

        # Display content of the selected page
        st.subheader(f"Page {page_number} Content:")
        page = doc.load_page(page_number - 1)
        page_text = page.get_text()
        st.text(page_text)

if __name__ == "__main__":
    main()
