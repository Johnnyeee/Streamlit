from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='openai-community/gpt2')
set_seed(42)
import streamlit as st
import streamlit as st
from transformers import pipeline, set_seed

st.title('Chat with AI')
st.markdown("### Type below and let AI continue your text")

generator = pipeline('text-generation', model='openai-community/gpt2')
set_seed(42)

with st.form("my_form"):
    user_input = st.text_area("Your text:", height=100)
    max_length = st.slider("Max length of response", min_value=50, max_value=200, value=100)
    num_return_sequences = st.number_input("Number of responses", min_value=1, max_value=5, value=1)
    submitted = st.form_submit_button("Submit")

if submitted:
    responses = generator(user_input, max_length=max_length, num_return_sequences=num_return_sequences)
    for i, response in enumerate(responses):
        st.write(f"Response {i+1}:")
        st.text_area("", value=response['generated_text'], height=150, key=f"response_{i}")
