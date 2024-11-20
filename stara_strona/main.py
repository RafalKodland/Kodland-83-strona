from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", losowa=randint(1, 100))

@app.route("/test")
def test():
    return f"<p>Strona testowa. Losowa liczba: {randint(1, 100)}</p><a href='/'>Cofnij się</a>"

@app.route("/<zmienna>")
def pokazowa(zmienna):
    return f"Zawartość zmiennej: {zmienna}"

@app.route("/<zmienna>/<inna>")
def pokazowa2(zmienna, inna):
    return f"Zawartość zmiennej: {zmienna}<br>Zawartość innej: {inna}"


app.run(debug=True)