"""
Student Feedback System - Database Module (SQLite)
"""
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'feedback.db')


def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database and create the feedback table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            feedback TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("[✓] Database initialized successfully.")


def insert_feedback(name, feedback):
    """Insert a new feedback entry into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO feedback (name, feedback, created_at) VALUES (?, ?, ?)',
        (name, feedback, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    )
    conn.commit()
    conn.close()


def get_all_feedback():
    """Retrieve all feedback entries, ordered by most recent first."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM feedback ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows
