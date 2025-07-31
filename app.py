from flask import Flask, render_template, request
import requests


app = Flask(__name__)

def fetch_data(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

@app.route('/')
def index():
    return home()


@app.route('/Paises')
def home():
    

    countries = fetch_data("https://restcountries.com/v3.1/all?fields=name,capital,flags")
    countries.sort(key=lambda x: x['name']['common'])
    
    return render_template("home.html", countries=countries)

@app.route('/Paises/<country_name>')
def Paises(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    datos = fetch_data(url)

    if datos:
        return render_template("detalles.html", country=datos[0])
    else:
        return f"No se encontró información para {country_name}"

    


if __name__ == '__main__':
    app.run(debug=True)