import sqlite3

# Function to create the 'Members' table
def create_members_table():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Function to create the 'WorkoutSessions' table
def create_workouts_table():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WorkoutSessions (
            session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            date TEXT NOT NULL,
            duration_minutes INTEGER NOT NULL,
            calories_burned INTEGER NOT NULL,
            FOREIGN KEY (member_id) REFERENCES Members (member_id)
        )
    ''')

    conn.commit()
    conn.close()

# Function to add a member
def add_member(id, name, age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Members (member_id, name, age)
            VALUES (?, ?, ?)
        ''', (id, name, age))
        
        conn.commit()
        print("Member added successfully!")
    
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    
    finally:
        if conn:
            conn.close()

# Function to add a workout session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
            VALUES (?, ?, ?, ?)
        ''', (member_id, date, duration_minutes, calories_burned))
        
        conn.commit()
        print("Workout session added successfully!")
    
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    
    finally:
        if conn:
            conn.close()

# Function to delete a workout session
def delete_workout_session(session_id):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            DELETE FROM WorkoutSessions WHERE session_id = ?
        ''', (session_id,))
        
        if cursor.rowcount == 0:
            raise ValueError(f"No workout session found with session_id: {session_id}")
        
        conn.commit()
        print("Workout session deleted successfully!")
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    
    finally:
        if conn:
            conn.close()

# Create the tables
create_members_table()
create_workouts_table()

# Example usage
add_member(101, 'John Doe', 30)
add_workout_session(101, '2025-02-20', 60, 500)
delete_workout_session(1)
