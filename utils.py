import openai
import os
from dotenv import load_dotenv
import re
import string
import random

load_dotenv()

openai.api_key = os.getenv("API-key")
model_engine = "text-davinci-002"

def generate_response(prompt, model=model_engine, tokenizer=None):
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        message = response.choices[0].text
        message = re.sub('[%s]' % re.escape(string.punctuation), '', message)
        message = message.strip()

        return message

    except Exception as e:
        print(f"OpenAI API error: {e}")
        return f"Sorry, I am unable to process your request at the moment. Please try again later."
