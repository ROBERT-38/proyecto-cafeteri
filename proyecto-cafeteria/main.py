import os
import globales
import ventas
os.system("cls")




def menu_general():
   while True:
        os.system("cls")
        print("1.precargar ventas")
        print("2.crear ventas")
        print("3.reportar sueldos")
        print("4.estadisticas")
        print("5.salir")

        opcion = globales.seleccionar_opcion(5)

        if opcion == 1:
           print("precargar ventas")
           ventas.precargar_ventas()
        elif opcion == 2:
            print("crear")
        elif opcion == 3:
            print("reporte de sueldos")
        elif opcion == 4:
            print("estadisticas")
        elif opcion == 5:
            print("salir")
            return
        input()


if __name__ == "__main__":
    menu_general()