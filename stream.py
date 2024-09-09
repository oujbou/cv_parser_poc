import streamlit as st
import pandas as pd
#import openai_helper
from helper_functions import extract_resume_data, extract_from_pdf

resume_data = pd.DataFrame({
    "Entities": ["Name", "email_id", "mob_number", "qualification", "experience", "skills", "certification",
                 "achievement"],
    "value": ["", "", "", "", "", "", "", ""]
})

st.title("Resume Extractor App")

uploaded_file = st.file_uploader("upload a file", type=["pdf", "docx", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    text = extract_from_pdf(uploaded_file)

if st.button("Extract"):
    resume_data = extract_resume_data(text)

st.dataframe(resume_data,
             column_config={
                 "Entities": st.column_config.Column(width=150),
                 "value": st.column_config.Column(width=450)

             },
             hide_index=True)
