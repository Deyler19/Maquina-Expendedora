import csv
import pandas as pd
import re


lett_patter = '^[A-Za-z]+$'
num_patter = '^[0-9]+$'



print("productos disponibles")

producto= pd.read_csv('DB_CSV.csv')
producto= producto.to_string(index=False)
print (producto)

while True:
    introducir_dinero=input("introduzca dinero ")
    if re.fullmatch(num_patter, (introducir_dinero)):
        break
while True:
    introducir_datos=input("que desea comprar?")
    if re.fullmatch(num_patter, introducir_datos):
        break

with open('DB_CSV.csv', newline='',mode= 'r+') as db:
        lector = csv.reader(db , delimiter=',')
        for row in lector:
            if introducir_datos in row[0]:
                print(f' Producto seleccionado cuesta {row[2]} y usted cuenta con {introducir_dinero}')
                if int(introducir_dinero) >= int(row[2]):
                    devuelta=int(introducir_dinero)-int(row[2])
                    print (f'su producto {row [1]} esta disponible, su cambio es {devuelta} ')
                    break
                elif int(introducir_dinero) < int(row[2]):
                        print ("echa ma' cualto maldito pobre")
                        break
                else:
                    print ("Producto no encontrado")
























