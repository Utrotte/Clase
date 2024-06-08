import os
os.system("cls")

import csv
import json
pequeño=[]
mediano=[]
gran=[]

with open("listadoRutEmpresa.csv","r") as archivo_csv:
    lector_csv=csv.DictReader(archivo_csv)

    for fila in lector_csv:
        rut=fila["rut"]
        nombre=fila["nombre"]
        ventas=int(fila["ventas"])

        if ventas <= 100000000:
            clas="Pequeño Contribuyente"
            pequeño.append({
                "rut":rut,
                "nombre":nombre,
                "ventas":ventas
            })
        elif ventas >= 100000001 and ventas <= 200000000:
            clas="Mediano Contribuyente"
            mediano.append({
                "rut":rut,
                "nombre":nombre,
                "ventas":ventas
            })
        elif ventas >= 200000001:
            clas="Gran Contribuyente"
            gran.append({
                "rut":rut,
                "nombre":nombre,
                "ventas":ventas
            })

        print(f"{rut} {nombre} {ventas}")

with open("","w") as archivo_json:
     json.dump(pequeño, archivo_json, indent=1)