import csv
import pandas as pd

print("productos disponibles")

producto= pd.read_csv('DB_CSV.csv')
print (producto)

introducir_dinero=input("introduzca dinero ")

introducir_datos=input("que desea comprar?")

with open('DB_CSV.csv', newline='',mode= 'r+') as db:
    lector = csv.reader(db , delimiter=',')
    for row in lector:
        if introducir_datos in row[0]:
            print(row[1])
            if int(introducir_dinero) >= int(row[1]):
                devuelta=int(introducir_dinero)-int(row[1])
                print (f'su producto {row [0]} esta disponible, su cambio es {devuelta} ')
                break
            else: print("Producto no encontrado")
            break














