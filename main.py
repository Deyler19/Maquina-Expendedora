import csv
import pandas as pd
import re


lett_patter = '^[A-Za-z]+$'
num_patter = '^[0-9]+$'

lista_seleccion = []

def escribir(li):
    li = []
    with open('DB_CSV.csv', newline='',mode= 'w') as db:
        escritura = csv.writer(li)


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
        lista_seleccion.append(introducir_datos)
        break

with open('DB_CSV.csv', newline='',mode= 'r+') as db:
        lector = csv.reader(db , delimiter=',')
        linea  = lector.line_num
        escritor = csv.writer(db,delimiter=",")
        for row in lector:
            if introducir_datos in row[0]:
                stock = int(row[3])

                if stock <= 0:
                    print("No hay Articulo Disponible, Seleccione Otro")
                    break
                
                else: 

                    print(f' Producto seleccionado cuesta {row[2]} y usted cuenta con {introducir_dinero}')
                    if int(introducir_dinero) >= int(row[2]):
                            lista_seleccion.append(row[1])
                            lista_seleccion.append(row[2])
                            remain = stock - 1
                            lista_seleccion.append(remain) 
                            devuelta=int(introducir_dinero)-int(row[2])
                            linea_select = lector.line_num

                            print(linea_select)
                            print (f'su producto {row [1]} esta disponible, su cambio es {devuelta} ')

                            break
                    elif int(introducir_dinero) < int(row[2]):
                        print ("echa ma' cualto maldito pobre")
                        break
            
        else:
                print ("Producto no encontrado, elige bien maldito animal")
print(lista_seleccion,)























