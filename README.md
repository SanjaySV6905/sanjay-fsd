# Recipe Sharing Platform

A simple web app where users can share recipes, view others recipes, and rate them out of 10 stars.
Built as a beginner project using Flask and MySQL.

---

## Project Structure

```
project/
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   ├── home.html
│   └── add_recipe.html
├── app.py
├── setup_db.sql
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/SanjaySV6905/sanjay-fsd.git
cd sanjay-fsd
```

2. Install Python packages

```
pip install -r requirements.txt
```

3. Set up the MySQL database
   - Open MySQL and run the setup_db.sql file
   - Or paste this in your MySQL terminal:

```
CREATE DATABASE recipe_db;
USE recipe_db;

CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    time VARCHAR(50),
    ingredients TEXT,
    instructions TEXT,
    average_rating FLOAT DEFAULT 0
);

CREATE TABLE ratings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_id INT,
    rating INT,
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
);
```

4. Update your MySQL password in app.py

```python
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="your_password_here",
    database="recipe_db"
)
```

5. Run the app

```
python app.py
```

6. Open your browser and go to http://127.0.0.1:5000

---

## Tools Used

Backend
- Python 3
- Flask 3.0.0
- mysql-connector-python 8.2.0

Frontend
- HTML5
- CSS3
- Bootstrap 5.3 (via CDN)
- jQuery 3.6 (via CDN)

Database
- MySQL
