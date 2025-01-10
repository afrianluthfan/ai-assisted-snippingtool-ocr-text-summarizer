import pytesseract
from PIL import ImageGrab, Image
import google.generativeai as genai

# Get the API key from the environment variable
genai.configure(api_key="AIzaSyBG63eP-V_hBXC0sTBLRjnuaneUpMgY0O4")
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)

# Grab the image from the clipboard
clipboard_image = ImageGrab.grabclipboard()


def extract_quiz_options(image):
    """
    Extract quiz options from an image.

    :param image: The image containing the quiz options.
    :return: A list of quiz options extracted from the image.
    """
    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(image, lang="ind+eng")

    # Split the text into lines and filter for option lines
    lines = extracted_text.split("\n")
    options = [
        line.strip()
        for line in lines
        if line.strip().startswith(("a.", "b.", "c.", "d."))
    ]

    # Remove the option prefixes (a., b., etc.)
    clean_options = [option[2:].strip() for option in options]
    return clean_options


def process_text(input_text, option):
    """
    Processes the text based on the selected option: summarize or answer quiz.

    :param input_text: The text to process.
    :param option: User choice: 'summarize' or 'quiz'.
    :return: Processed result (summary or quiz answer).
    """

    if option == "summarize":
        prompt = (
            "Summarize this text in the language that the text is in: " + input_text
        )
    elif option == "quiz":
        prompt = (
            "Answer the following quiz question in the language that the quiz is presented in: "
            + input_text
        )
    else:
        return "Invalid option selected."

    # Make the request to the Gemini API
    response = model.generate_content(prompt)

    # Check if the request was successful
    try:
        return response.text
    except AttributeError:
        return "Error: Unable to generate content."


# Main program flow
if isinstance(clipboard_image, Image.Image):
    # Convert the image to RGB format to ensure compatibility
    clipboard_image = clipboard_image.convert("RGB")

    # Ask user to choose an action
    print("Choose an option:")
    print("1. Summarize the extracted text")
    print("2. Answer a quiz from the extracted text")
    print("3. Print out the text into terminal")
    print("4. Extract quiz options into an array")
    choice = input("Selected number: ")

    if choice == "1":
        # Extract text from the image using Tesseract
        text = pytesseract.image_to_string(clipboard_image, lang="ind+eng")
        RESULT = process_text(text, "summarize")
    elif choice == "2":
        # Extract text from the image using Tesseract
        text = pytesseract.image_to_string(clipboard_image, lang="ind+eng")
        RESULT = process_text(text, "quiz")
    elif choice == "3":
        # Extract text from the image using Tesseract
        text = pytesseract.image_to_string(clipboard_image, lang="ind+eng")
        RESULT = print(text)
    elif choice == "4":
        # Extract quiz options from the image
        quiz_options = extract_quiz_options(clipboard_image)
        RESULT = print(quiz_options)
    else:
        RESULT = "Invalid selection. Please choose a valid option."

    print(RESULT)
else:
    print("The clipboard does not contain an image.")
