import pytesseract
from PIL import ImageGrab, Image
import google.generativeai as genai
import os
import requests


# Get the API key from the environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Grab the image from the clipboard
clipboard_image = ImageGrab.grabclipboard()


def summarize_text(text):

    # Make the request to the Gemini API
    response = model.generate_content("Summarize this text: " + text)

    # Check if the request was successful
    try:
        return response.text
    except:
        return f"Error: {response.status_code}"


# Check if the clipboard content is an image
if isinstance(clipboard_image, Image.Image):
    # Convert the image to RGB format to ensure compatibility
    clipboard_image = clipboard_image.convert("RGB")

    # Extract text from the image using Tesseract
    text = pytesseract.image_to_string(clipboard_image, lang="ind+eng")

    # Print the extracted text
    # print("Extracted Text:\n", text)

    # Summarize the extracted text using Gemini API
    summary = summarize_text(text)
    print(summary)
else:
    print("The clipboard does not contain an image.")
