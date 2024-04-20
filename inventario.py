productos = {}

def menu():
    while(True):
        menuPrincipal = "MENU DE OPCIONES\n"
        menuPrincipal+= "1. Registrar un producto\n"
        menuPrincipal+= "2. Ver todos los productos\n"
        menuPrincipal+= "3. Consultar un producto\n"
        menuPrincipal+= "4. Salir\n\n"
        print(menuPrincipal)
        opcion = int(input("Ingrese una opción del menú: "))
        if opcion == 1:
            registrar()
        elif opcion == 2:
            vertodos()
        elif opcion == 3:
            productoCons = consultarProducto()
            print(productoCons)
        elif opcion == 4:
            print("Saliendo del programa...")
            break

def registrar():
    while(True):
        producto = []
        print("\nModulo de registro de productos")
        codigo = input("Ingrese el codigo del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        costoProducto = float(input("Ingrese el valor del producto: "))
        inventario = int(input("Ingrese la cantidad de productos en el inventario: "))
        producto.append(descripcion)
        producto.append(costoProducto)
        producto.append(inventario)
        productos[codigo] = producto
        valor = input("¿Desea agregar otro producto? [Si] [No]").lower()
        if valor == "si":
            continue
        else:
            menu()

def consultarProducto():
    productoConsultado = []
    print("Modulo de consulta de productos")
    codigo = input("Ingrese el codigo del producto a buscar: ")
    try:
        productoConsultado = productos[codigo]
    except:
        print("El producto no existe en la base de datos")
    
    if not(len(productoConsultado) == 0):
        return productoConsultado

def vertodos():
    print(productos)

if __name__ == "__main__":
    menu()