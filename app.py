import requests
from utils import generate_response
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        response = get_chatgpt_response(message)
        return render_template('results.html', response=response)
    return render_template('index.html')

def get_chatgpt_response(message):
    user_input = request.form['user_input']
    prompt = f"User: {user_input}\nAI:"
    response = generate_response(prompt)
    return response

if __name__ == '__main__':
    app.run(debug=True)
