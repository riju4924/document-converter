import streamlit as st
import os
from converter import word_to_pdf, pdf_to_word

st.set_page_config(page_title="Document Converter", layout="centered")

st.title("📄 Word ↔ PDF Converter")

conversion = st.selectbox(
    "Choose conversion type",
    ["Word to PDF", "PDF to Word"]
)

uploaded_file = st.file_uploader(
    "Upload file",
    type=["docx", "pdf"]
)

if uploaded_file:
    input_file = f"temp_{uploaded_file.name}"

    with open(input_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Convert"):
        if conversion == "Word to PDF":
            output_file = uploaded_file.name.replace(".docx", ".pdf")
            word_to_pdf(input_file, output_file)

        else:
            output_file = uploaded_file.name.replace(".pdf", ".docx")
            pdf_to_word(input_file, output_file)

        with open(output_file, "rb") as f:
            st.download_button(
                "⬇️ Download Converted File",
                f,
                output_file
            )

        os.remove(input_file)
