import os
import random
import globales
os.system("cls")

def precargar_ventas():
    ventas=globales.leer_archivo_json("ventas.json")
    empleados = globales.leer_archivo_json('empleados.json')

    id_venta = 1 

    for i in range(3):
        empleado=random.choice(empleados)#taremos 1 empleados alateorie¿
        id_venta +=1
        id_empleado = empleado['id_empleado']
        total_venta =  random.randint(30000,70000)
        propina = round(total_venta*0.1)

        nueva_venta = {
            "id_venta": id_venta,
            "id_empleado":id_empleado,
            "total_venta":total_venta,
            "propina":propina

        }

        ventas.append(nueva_venta)
    globales.guardar_archivo_json('ventas.json',ventas)
    input("ventas cargadas")
