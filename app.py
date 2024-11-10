import streamlit as st
from Gen_Agent import generate_use_cases
from resource import search_huggingface_datasets, search_kaggle_datasets

st.title("AI Use Case Generator")
st.write("""
This app generates AI use cases for companies based on industry and focus areas. You can also fetch relevant datasets from Kaggle and HuggingFace.
""")

industry_input = st.text_input("Enter the industry (e.g., Automotive, Healthcare, etc.):")
focus_input = st.text_input("Enter the company focus areas (e.g., supply chain, customer experience):")

if st.button("Generate Use Cases"):
    use_cases = generate_use_cases(industry_input, focus_input)
    st.subheader("Generated Use Cases")
    st.write(use_cases)

    hf_datasets = search_huggingface_datasets(" ".join(industry_input.split()))
    kaggle_datasets = search_kaggle_datasets(" ".join(industry_input.split()))

    st.subheader("Relevant Resources")
    st.write("### HuggingFace Datasets")
    st.write(hf_datasets)

    st.write("### Kaggle Datasets")
    st.write(kaggle_datasets)
