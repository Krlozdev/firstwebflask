#Ecommerce de frutas

lista_compras = []

precios_del_dia = {

    "manzana": 3.50,
    "pera": 5.00,
    "platano": 2.00,
    "uva": 6.00,
    "naranja": 3.00,
    "mango": 4.50,
    "papaya": 3.00,
    "mandarina": 3.50


}

print("|||||Bienvenido a la Fruteria Markos Light||||""\n")

print("Frutas frascas del dia : manzana, pera, platano, uva, naranja, mango, papaya""\n")
count = 0
uni_maxi = 6
while True:

    print("Lista de Compras")
    print("1: Agregar una fruta del dia ")
    print("2: Mostrar la lista de compras")
    print("3: Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':

        while count < uni_maxi:
            articulo = input("Ingrese el nombre de la fruta desea agregar : ")
            lista_compras.append(articulo)




    elif opcion == '2':

        print("Lista de Compras: ")
        print(",".join(lista_compras))

        while True:

            print("1: Eliminar un artículo")
            print("2: Ver precio individual")
            print("3: Ver precio total")
            print("4: Volver al menu principal")
            print("5: Salir")

            option = input("ingrese su opcion: ")

            if option == '1':

                art_rmv = input("Ingrese el nombre del artículo a eliminar: ")

                if art_rmv in lista_compras:

                    lista_compras.remove(art_rmv)
                    print("El artículo {} ha sido eliminado de la lista de compras".format(art_rmv))
                    print("Lista de Compras: ")
                    print("\n"",".join(lista_compras))

                else:
                    break

            elif option == '2':

                for articulo in lista_compras:
                    if articulo in precios_del_dia:

                       print("El precio de {} es de ${}".format(articulo, precios_del_dia[articulo]))

            elif option == 3:

                print("El precio total de su compra es de ${}".format(sum(precios_del_dia[articulo] for articulo in lista_compras if articulo in precios_del_dia)))


    elif opcion == '3':

        print("Saliendo del programa...")

        break

    else:

        print("Opción inválida. Por favor, intente de nuevo.")


