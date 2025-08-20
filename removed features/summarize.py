import streamlit as st
import tempfile
import os

from mistral_api import call_mistral
from utils.pdf_utils import extract_text_from_pdf_smart as extract_text_from_pdf
from shared_sidebar import render_sidebar  # if you use it elsewhere

st.title("📄 Upload & Summarize Legal Document")

uploaded_file = st.file_uploader("Upload a legal PDF", type=["pdf"])

if uploaded_file:
    # Save uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file.flush()
        os.fsync(tmp_file.fileno())
        tmp_path = tmp_file.name

    # Extract text
    text = extract_text_from_pdf(tmp_path)

    # Clean up the temp file
    os.remove(tmp_path)

    with st.spinner("Summarizing..."):
        summary_prompt = (
            "You are a legal assistant. Read the following legal document and provide a clear, concise summary "
            "highlighting the main parties, issues, clauses, and outcomes:\n\n"
            f"{text}"
        )
        summary = call_mistral(summary_prompt, max_tokens=600)

    st.success("📌 Summary:")
    st.write(summary)

    with st.expander("🔍 View Extracted Text (Optional)"):
        st.text_area("Extracted Text", text, height=300)
