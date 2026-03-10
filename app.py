import streamlit as st
from google import genai
from pdf_reader import extract_text_from_pdf

# API key
client = genai.Client(api_key="AIzaSyAbYVj2lm1wV7YBDhcBslQXMxx0cPlfLgo")

st.title("📚 AI Study Notes Generator")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
text_input = st.text_area("Or paste your text here")

if st.button("Generate Notes"):

    text = ""

    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)

    elif text_input:
        text = text_input

    if text == "":
        st.warning("Please upload a PDF or enter text.")
    else:

        prompt = f"""
Summarize the following study material.

Provide:
1. Short Summary
2. Key Points
3. Important Exam Questions

Text:
{text}
"""

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )

        st.subheader("Generated Notes")
        st.write(response.text)