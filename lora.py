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
 
 
while(1):
    
    print ("Aguardando informacoes do LoRa...")
    
    #Aguarda a string na serial
    x = ser.readline()
    
    #Mostra na tela a string recebida
    print ("Recebido: ",x.decode('utf-8'))
    
    
    time.sleep(0.1)