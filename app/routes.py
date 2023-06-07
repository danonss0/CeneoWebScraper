from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/extract')
def extract():
    return render_template("extract.html")

@app.route('/products')
def extract():
    return render_template("products_list.html")

@app.route('/product')
def extract():
    return render_template("product.html")