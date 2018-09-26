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
    '''Routing view to render/call index.html in browser'''
    return render_template("index.html")
    
@app.route('/about')
def about():
    '''Routing view to render/call about.html in browser'''
    return render_template("about.html")
 
@app.route('/get_recipes')
def get_recipes():
    '''Routing view to render/call recipes.html in browser.'''
    return render_template("recipes.html",
    recipes=mongo.db.recipes.find())

@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    the_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories=mongo.db.categories.find()
    return render_template('viewrecipe.html', recipe=the_recipe, categories=all_categories)

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    '''Routing to delete recipe when user selects delete button'''
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    '''Routing to edit recipe when user selects edit button.'''
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=the_recipe)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    '''Routing to include recipe prior data within edit view.'''
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_title':request.form.get['recipe_title'],
        'date_posted':request.form.get['date_posted'],
        'description':request.form.get['description'],
        'ingredients':request.form.get['ingredients'],
        'instructions':request.form.get['instructions'],
        'author_name':request.form.get['author_name']
    })
    return redirect(url_for('get_recipes'))

@app.route('/add_recipe')
def add_recipe():
    '''Routing view to render/call addrecipe.html in browser.'''
    return render_template('addrecipe.html')
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    '''Routing to add new recipe.'''
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/contact')
def contact():
    '''Routing view to render/call contact.html in browser'''
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    #If debug=True not included, changes will not render in the browser.
    debug=True)