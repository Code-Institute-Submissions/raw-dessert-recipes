import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://admin:animals1234@ds233541.mlab.com:33541/raw_cookbook'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/about')
def about():
    return render_template("about.html")
 
@app.route('/recipes')
def recipes():
    return render_template("recipes.html")
 
@app.route('/addrecipes')
def addrecipes():
    return render_template("addrecipes.html") 

@app.route('/contact')
def contact():
    return render_template("contact.html")  
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    #If debug=True not included, changes will not render in the browser.
    debug=True)