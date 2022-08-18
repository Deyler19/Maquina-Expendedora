import csv
import pandas as pd
import re


lett_patter = '^[A-Za-z]+$'
num_patter = '^[0-9]+$'



print("productos disponibles")

producto= pd.read_csv('DB_CSV.csv')
print (producto)

while True:
    introducir_dinero=input("introduzca dinero ")
    if re.fullmatch(num_patter, (introducir_dinero)):
        break
while True:
    introducir_datos=input("que desea comprar?")
    if re.fullmatch(lett_patter, introducir_datos):
        break

with open('DB_CSV.csv', newline='',mode= 'r+') as db:
    lector = csv.reader(db , delimiter=',')
    for row in lector:
        if introducir_datos in row[0]:
            print(f' Producto seleccionado cuesta {row[1]} y usted cuenta con {introducir_dinero}')
            if int(introducir_dinero) >= int(row[1]):
                devuelta=int(introducir_dinero)-int(row[1])
                print (f'su producto {row [0]} esta disponible, su cambio es {devuelta} ')
            elif int(introducir_dinero) < int(row[1]):
                    print ("echa ma' cualto maldito pobre")
                    break
            else: print("Producto no encontrado")
            break














