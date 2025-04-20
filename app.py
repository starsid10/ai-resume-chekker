import streamlit as st
from pyresparser import ResumeParser
import os
import tempfile

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 AI-Powered Resume Screener")
st.write("Upload a resume (PDF or DOCX) to extract key information like name, skills, education, etc.")

uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

if uploaded_file is not None:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name.split('.')[-1]) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name

    # Parse resume
    try:
        data = ResumeParser(temp_path).get_extracted_data()
        if data:
            st.success("✅ Resume parsed successfully!")
            st.subheader("🔍 Extracted Information:")
            for key, value in data.items():
                st.markdown(f"**{key.capitalize()}**: {value}")
        else:
            st.warning("Could not extract data. Please try another resume.")

    except Exception as e:
        st.error(f"❌ Error while parsing resume: {str(e)}")

    # Clean up temp file
    os.remove(temp_path)
