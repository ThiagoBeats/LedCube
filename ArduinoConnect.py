# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:49:37 2023

@author: thiago
"""
"""
import serial

ser = serial.Serial('COM6', 9600)  # Substitua 'COMx' pela porta serial do seu Arduino

while True:
    data = ser.readline() #LÊ O SERIAL
    print(data.decode('utf-8').strip())
    ser.write(b'A')  # Envia o comando 'A' para o Arduino
    ser.close()


"""

camadas = []
colunas = []

#Inicia o vetor de camadas preenchendo com zeros
for i in range(0, 6):
    camadas.append([])
    
# #Inicia o vetor de colunas preenchendo com zeros
# for i in range(0, QntColunas):
#     colunas.append([])
    
for i in range(0, 6):
    for j in range(i*6, 216, 36):
        camadas[i].append(j)
        camadas[i].append(j+1)
        camadas[i].append(j+2)
        camadas[i].append(j+3)
        camadas[i].append(j+4)
        camadas[i].append(j+5)

    for r in camadas[i]:
        colunas.append([r, r+6, r+12, r+18, r+24, r+30])

del colunas[36:]


programa = []

with open('Programa.txt', 'r') as arquivo:
    # Lê o conteúdo do arquivo
    conteudo = arquivo.read()

# Agora você pode trabalhar com o conteúdo
for i in range(0, len(conteudo)):
    if conteudo[i] != ',':
        programa.append(conteudo[i])
        
Qntframes = int(len(programa)/36)

subarrays = []

for i in range(0, len(programa), 36):
    subarray = programa[i:i + 36]
    subarrays.append(subarray)
   
print(programa)

