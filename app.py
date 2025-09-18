from dotenv import load_dotenv

load_dotenv()

import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# List available models and let user select
def get_supported_models():
    models = []
    for m in genai.list_models():
        if 'generateContent' in getattr(m, 'supported_generation_methods', []):
            models.append(m.name)
    return models

supported_models = get_supported_models()
if not supported_models:
    st.error("No supported Gemini models found for generateContent. Check your API key and project permissions.")
    st.stop()

selected_model = st.selectbox("Select Gemini model", supported_models)
model = genai.GenerativeModel(selected_model)


# function to get response from Gemini model

def get_gemini_response(input_text, image_parts, prompt):
    # Gemini expects image_parts to be a list of dicts for images, or just text for text-only
    contents = [prompt]
    if input_text:
        contents.append(input_text)
    if image_parts:
        contents.extend(image_parts)
    response = model.generate_content(contents)
    # Return only the text part of the response
    return getattr(response, 'text', str(response))

#converting the input image into bytes
def input_image_setup(upload_file):
    if upload_file is not None:
        bytes=upload_file.getvalue()
        image_parts=[
            {
                "mime_type":upload_file.type,
                "data":bytes
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File not found")


#streamlit app
st.set_page_config(page_title="Multimodel Invoice Extractor")
st.header("Multimodel Invoice Extractor")
input_text=st.text_input("Enter your query",key="input_text")
upload_file =st.file_uploader("Choose a file...",type=['JPG','PNG','PDF'])


if upload_file is not None:
    # Only display image if it's an image file
    if upload_file.type in ["image/jpeg", "image/png"]:
        image = Image.open(upload_file)
        st.image(image, caption="Uploaded image", use_column_width=True)
    elif upload_file.type == "application/pdf":
        st.info("PDF uploaded. Preview not supported, but will be processed.")

submit=st.button("Tell me about the invoice")


#how the gemini should behave
input_prompt="""
You are an invoice extraction model. 
We will upload an invoice image and you need to answer questions that has been asked based on the invoice.
"""

#if submit buttton is clicked

if submit:
    image_data = input_image_setup(upload_file)
    response = get_gemini_response(input_text, image_data, input_prompt)
    st.subheader("The response is: ")
    # Only display as text, not bytes
    st.write(str(response))