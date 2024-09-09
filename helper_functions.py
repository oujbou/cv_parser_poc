import os
import json
from keys import OPENAI_API_KEY
from openai import OpenAI
import pandas as pd
from prompts import get_prompt
from PyPDF2 import PdfReader


client = OpenAI(api_key=OPENAI_API_KEY)
#OPENAI_API_KEY = os.getenv(OPENAI_API_KEY)
# client = OpenAI(api_key=OPENAI_API_KEY)

# from docx import Document
# from PIL import Image
# import pytesseract

# client = OpenAI(
#     api_key=os.environ['OPENAI_API_KEY'],
# )



def extract_resume_data(text):
    prompt = get_prompt() + text
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user",
             "content": prompt
             }
        ]
    )
    content = response.choices[0].message.content

    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(), columns=["measure", "value"])
    except (json.JSONDecodeError, IndexError):
        pass

    return pd.DataFrame({
        "Entities": ["Name", "email_id", "mob_number", "qualification", "experience", "skills", "certification",
                     "achievement"],
        "value": ["", "", "", "", "", "", "", ""]

    })


def extract_from_pdf(file):
    pdf_text = ""
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()
    return pdf_text


if __name__ == '__main__':
    text = " "
    df = extract_resume_data(text)
    print(df.to_string())
