from app import app, db
from flask import redirect, render_template, url_for, flash


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',  title=title)


@app.route('/about')
def my_portfolio():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')



# PRODUCT LINE 

@app.route('/lighting_types/airport_lighting')
def airport_lighting():
    return render_template('/lighting_types/airport_lighting.html')

@app.route('/highway_construction_lighting')
def highway_construction_lighting():
    return render_template('highway_construction_lighting.html')

@app.route('/marine_lighting')
def marine_lighting():
    return render_template('maring_lighting.html')

@app.route('/rairoad_lighting')
def railroad_lighting():
    return render_template('rairoad_lighting.html')



# AIRPORT PRODUCTS 

@app.route('/airport/model_630')
def model_630():
    return render_template('/airport/model_630.html')