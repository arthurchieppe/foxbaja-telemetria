import sqlite3
import os
import sys

if 'foxbaja_telemetria.db' in os.listdir():
    print("\nERRO: base de dados ja existe, apague manualmente para continuar\n")
    sys.exit()

conn = sqlite3.connect('foxbaja_telemetria.db') 
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS telemetria (
        id INT PRIMARY KEY,
        velocidade INT NOT NULL,
        temperatura INT NOT NULL,
        rotacao INT NOT NULL,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

conn.commit()