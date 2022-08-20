# Importing all of the dependencies
from flask import Flask, render_template
import os
from products import products

# This is the port number, defaults to 5000 if no environment variable is found
port = int(os.getenv('PORT', 5000))

# Creating the app, it will be referenced in all of the routes and when starting the server
app = Flask(__name__)

# The homepage
@app.route('/')
def homepage():
    return render_template('index.html')

# The catalogue
@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html')

# The contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# The about page
@app.route('/about')
def about():
    return render_template('about.html')

# The login page
@app.route('/login')
def login():
    return render_template('login.html')

# The product listings
@app.route('/products/<category>')
def productlistings(category):
    try:
        selected_category = products[category.lower()]
    except:
        return render_template('404.html')
    return render_template('products.html', products = selected_category, section = category.capitalize())

# A single product
@app.route('/products/<category>/<product>')
def singleproduct(category, product):
    selected_category = products[category.lower()]
    for item in selected_category:
        if item[0] == product:
            selected_product = item

    return render_template('singleproduct.html', category = category, product = selected_product, section = category.capitalize())

# The 404 page
@app.errorhandler(404)
def errorhandler(e):
    print(e)
    return render_template('404.html')

# Start hosting the server
app.run(host='0.0.0.0', port=port, debug=True)