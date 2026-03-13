# Recipe Sharing Platform 🍳

A simple and beginner-friendly web application for sharing and discovering recipes with an interactive rating system.

## 🌟 Features
- View all recipes on the home page with beautiful card layout
- Search recipes by name, ingredients, or instructions (real-time filtering)
- Add new recipes with name, ingredients, instructions, and cooking time
- Interactive star rating system (rate recipes 1-10 stars)
- View average ratings and total number of ratings
- Responsive design with Bootstrap 5
- Form validation using jQuery
- Clean and intuitive user interface

## 🛠️ Technologies Used
- **Backend:** Flask (Python web framework)
- **Frontend:** HTML5, Bootstrap 5, CSS3
- **JavaScript:** jQuery for DOM manipulation and interactivity
- **Data Storage:** JSON file (recipes.json)

---

## 📥 How to Download and Run in VS Code (Windows)

### Step 1: Clone the Repository
1. Open **Command Prompt** or **PowerShell**
2. Navigate to where you want to save the project:
   ```bash
   cd Desktop
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/SanjaySV6905/sanjay-fsd.git
   ```
4. Navigate into the project folder:
   ```bash
   cd sanjay-fsd
   ```

### Step 2: Open in VS Code
1. Open **VS Code**
2. Click **File** → **Open Folder**
3. Select the `sanjay-fsd` folder
4. Or simply type in terminal:
   ```bash
   code .
   ```

### Step 3: Install Python (if not installed)
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, check **"Add Python to PATH"**
3. Verify installation:
   ```bash
   python --version
   ```

