#CODIGO QUE FUNCIONA
import openai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug = True)