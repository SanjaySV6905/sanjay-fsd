from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# --- MySQL Connection ---
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Sanjay@6905",
    database="recipe_db"
)
cursor = db.cursor(dictionary=True)

# --- Home page - show all recipes ---
@app.route('/')
def home():
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    return render_template('home.html', recipes=recipes)

# --- Add recipe page ---
@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        cursor.execute(
            "INSERT INTO recipes (name, time, ingredients, instructions) VALUES (%s, %s, %s, %s)",
            (request.form['name'], request.form['time'], request.form['ingredients'], request.form['instructions'])
        )
        db.commit()
        return redirect(url_for('home'))
    return render_template('add_recipe.html')

# --- Rate a recipe ---
@app.route('/rate/<int:id>', methods=['POST'])
def rate_recipe(id):
    rating = int(request.form['rating'])

    # Insert the new rating
    cursor.execute("INSERT INTO ratings (recipe_id, rating) VALUES (%s, %s)", (id, rating))
    db.commit()

    # Calculate new average
    cursor.execute("SELECT AVG(rating) as avg FROM ratings WHERE recipe_id = %s", (id,))
    result = cursor.fetchone()
    avg = round(result['avg'], 1)

    # Update average in recipes table
    cursor.execute("UPDATE recipes SET average_rating = %s WHERE id = %s", (avg, id))
    db.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
