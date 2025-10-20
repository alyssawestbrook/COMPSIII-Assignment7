import sqlite3

connection = sqlite3.connect('python_pulse.db')
cursor = connection.cursor()

# Drop tables if they already exist to prevent duplicates
cursor.execute("DROP TABLE IF EXISTS user_workout")
cursor.execute("DROP TABLE IF EXISTS workouts")
cursor.execute("DROP TABLE IF EXISTS goals")
cursor.execute("DROP TABLE IF EXISTS profiles")
cursor.execute("DROP TABLE IF EXISTS users")

# Create users table with user_id, username, password, email
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Sample user data
users_data = [
    ('john_doe', 'password123', 'john_doe@gmail.com'),
    ('jane_smith', 'mypassword', 'jane@gmail.com'),
    ('alice_jones', 'alicepassword', 'ajones@yahoo.com'),
    ('bob_brown', 'bobpassword', 'bobby@yahoo.com'),
    ('rebecca_charles', 'rebeccapassword', 'becky123@gmail.com')
]

# Insert sample users into users table
cursor.executemany("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", users_data)

# Create profiles table with one-to-one relationship to users
cursor.execute("""
CREATE TABLE profiles (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    height INTEGER,
    weight INTEGER,
    age INTEGER,
    notes TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

# Sample profile data
profiles_data = [
    (1, 180, 75, 28, 'Loves hiking and outdoor activities.'),
    (2, 165, 60, 25, 'Enjoys painting and art.'),
    (3, 170, 65, 30, 'Passionate about technology and coding.'),
    (4, 175, 80, 22, 'Avid reader and writer.'),
    (5, 160, 50, 27, 'Fitness enthusiast and gym lover.')
]

# Insert sample profiles into profiles table
cursor.executemany("INSERT INTO profiles (user_id, height, weight, age, notes) VALUES (?, ?, ?, ?, ?)", profiles_data)

# Create goals table with one-to-many relationship to users
cursor.execute("""
CREATE TABLE goals (
    goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    target_value INTEGER,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

# Sample goal data
goals_data = [
    ('Run 5km', 5, 1),
    ('Lose 10kg', 10, 2),
    ('Lift 100kg 3x', 100, 3),
    ('Meditate daily', 1, 5),
    ('Cycle 100km', 100, 4),
    ('Complete a marathon', 42, 5),
    ('Run 5 km', 5, 5)
]

# Insert sample goals into goals table
cursor.executemany("INSERT INTO goals (name, target_value, user_id) VALUES (?, ?, ?)", goals_data)

# Create workouts table
cursor.execute("""
CREATE TABLE workouts (
    workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    duration INTEGER
)
""")

# Sample workout data
workouts_data = [
    ('Morning Yoga', 'A refreshing morning yoga session.', 30),
    ('HIIT Workout', 'High-Intensity Interval Training.', 45),
    ('Weightlifting', 'Full body weightlifting session.', 60),
    ('Cycling', 'Outdoor cycling for endurance.', 120),
    ('Meditation', 'Guided meditation for relaxation.', 15)
]

# Insert sample workouts into workouts table
cursor.executemany("INSERT INTO workouts (name, description, duration) VALUES (?, ?, ?)", workouts_data)

# Create many-to-many relationship between users and workouts
cursor.execute("""
CREATE TABLE user_workout (
    user_id INTEGER,
    workout_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(workout_id) REFERENCES workouts(workout_id)
)
""")

# Sample user_workout data
user_workout_data = [
    (1, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (5, 2)
]

# Insert sample user_workout into user_workout table
cursor.executemany("INSERT INTO user_workout (user_id, workout_id) VALUES (?, ?)", user_workout_data)

# Commit all changes to the database
connection.commit()

# Close the connection
connection.close()