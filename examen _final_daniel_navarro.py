# productos =modelo:[marca,pantalla,ram,disco,gb ] 
productos = {
   '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1060'],
    'JjfFHD2': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1060'],
    'JjfFHD3': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1060'],
}
stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'JjfFHD2': [424990, 0],
    'JjfFHD3': [424990, 2],

}

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock.get(modelo, [0, 0])[1]
    print(f"Stock total de {marca.capitalize()}: {total}")

def busqueda_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return
    resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0 and modelo in productos:
            marca = productos[modelo][0]
            resultados.append(f"{marca}-----{modelo}")
    if resultados:
        for item in sorted(resultados):
            print(item)
    else:
        print("No hay noteboock en ese rango de precio.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

def main():
    while True:
        print("\n   MENU PRINCIPAL  ")
        print("(1) Stock marca.")
        print("(2) Busqueda por precio.")
        print("(3) Actualizar precio.")
        print("(4) Salir")
        opcion = input("Ingrese opción: ")
        if opcion == "4":
            print("\nPrograma finalizado.")
            break
        elif opcion == "1":
            marca = input("Ingrese la marca: ")
            stock_marca(marca)
        elif opcion == "2":
            p_min = input("Ingrese el precio mínimo: ")
            p_max = input("Ingrese el precio máximo: ")
            busqueda_precio(p_min, p_max)
        elif opcion == "3":
            modelo = input ("ingrese el modelo:")
            p = input("Ingrese el nu8evo precio:  ")
            if actualizar_precio(modelo, int(p)):
                print(f"Precio del modelo {modelo} actualizado a {p}.")
            else:
                print("Modelo no encontrado.")
        else:
            print("opcion no vqalida, intente nuevamente.")

if __name__ == "__main__":
    main()
 
