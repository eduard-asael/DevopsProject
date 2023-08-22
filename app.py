from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("Portfolio.html")


@app.route("/elements")
def elements():
    return render_template("elements.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


app.run(debug=True, port=3000)
