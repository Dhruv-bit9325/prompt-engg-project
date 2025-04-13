import streamlit as st
import google.generativeai as genai

# Set page config
st.set_page_config(
    page_title="Technical Glossary Builder",
    layout="wide"
)

# Hardcoded Gemini API key
api_key = "AIzaSyDrksJ5fvEXs7ZCKS4qQ4-LFgP8M4MZAE0"

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

# App title and description
st.title("Technical Glossary Builder")
st.markdown("Generate definitions for technical terms using AI")

# Simple category list
categories = ["Programming", "DevOps", "Data Science", "Networking", "Security", "Other"]

# Simple input form - just two inputs and a button
st.header("Generate Definition")

# Two inputs
term = st.text_input("Enter a technical term", placeholder="e.g., API, Docker, JWT")
category = st.selectbox("Select category", options=categories)

# Generate button
if st.button("Generate Definition"):
    if term:
        with st.spinner("Generating definition..."):
            try:
                # Prepare prompt for Gemini
                prompt = f"""
                Generate a clear, concise technical definition for the term "{term}" in the {category} category.
                
                The definition should:
                1. Be easy to understand for professionals in the field
                2. Include key aspects of the concept
                3. Be approximately 2-4 sentences long
                4. Include examples of use cases if appropriate
                """
                
                # Call Gemini API
                response = model.generate_content(prompt)
                
                # Display results
                st.subheader(f"Definition for: {term}")
                st.markdown(response.text)
                
                # Display as a glossary entry
                st.subheader("Glossary Entry Format")
                glossary_entry = f"""
                | Term | Category | Definition |
                |------|----------|------------|
                | **{term}** | {category} | {response.text.strip()} |
                """
                st.markdown(glossary_entry)
                
            except Exception as e:
                st.error(f"Error generating definition: {str(e)}")
    else:
        st.warning("Please enter a technical term")


# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>Made by Dhruv Mutha</div>", unsafe_allow_html=True)
