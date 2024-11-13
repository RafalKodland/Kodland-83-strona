from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Witaj Świecie!</h1><a href='/test'>Przejdź do strony testowej</a>"

@app.route("/test")
def test():
    return f"<p>Strona testowa. Losowa liczba: {randint(1, 100)}</p><a href='/'>Cofnij się</a>"

app.run(debug=True)