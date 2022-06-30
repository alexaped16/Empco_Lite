from app import app, db
from flask import redirect, render_template, url_for, flash


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',  title=title)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/product_line')
def product_line():
    return render_template('product_line.html')


@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/sister_companies')
def sister_companies():
    return render_template('sister_companies.html')

@app.route('/akt')
def akt():
    return render_template('akt.html')



# PRODUCT LINE 

@app.route('/lighting_types/airport_lighting')
def airport_lighting():
    return render_template('/lighting_types/airport_lighting.html')

@app.route('/highway_construction_lighting')
def highway_construction_lighting():
    return render_template('highway_construction_lighting.html')

@app.route('/marine_lighting')
def marine_lighting():
    return render_template('marine_lighting.html')

@app.route('/rairoad_lighting')
def railroad_lighting():
    return render_template('rairoad_lighting.html')



# AIRPORT PRODUCTS 

@app.route('/airport/model_630')
def model_630():
    return render_template('/airport/model_630.html')