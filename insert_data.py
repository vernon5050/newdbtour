import sqlite3

DATABASE = 'tennis_tournament.db'

def populate_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Insert sample data into current_results table
    cursor.executemany('''
        INSERT INTO current_results (player1, player2, score, winner)
        VALUES (?, ?, ?, ?)
    ''', [
        ('Player A', 'Player B', '6-4, 7-5', 'Player A'),
        ('Player C', 'Player D', '6-3, 6-7, 7-6', 'Player C')
    ])
    
    # Insert sample data into future_matches table
    cursor.executemany('''
        INSERT INTO future_matches (player1, player2, match_date, match_time)
        VALUES (?, ?, ?, ?)
    ''', [
        ('Player E', 'Player F', '2025-03-25', '15:00'),
        ('Player G', 'Player H', '2025-03-26', '18:00')
    ])
    
    conn.commit()
    conn.close()

populate_data()
