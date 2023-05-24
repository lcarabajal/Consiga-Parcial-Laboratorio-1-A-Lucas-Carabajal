# Administración de Insumos de una Tienda de Mascotas.
# Se solicita desarrollar un programa para administrar los insumos de una
# tienda de mascotas. Para ello, se dispone de un archivo CSV con el
# siguiente formato:

# ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS
# 1,Alimento para perros,Pedigree,$12.99,Sabor delicioso~Nutrición
# equilibrada~Contiene vitaminas y minerales


# El programa debe ofrecer un menú con las siguientes opciones:
# 1. Cargar datos desde archivo: Esta opción permite cargar el contenido
# del archivo "Insumos.csv" en una colección, teniendo en cuenta que
# las características de los insumos deben estar en un tipo de colección
# integrada.
# 2. Listar cantidad por marca: Muestra todas las marcas y la cantidad
# de insumos correspondientes a cada una.
# 3. Listar insumos por marca: Muestra, para cada marca, el nombre y
# precio de los insumos correspondientes.
# 4. Buscar insumo por característica: El usuario ingresa una 
# característica (por ejemplo, "Sin Granos") y se listarán todos los
# insumos que poseen dicha característica.
# 5. Listar insumos ordenados: Muestra el ID, descripción, precio, marca
# y la primera característica de todos los productos, ordenados por
# marca de forma ascendente (A-Z) y, ante marcas iguales, por precio
# descendente.
# 6. Realizar compras: Permite realizar compras de productos. El usuario
# ingresa una marca y se muestran todos los productos disponibles de
# esa marca. Luego, el usuario elige un producto y la cantidad deseada.
# Esta acción se repite hasta que el usuario decida finalizar la compra.
# Al finalizar, se muestra el total de la compra y se genera un archivo
# TXT con la factura de la compra, incluyendo cantidad, producto,
# subtotal y el total de la compra.
# 7. Guardar en formato JSON: Genera un archivo JSON con todos los
# productos cuyo nombre contiene la palabra "Alimento".
# 8. Leer desde formato JSON: Permite mostrar un listado de los insumos
# guardados en el archivo JSON generado en la opción anterior.
# 9. Actualizar precios: Aplica un aumento del 8.4% a todos los
# productos, utilizando la función map. Los productos actualizados se
# guardan en el archivo "Insumos.csv".
# 10. Salir del programa
# 11. Agregar producto a la lista
# 12. 
# Nota: Utilizar las funciones filter y reduce cuando sea necesario.


# 1.El programa deberá permitir agregar un nuevo producto a la lista (mediante una
# nueva opción de menú).
# Al momento de ingresar la marca del producto se deberá mostrar por pantalla un
# listado con todas las marcas disponibles. Las mismas serán cargadas al programa
# desde el archivo marcas.txt.
# En cuanto a las características, se podrán agregar un mínimo de una y un máximo
# de 3.
# 2. Agregar una opción para guardar todos los datos actualizados (incluyendo las altas).
# El usuario elegirá el tipo de formato de exportación: csv o json.

#Lucas Damian Carabajal Silva
#DIV-A LABORATORIO

#En esta seccion declaro y import librerias de otros lados para que las funciones puedan funcionar sin errores
#--------------------------------------
import os 
from funciones_parcial import * 
        
flag_lista_cargada = False
flag_json_creado = False
#---------------------------------------

while True: #while True para que el codigo sea constante y no se ejecute una sola vez
    os.system("cls") #el os.system("cls") para que la pantalla de la terminal se limpie y no quede todo registrado
    
    match(menu_veterinario()): #el match que obtiene la opcion que el usuario eligio (la funcion retorna opcion)
        
        # Todos los casos posibles
         
        case "1":
          flag_lista_cargada = True #cambio el flag para que el usuario no rompa todo al intentar hacer otra opcion que necesite la lista_insumos (osea todas)
          lista_insumos = cargarArchivos() #carga los datos a la lista_insumos desde insumos
                           
        case "2":
            if flag_lista_cargada:
                mostrarInsumoMarcas(lista_insumos,'marca')
            else:
                print("No se puede realizar la accion sin primero cargar la lista (vaya a opción 1)")    
                
        case "3":
            if flag_lista_cargada:
                mostrarPreciosMarcas(lista_insumos,'marca')
            else:
                print("No se puede realizar la accion sin primero cargar la lista (vaya a opción 1)")    
        
        case "4":
            if flag_lista_cargada:
                encontrarCaracteristica(lista_insumos,'descripcion')
            else:
                print("No se puede realizar la accion sin primero cargar la lista (vaya a opción 1)")    
        
        case "5":    
            if flag_lista_cargada:
                mostrarOrdenado(ordenarMayor(lista_insumos))
            else:
                print("No se puede realizar la accion sin primero cargar la lista (vaya a opción 1)")   
                
        case "6":
            if flag_lista_cargada:
                realizarCompra(lista_insumos)
            else:
                print("No se puede realizar la accion sin primero cargar la lista (vaya a opción 1)")   
                
        case "7":
            flag_json_creado = True
            if flag_lista_cargada:
                encontrarNombre(lista_insumos)
            else:
                print("No se puede realizar la accion sin primero cargar la lista (vaya a opción 1)")   
        
        case "8":
            if flag_lista_cargada and flag_json_creado:
                mostrarJson()
            else:
                print("No se puede realizar la accion sin primero cargar la lista (vaya a opción 1) o Archivo json no esta creado (vaya a opcion 7)")   
           
        case "9":
            if flag_lista_cargada:
                aumentoPrecio(lista_insumos)
            else:
                print("No se puede realizar la accion sin primero cargar la lista (vaya a opción 1) o Archivo json no esta creado (vaya a opcion 7)")
                
        case "10":
            salir = input("Seguro que desea salir ? s/n: ")
            if salir == "s":
                break
        
        case "11":
            if flag_lista_cargada:
                agregarInsumo(lista_insumos)
            else:
                print("no se puede agregar cosas en lista sin cargar la lista primero (opcion 1)")
        case "12":
            if flag_lista_cargada:
                guardaElementos(lista_insumos)
            else:
                print("no se puede agregar cosas en lista sin cargar la lista primero (opcion 1)")
        #Esta opcion es por si el usuario pone cualquier cosa
        case _default:
            print("esa opcion no existe!")
    
    os.system("pause")#Esto hace que el codigo se ejecute pero que espere hasta el siguente ingreso del usuario, para poder ver las opciones y sus resultados
#----------------------------------------------------------