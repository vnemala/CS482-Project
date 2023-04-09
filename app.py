import streamlit as st


from transformers import pipeline
import torch
import torch.nn.functional as functional

classifier = pipeline("sentiment-analysis")
text = st.text_input('Enter sample text', 'I really like HuggingFace and it is a great tool for deploying AI models.')

result = classifier(text)
st.write('The sentiment displayed in the sample text is', result)