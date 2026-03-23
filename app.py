from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "recipe123"  # needed to use session

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
    cursor.execute("""
        SELECT recipes.*, COUNT(ratings.id) as vote_count
        FROM recipes
        LEFT JOIN ratings ON recipes.id = ratings.recipe_id
        GROUP BY recipes.id
    """)
    recipes = cursor.fetchall()
    # pass list of already-rated recipe ids from session
    rated = session.get('rated', [])
    return render_template('home.html', recipes=recipes, rated=rated)

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
    # Check if user already rated this recipe
    rated = session.get('rated', [])
    if id in rated:
        return redirect(url_for('home'))

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

    # Save this recipe id in session so user can't rate again
    rated.append(id)
    session['rated'] = rated

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
