from flask import request, jsonify
from app import app
from app.scraper import get_external_tor_ips
import sqlite3

DB_NAME = 'excluded_ips.db'

@app.route('/api/ips', methods=['GET'])
def get_ips():
    # Getting external IPs
    all_ips = get_external_tor_ips()
    
    # Excluding IPs from the database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT ip FROM excluded_ips')
    excluded_ips = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Removing excluded IPs
    final_ips = list(set(all_ips) - set(excluded_ips))
    
    return jsonify(final_ips), 200

@app.route('/api/exclude-ip', methods=['POST'])
def exclude_ip():
    ip = request.json.get('ip')
    if ip:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO excluded_ips (ip) VALUES (?)', (ip,))
            conn.commit()
            conn.close()
            return jsonify({'message': 'IP excluded successfully'}), 200
        except sqlite3.IntegrityError:
            return jsonify({'error': 'IP already excluded'}), 400
    
    return jsonify({'error': 'Invalid IP'}), 400
