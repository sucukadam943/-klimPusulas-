import sqlite3
import streamlit as st

DB_FILE = "database.db"  # SQLite database file (auto-created)

def run_query(query, params=()):
    """Executes SQL queries and returns results for SELECT queries."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            conn.row_factory = sqlite3.Row  # Enables column access by name
            cur = conn.cursor()
            cur.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                return cur.fetchall()  # Fetch results for SELECT queries
            conn.commit()
            return True
    except sqlite3.Error as e:
        return f"Database error: {e}"

def create_tables():
    """Ensures all required tables exist in the database."""
    queries = [
        """CREATE TABLE IF NOT EXISTS proje_fikirleri (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            baslik TEXT NOT NULL,
            aciklama TEXT NOT NULL,
            kategori TEXT NOT NULL,
            kullanici TEXT NOT NULL,
            tarih DATE DEFAULT CURRENT_DATE
        )""",
        """CREATE TABLE IF NOT EXISTS karbon_hesaplamalari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici TEXT NOT NULL,
            ulasim_puani FLOAT NOT NULL,
            enerji_puani FLOAT NOT NULL,
            beslenme_puani FLOAT NOT NULL,
            toplam_puan FLOAT NOT NULL,
            tarih DATE DEFAULT CURRENT_DATE
        )""",
        """CREATE TABLE IF NOT EXISTS forum_yorumlari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            baslik TEXT NOT NULL,
            yorum TEXT NOT NULL,
            kullanici TEXT NOT NULL,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    ]
    try:
        for query in queries:
            run_query(query)
        return True
    except Exception as e:
        print(f"Error creating tables: {e}")
        return False

def test_connection():
    """Test SQLite database connection"""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            st.success("Database connection successful!")
            return True
    except sqlite3.Error as e:
        st.error(f"Database connection error: {e}")
        return False

