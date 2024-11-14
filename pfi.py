#Ignacio Castillo - Proyecto Integrador final

""" Crear un menú interactivo utilizando bucles while y condicionales if-elif-else:
● El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos.
● Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados. 

Agregar productos al inventario
Implementar la funcionalidad para agregar productos a una lista:
● Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada.

Mostrar el inventario
Mostrar los productos ingresados:
● Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el
momento. """


import os
is_running = True

# Lista para almacenar los productos y cantidades

productos = []
cantidades = [] 

os.system("cls")
while is_running:

    print("""
--------------------------------------------------
        Bienvenido al sistema de inventario
--------------------------------------------------
          
        (1) Agregar productos al inventario                
        (2) Mostrar productos Registrados          
        (3) Salir              
          
        """)

    opcion = input('Ingresa la opcion deseada y presione Enter: ')
    
    if opcion == '1':
        while True:
            producto = input("Ingrese el nombre del producto: ")    
            ###Bucle validador    
            if producto.isalpha():
                break
            else: 
                print("Ingrese el nombre del producto por favor (Solo texto)")

        print(f'{producto} Agregado!')
        productos.append(producto)
        

        ###Bucle validador         
        while True: 
            cantidad = input("Ingrese la cantidad del producto: ")
            if cantidad.isdigit() or cantidad[0] == '-' and cantidad[1::].isdigit(): # el primer caracter sea un '-' y el resto todos digitos.
                cantidad = int(cantidad) 
                if cantidad > 0:
                    break
                else:
                    print("La cantidad no puede ser menor o igual a 0. Intentá de nuevo.")
            else:
                print('El dato debe ser numérico...')
        print("Ingresaste una cantidad válida:", cantidad) 
        cantidades.append(cantidad)
    

    elif opcion == '2':
        max = len(productos)

        for i in range(0, max):
            print(productos[i], cantidades[i])

    elif opcion == '3': 
        is_running = False
        print('Gracias por usar el programa. Adios!')

    else: 
        print("La opcion ingresada es incorrecta, intentelo nuevamente...")


    
