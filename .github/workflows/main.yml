from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'tennis_tournament.db'

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create table for current tournament results
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS current_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player1 TEXT NOT NULL,
            player2 TEXT NOT NULL,
            score TEXT NOT NULL,
            winner TEXT NOT NULL
        )
    ''')
    
    # Create table for future matches
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS future_matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player1 TEXT NOT NULL,
            player2 TEXT NOT NULL,
            match_date TEXT NOT NULL,
            match_time TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Render the main page with data from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Fetch data from current_results table
    cursor.execute('SELECT * FROM current_results')
    current_results = cursor.fetchall()
    
    # Fetch data from future_matches table
    cursor.execute('SELECT * FROM future_matches')
    future_matches = cursor.fetchall()
    
    conn.close()
    
    return render_template('index.html', current_results=current_results, future_matches=future_matches)

if __name__ == '__main__':
    # Initialize the database before starting the app
    init_db()
    app.run(debug=True)
