from . import translator
from flask import Flask, render_template

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/e2f/<text>')
def e2f(text):
    english = translator.english_to_french(text)
    return english

@app.route('/f2e/<text>')
def f2e(text):
    french = translator.french_to_english(text)
    return french