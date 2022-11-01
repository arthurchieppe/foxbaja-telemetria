#Programa: Comunicacao Arduino e Raspberry Pi com LoRa
#Autor: Arduino e Cia
 
import RPi.GPIO as GPIO
import time
import serial
import sqlite3
import os
import sys
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Configura a serial e a velocidade de transmissao
ser = serial.Serial('/dev/serial0', 115200)
time.sleep(3) 

def checksum(data):
    filtered = data.split("/")
    print(f"edir {filtered[0]}")
    checksum = 0
    for i in range(0, len(filtered[0])):
        checksum += ord(filtered[0][i])
    return checksum

def save_df(data):
    if 'foxbaja_telemetria.db' not in os.listdir():
        print("\nERRO: base de dados nao existe\n")
        sys.exit()

    with sqlite3.connect('foxbaja_telemetria.db') as conn:
        c = conn.cursor()
        try:
            data = data.split(",")
            
            rotacao = int(data[0])
            velocidade = int(data[1])
            freio = int(data[2])   
            combustivel = int(data[3])
            temperatura = int(data[4])
            
            c.execute(f"""
            INSERT INTO telemetria 
            (rotacao, velocidade, freio, combustivel, temperatura)
            VALUES
            ({rotacao}, {velocidade}, {freio}, {combustivel}, {temperatura})
            """)
            conn.commit()
        except:
            pass
        
 
while(1):
    
    print ("Aguardando informacoes do LoRa...")
    
    #Aguarda a string na serial
    x = ser.readline()
    msg = x.decode('utf-8')
    try:
        splitted = msg.split("/")
        #Mostra na tela a string recebida
        print("Recebido: ", msg)
        checksum_result = checksum(splitted[0])
        if checksum_result == int(splitted[1]):
            save_df(splitted[0])
    except:
        pass
    time.sleep(0.2)