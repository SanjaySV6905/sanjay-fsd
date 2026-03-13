from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# File to store recipes
RECIPES_FILE = 'recipes.json'

def load_recipes():
    if os.path.exists(RECIPES_FILE):
        with open(RECIPES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_recipes(recipes):
    with open(RECIPES_FILE, 'w') as f:
        json.dump(recipes, f, indent=2)

@app.route('/')
def home():
    recipes = load_recipes()
    return render_template('home.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe = {
            'name': request.form['name'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            'time': request.form['time'],
            'ratings': [],
            'average_rating': 0
        }
        recipes = load_recipes()
        recipes.append(recipe)
        save_recipes(recipes)
        return redirect(url_for('home'))
    return render_template('add_recipe.html')

@app.route('/rate/<int:recipe_id>', methods=['POST'])
def rate_recipe(recipe_id):
    rating = int(request.form['rating'])
    recipes = load_recipes()
    
    if 0 <= recipe_id < len(recipes):
        if 'ratings' not in recipes[recipe_id]:
            recipes[recipe_id]['ratings'] = []
        
        recipes[recipe_id]['ratings'].append(rating)
        recipes[recipe_id]['average_rating'] = round(sum(recipes[recipe_id]['ratings']) / len(recipes[recipe_id]['ratings']), 1)
        save_recipes(recipes)
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
