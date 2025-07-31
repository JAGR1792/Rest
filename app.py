from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,flags")
    countries = response.json()
    return render_template("home.html", countries=countries)
