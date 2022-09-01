import sqlite3
import os
import sys
import random
import time

if 'foxbaja_telemetria.db' not in os.listdir():
    print("\nERRO: base de dados nao existe\n")
    sys.exit()


with sqlite3.connect('foxbaja_telemetria.db') as conn:
    c = conn.cursor()

    for i in range(600):
        velocidade = random.randint(20,30)
        temperatura = random.randint(60,90)
        rotacao = random.randint(2000,3000)
        c.execute(f"""
        INSERT INTO telemetria 
        (velocidade, temperatura, rotacao)
        VALUES
        ({velocidade}, {temperatura}, {rotacao})
        """)

        conn.commit()
        print(f"Velocidade: {velocidade} - Temperatura: {temperatura} - Rotacao: {rotacao}\n")
        time.sleep(1)
