from flask import Flask
import sqlite3

app = Flask(__name__)

# Creating the database table for excluded IPs if not exists
DB_NAME = 'excluded_ips.db'
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS excluded_ips (
    id INTEGER PRIMARY KEY,
    ip TEXT NOT NULL UNIQUE
)
''')
conn.commit()
conn.close()

from app import routes
