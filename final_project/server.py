from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(text_to_translate=None):
    text_to_translate = request.args.get('textToTranslate')
    english = translator.english_to_french(text_to_translate)
    return english

@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    french = translator.french_to_english(text_to_translate)
    return french

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
