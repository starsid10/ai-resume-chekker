# app.py
import streamlit as st
import spacy
import os

# Check if model is downloaded, if not, download it
model_path = os.path.join("degree", "model")
if not os.path.exists(model_path):
    # Download the required model
    spacy.cli.download("en_core_web_sm")  # Use the correct model here


from resume_parser import extract_text_from_pdf, extract_text_from_docx
from preprocess import clean_text
from your_matching_script import rank_resumes  # reuse functions

st.title("AI Resume Screening System")

uploaded_files = st.file_uploader("Upload Resumes (PDF or DOCX)", accept_multiple_files=True)
job_description = st.text_area("Paste the Job Description")

if st.button("Match Resumes"):
    resume_texts = []
    filenames = []

    for file in uploaded_files:
        if file.name.endswith('.pdf'):
            text = extract_text_from_pdf(file)
        else:
            text = extract_text_from_docx(file)
        cleaned = clean_text(text)
        resume_texts.append(cleaned)
        filenames.append(file.name)

    jd_cleaned = clean_text(job_description)
    ranked_indices, scores = rank_resumes(resume_texts, jd_cleaned)

    st.subheader("Top Matching Resumes:")
    for idx in ranked_indices:
        st.write(f"{filenames[idx]} - Score: {scores[idx]:.2f}")
