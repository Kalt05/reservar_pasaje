# app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/reservar', methods=['POST'])
def reservar():
    data = request.json
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO reservaciones (nombre, ci, destino, municipio, omnibus, fecha, telefono)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data['nombre'], data['ci'], data['destino'], data['municipio'], 
          data['omnibus'], data['fecha'], data['telefono']))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Reservación guardada"})

if __name__ == '__main__':
    app.run()
