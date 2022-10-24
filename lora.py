#Programa: Comunicacao Arduino e Raspberry Pi com LoRa
#Autor: Arduino e Cia
 
import RPi.GPIO as GPIO
import time
import serial
 
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
            pass # Salva no banco de dados
    except:
        pass
    time.sleep(0.1)