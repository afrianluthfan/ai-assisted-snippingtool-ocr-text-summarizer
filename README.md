# SnippingTool OCR

### About

This is a program that can summarize any texts you can screenshot with Microsoft's Snipping Tool with the help of Google's Gemini. I made this cos i was bored lol

### Requirements

- Windows OS (well, duh)
- Microsoft's Snipping Tool (should come preinstalled)
- Python 3.12.1 (the one im using)
- [UB Mannheim's Tesseract](https://github.com/tesseract-ocr/tesseract)
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)

### Instructions

1.  Clone this project into your local machine
2.  Open up powershell/command prompt inside of the newly cloned folder
3.  Initialize it by running

    `python -m venv venv`

4.  Activate the virtual environment by running

    `venv\Scripts\activate`

5.  Install all of the requirements by running

    `pip install -r requirements.txt`

6.  Get tesseract **[here](https://github.com/tesseract-ocr/tesseract)**
7.  Install it (preferably in `C:\Program Files\`)
8.  Add Tesseract to your path in Environment Variables (refer to [here](https://www.google.com/search?q=how+to+add+environment+variable+in+windows&oq=how+do+i+add+to+envir&sourceid=chrome&ie=UTF-8) if you don't know how to do it)
9.  Set the GEMINI_API_KEY variable in your local machine for your Gemini API Key with Powershell/Command Prompt by running

    `$Env:GEMINI_API_KEY= "(YOUR GEMINI API KEY GOES HERE)"`

    e.g.,
    `$Env:GEMINI_API_KEY = "qwertyuiop-asdf_fghjkl"`

10. `Win+Shift+S` to take a screeshot using Snipping Tool and then run the program.
11. The output is then printed onto the console
