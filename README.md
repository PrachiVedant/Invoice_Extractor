
# Multimodal Invoice Extractor with Google Gemini API

This project is a Streamlit web app that extracts information from invoice images or PDFs using Google Gemini (Generative AI) models.

## Features
- Upload invoice images (JPG, PNG) or PDFs
- Enter a custom query about the invoice
- Uses Google Gemini API to extract and answer questions about the invoice
- Model selection: Automatically lists available Gemini models that support content generation
- Handles image and PDF uploads

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd INVOICE_EXTRACTOR
```

### 2. Create and Activate a Virtual Environment (optional but recommended)
```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Set Up Google Gemini API Key
- Create a `.env` file in the project root with the following content:
  ```
  GOOGLE_API_KEY=your_google_gemini_api_key_here
  ```
- Get your API key from [Google AI Studio](https://makersuite.google.com/) or Google Cloud Console.

### 5. Run the App
```
streamlit run app.py
```
- Open the provided local URL in your browser.

## Usage
1. Select a supported Gemini model from the dropdown.
2. Upload an invoice image (JPG/PNG) or PDF.
3. Enter your query (e.g., "What is the total amount?").
4. Click "Tell me about the invoice" to get the extracted information.

## Troubleshooting
- **Model Not Found:** If you see a 404 error for a model, select another model from the dropdown.
- **Quota Exceeded:** If you see a 429 error, your Google Gemini API quota is exhausted. Check your Google Cloud billing and quota settings.
- **API Key Issues:** Make sure your `.env` file is present and contains a valid API key.

## Dependencies
- streamlit
- python-dotenv
- pillow
- google-generativeai

## License
This project is for educational/demo purposes. See LICENSE for details.