### Step 4: Install Required Packages
1. Open terminal in VS Code (Ctrl + `)
2. Install Flask:
   ```bash
   pip install -r requirements.txt
   ```

### Step 5: Run the Application
1. In VS Code terminal, run:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```
3. To stop the server, press **Ctrl + C** in terminal

---

## 📁 Project Structure
```
sanjay-fsd/
├── static/              # Static files (CSS, JS)
│   ├── style.css       # Custom styling
│   └── script.js       # jQuery code for interactivity
├── templates/           # HTML templates
│   ├── home.html       # Home page with recipe cards
│   └── add_recipe.html # Add recipe form page
├── app.py              # Flask main application file
├── recipes.json        # JSON file storing all recipes
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

---

## 💻 Code Explanation

### 1. **app.py** (Flask Backend)
This is the main Python file that runs the web server.

```python
from flask import Flask, render_template, request, redirect, url_for
```
- Imports Flask framework and necessary functions

```python
app = Flask(__name__)
```
- Creates a Flask application instance

```python
def load_recipes():
    if os.path.exists(RECIPES_FILE):
        with open(RECIPES_FILE, 'r') as f:
            return json.load(f)
    return []
```
- Loads recipes from JSON file
- Returns empty list if file doesn't exist

```python
@app.route('/')
def home():
    recipes = load_recipes()
    return render_template('home.html', recipes=recipes)
```
- Defines the home page route (/)
- Loads all recipes and passes them to home.html template

```python
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
```
- Handles both GET (show form) and POST (submit form) requests
- Creates a new recipe dictionary with form data
- Saves to JSON file and redirects to home page

```python
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
```
- Handles rating submission
- Calculates average rating from all ratings
- Saves updated data and redirects to home

---

### 2. **templates/home.html** (Home Page)
This displays all recipes in card format.

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
```
- Bootstrap navigation bar at the top

```html
<header class="hero-section text-center text-white">
    <h1>Welcome to Recipe Sharing Platform</h1>
    <p>Discover and share amazing recipes</p>
    <a href="/add" class="btn btn-light btn-lg">Add Your Recipe</a>
</header>
```
- Hero section with gradient background
- Call-to-action button to add recipes

```html
<input type="text" id="searchInput" class="form-control" placeholder="🔍 Search recipes...">
```
- Search box for filtering recipes in real-time

```html
{% for recipe in recipes %}
<div class="col-md-6 col-lg-4">
    <div class="card h-100 shadow-sm">
        <div class="card-body">
            <h5 class="card-title">{{ recipe.name }}</h5>
            ...
        </div>
    </div>
</div>
{% endfor %}
```
- Jinja2 template loop to display each recipe as a card
- Bootstrap grid system (responsive columns)

```html
<div class="star-rating">
    <span class="star" data-value="1">★</span>
    <span class="star" data-value="2">★</span>
    ...
</div>
```
- 10 clickable stars for rating
- Each star has a data-value attribute (1-10)

---

### 3. **templates/add_recipe.html** (Add Recipe Page)
Form to add new recipes.

```html
<form id="recipeForm" method="POST">
    <div class="mb-3">
        <label for="name" class="form-label">Recipe Name</label>
        <input type="text" class="form-control" id="name" name="name" required>
    </div>
    ...
</form>
```
- HTML form with Bootstrap styling
- `method="POST"` sends data to server
- `required` attribute for validation

---

### 4. **static/script.js** (JavaScript/jQuery)
Handles interactivity and dynamic behavior.

```javascript
$('#searchInput').on('keyup', function() {
    let searchText = $(this).val().toLowerCase();
    
    $('.card').each(function() {
        let cardText = $(this).text().toLowerCase();
        
        if (cardText.includes(searchText)) {
            $(this).parent().show();
        } else {
            $(this).parent().hide();
        }
    });
});
```
- Real-time search functionality
- Filters recipe cards as you type
- Shows/hides cards based on search match

```javascript
$('.star').on('click', function() {
    let rating = $(this).data('value');
    let form = $(this).closest('.rating-form');
    
    form.find('.rating-value').val(rating);
    form.find('.star').removeClass('selected');
    form.find('.star').each(function() {
        if ($(this).data('value') <= rating) {
            $(this).addClass('selected');
        }
    });
    
    form.submit();
});
```
- Handles star click events
- Sets hidden input value with rating
- Highlights selected stars
- Auto-submits the form

```javascript
$('.star').on('mouseenter', function() {
    let rating = $(this).data('value');
    let form = $(this).closest('.rating-form');
    
    form.find('.star').removeClass('hover');
    form.find('.star').each(function() {
        if ($(this).data('value') <= rating) {
            $(this).addClass('hover');
        }
    });
});
```
- Hover effect for stars
- Shows preview of rating before clicking

---

### 5. **static/style.css** (Custom Styling)

```css
.hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 80px 20px;
}
```
- Purple gradient background for hero section

```css
.card:hover {
    transform: translateY(-5px);
}
```
- Lift effect when hovering over recipe cards

```css
.star {
    font-size: 30px;
    color: #ddd;
    cursor: pointer;
    transition: all 0.2s ease;
}

.star:hover {
    color: #ffd700;
    transform: scale(1.2);
}
```
- Star styling with golden yellow color
- Smooth animations on hover

---

## 🎯 How to Use the Application

1. **View Recipes:** Home page displays all recipes in card format
2. **Search Recipes:** Type in the search box to filter recipes instantly
3. **Add Recipe:** Click "Add Your Recipe" button, fill the form, and submit
4. **Rate Recipe:** Hover over stars and click to rate (1-10 stars)
5. **View Ratings:** Each recipe shows average rating and total ratings

---

## 📝 Key Concepts for Beginners

### Flask Routes
- `@app.route('/')` - Defines URL paths
- Functions below routes handle requests

### Jinja2 Templates
- `{{ variable }}` - Display Python variables in HTML
- `{% for item in list %}` - Loop through data
- `{% if condition %}` - Conditional rendering

### jQuery Selectors
- `$('#id')` - Select by ID
- `$('.class')` - Select by class
- `.on('event', function)` - Event handling

### Bootstrap Classes
- `container` - Centered responsive container
- `row` and `col-*` - Grid system
- `card` - Card component
- `btn` - Button styling

---

## 🚀 Future Enhancements
- User authentication and login
- Recipe categories and tags
- Image upload for recipes
- Comments section
- Favorite/bookmark recipes
- Share recipes on social media

---

## 📄 License
This project is open source and available for educational purposes.

---

## 👨‍💻 Author
Sanjay SV

---

Enjoy cooking and sharing recipes! 🍳⭐
