from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)

# Load recipes from file
def load_recipes():
    if os.path.exists('recipes.json'):
        return json.load(open('recipes.json'))
    return []

# Save recipes to file
def save_recipes(recipes):
    json.dump(recipes, open('recipes.json', 'w'), indent=2)

# Home page - show all recipes
@app.route('/')
def home():
    return render_template('home.html', recipes=load_recipes())

# Add recipe page
@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe = {
            'name': request.form['name'],
            'time': request.form['time'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            'ratings': [],
            'average_rating': 0
        }
        recipes = load_recipes()
        recipes.append(recipe)
        save_recipes(recipes)
        return redirect(url_for('home'))
    return render_template('add_recipe.html')

# Rate a recipe
@app.route('/rate/<int:id>', methods=['POST'])
def rate_recipe(id):
    recipes = load_recipes()
    recipes[id]['ratings'].append(int(request.form['rating']))
    recipes[id]['average_rating'] = round(sum(recipes[id]['ratings']) / len(recipes[id]['ratings']), 1)
    save_recipes(recipes)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
