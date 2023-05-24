import re #importo las librerias para usarlas creando las funciones.
import os
import json 

multiplicar = lambda numero,multiplo: numero * multiplo

def menu_veterinario()->str:
    print("""
    
    •♦•♦• MENU DE ADMINISTRACION DE INSUMOS •♦•♦•
    
    ------------------------------------------------------------------------
    
    1. Cargar Datos de insumos.csv a una lista.
    2. Muestra todas las marcas y la cantidad
    de insumos correspondientes a cada una.
    3. Muestra para cada marca, el nombre y
    precio de los insumos correspondientes.
    4. Buscar insumo por característica.
    5. Listar insumos ordenados (por marca de forma ascendente)
    6. Realizar compra
    7. Genera un archivo JSON con todos los
    productos cuyo nombre contiene la palabra "Alimento".
    8. Permite mostrar un listado de los insumos
    guardados en el archivo JSON generado en la opción anterior.
    9. Actualizar precios: Aplica un aumento del 8.4%, a todos los
    productos, utilizando la función map. Los productos actualizados se
    guardan en el archivo "Insumos.csv".
    10. Salir del programa 
    """)
    
    opcion = input("Ingrese opcion: ")
        
    return opcion #esta funcion solo se encarga de mostrar y devolver la opcion que quiera el usuario


def cargarArchivos()->list:
    lista_ordenada = []
    contador = 0
    
    with open("insumos.csv", encoding="utf8") as archivo: #Tuve que usar el encoding="utf8" por el error: UnicodeDecodeError.
        for linea in archivo:
            insumo = re.split(',|\n',linea,0)
            
            if contador == 0: 
                print("esta linea no tiene datos")
                
            else: 
                diccionario_insumos = {}

                diccionario_insumos["id"] = insumo[0] 
                diccionario_insumos["nombre"] = insumo[1].capitalize()  
                diccionario_insumos["marca"] = insumo[2].capitalize()  
                diccionario_insumos["precio"] = float(insumo[3].replace("$"," "))
                diccionario_insumos["descripcion"] = insumo[4].lower() 
                
                lista_ordenada.append(diccionario_insumos)    
                print("Archivo cargado con exito!")
            
            contador += 1
    
    return lista_ordenada


def esta_en_lista(lista:list, item:str)-> bool:
    """devuelve un booleano si es que el item ingresado en el parametro esta en la lista ubicada en el parametro

    Args:
        lista (list): una lista que contenga valores
        item (str): el valor que quiera buscar en la lista

    Returns:
        bool: False si el item no esta en la lista, y True si el item esta en la lista
    """
    esta = False
    for elemento in lista:
        if elemento == item:
            esta = True
            break
        
    return esta 

def mostrarInsumoMarcas(lista:list, clave:str):
    """Muestra las marcas y sus respectivos insumos

    Args:
        lista (list): lista con diccionario
        clave (str): la clave que desea buscar en el diccionario de la lista ingresada
        
    """
    lista_insumos = []
    marcas = []

    for insumo in lista:
        lista_insumos.append(insumo.copy())

    for insumo in lista_insumos:     
        if not esta_en_lista(marcas, insumo[clave]):
            marcas.append(insumo[clave])
            
    for marca in marcas: 
        print("marca: " + marca)
        for insumo in lista:
            if(insumo['marca'] == marca):
                print(f"{insumo['id']} | {insumo['nombre']:33s} | {insumo['marca']:25s} | {insumo['precio']} |{insumo['descripcion']:25s} ")
            
        print("----------------------------------")
        
def mostrarPreciosMarcas(lista:list, clave:str):
    """Muestra SOLAMENTE los nombres y precios de las marcas mostradas como titulo

    Args:
        lista (list): lista con diccionario
        clave (str): clave para acceder a los valores
    """
    lista_insumos = []
    marcas = []

    for insumo in lista:
        lista_insumos.append(insumo.copy())

    for insumo in lista_insumos:
        if not esta_en_lista(marcas, insumo[clave]):
            marcas.append(insumo[clave])
            
    for tipo in marcas:
        print("marca: " + tipo)
        for insumo in lista:
            if(insumo['marca'] == tipo):
                print(insumo['nombre'], insumo['precio'])
            
        print("----------------------------------")

def encontrarCaracteristica(lista:list, descripcion:str):
    """Recorre la lista ingresada y compara los valores con la descripcion ingresada, si encuentra muestra la lista, sino muestra un mensaje "no se encontro la descripcion" 

    Args:
        lista (list): lista con diccionario 
        descripcion (str): la descripcion que busca
    """
    descripcion = input("Ingrese la descripcion que desea: ").lower()
    contador = 0
        
    for insumo in lista: 
        if descripcion in insumo['descripcion']:
            contador += 1
            print(f"{insumo['id']} | {insumo['nombre']:33s} | {insumo['marca']:25s} | {insumo['precio']} |{insumo['descripcion']:25s} ")
            print("------------------------------------------------------------------------------")

    if contador == 0:
        print("No se encontro la descripcion ingresada en el sistema...")
        
def ordenarMayor(lista:list)->list:
    """Ordena por Marca en ASCENDENTE comparando una marca con todas las marcas, en caso de misma marca va a ordenar por precio de forma descendiente 

    Args:
        lista (list): lista con diccionario

    Returns:
        list: lista con diccionario ordenado
    """
    tam = len(lista)
            
    for i in range(tam - 1):
        for j in range (i + 1, tam):
            if ((lista[i]['marca'] > lista[j]['marca']) or (lista[i]['marca'] == lista[j]['marca']) and (lista[i]['precio'] < lista[j]['precio'])):  
                aux = lista[i]
                lista[i] = lista[j]     
                lista[j] = aux       
    
    lista_ordenada = lista            
    return lista_ordenada

def mostrarOrdenado(lista:list):
    """muestra de forma "Pretty" la lista que es ingresada

    Args:
        lista (list): lista con diccionario
    """
    for insumo in lista:
        descripcion = re.split('~',insumo['descripcion'])
        print(f"{insumo['id']:25s} | {insumo['nombre']:33s} | {insumo['marca']:25s} | {insumo['precio']} |{descripcion[0]:25s} ")
        print("---------------------------------------------------------------------------------------------------------------")

def realizarCompra(lista:list):
    """Esta función realiza un sistema de compras en las que el usuario ingresa la marca que desea, si no esta en el sistema, lo hecha del sistema y termina, si esta,
    muestra todas las ocurrencias de esa marca en la lista, y para elegir el producto deseado tiene que ingresar el ID que identifica el insumo mostrado anteriormente
    Si el usuario ingresa un ID que no esta en el sistema lo devuelve al menu, al encontrar ambos datos (ID y Marca) se preguntara si quiere confirmar la compra
    al confirmar se preguntara por la cantidad, se generar un archivo de texto en donde esta el recibo de los productos comprados, marca y la cantidad """
    respuesta = 's'
    total = 0
    
    flag_id_encontrado = False
    flag_marca_encontrado = False
    cantidad_lista = []        
    producto_comprado = []        
    marca_lista = []        
    precio = [] 
    
    while respuesta == 's':
        while True:
            marca = input("Ingrese la marca que busca: ").capitalize()
            
            if marca.istitle() and marca.isalpha():
                break
            
            else:
                print("Error, ingrese solo palabras.")
        
        for insumo in lista: 
            if marca in insumo['marca']:
                flag_marca_encontrado = True
                print(f"{insumo['id']} | {insumo['nombre']:33s} | {insumo['marca']:25s} | {insumo['precio']} |{insumo['descripcion']:25s} ")
                print("--------------------------------------------------------------------------")
                
        if flag_marca_encontrado:        
            id = input("ingrese el id del producto que quiera comprar: ")
            
            for insumo in lista:
                if id == insumo['id'] and re.match(marca,insumo['marca']):
                    flag_id_encontrado = True
                    articuloComprado  = (insumo)
                    print(f"{articuloComprado['id']} | {articuloComprado['nombre']:33s} | {articuloComprado['marca']:25s} | {articuloComprado['precio']} | {articuloComprado['descripcion']:25s}")
            
            if flag_id_encontrado: 
                confirmacion = input("este es el producto que desea comprar ? s/n ").lower()
                if confirmacion == 's':
                    while True:
                        try: 
                            cantidad = int(input("Cuanta cantidad va a llevar ? ")) 
                            break
                        except ValueError:
                            print("lo que ingreso no es un numero")
                    
                        
                    cantidad_lista.append(cantidad)
                    producto_comprado.append(articuloComprado['nombre'])
                    marca_lista.append(articuloComprado['marca'])
                    precio.append(articuloComprado['precio'])
                    
                    total += float(multiplicar(articuloComprado['precio'],cantidad))  
                    respuesta = input("Desea continuar ? s/n ").lower()
                    
                    if respuesta == 'n' and (esta_en_lista(marca_lista,articuloComprado['marca']) == False):
                        break
                    
                    
                    else:
                        with open("D:\\Users\\lucas\\Desktop\\Consigna Parcial Laboratorio 1-A Lucas Carabajal\\Recibo.txt","w",encoding="utf8") as recibo:
                            mensaje = f"""
                                        RECIBO DE COMPRA
                            --------------------------------------------
                            Cantidad Comprada: {cantidad_lista}
                            Producto Comprado: {producto_comprado}
                            Marca: {marca_lista}
                            Precio: {precio}
                            --------------------------------------------
                            """
                            recibo.write(mensaje + os.linesep)
                            recibo.write("Total: " + str(total))
                            
                else:
                    print("Compra cancelada con exito!")
                    break
            else:
                print("Error, ID y Marca No se encontraron, volviendo al menu...")
                break
        else:
            print("No se encontro la marca buscada, porfavor intentelo denuevo desde menu...")
            break
        
       
def encontrarNombre(lista:list):
    """Busca en la lista ingresada la palabra Alimento, si encuentra coincidencia agrega la linea de datos de la lista a una nueva lista alimentos

    Args:
        lista (list): Lista con diccionario
    """
    lista_Alimentos = []
    for insumo in lista:
        if re.match("Alimento",insumo['nombre']):
            lista_Alimentos.append(insumo)
                      
    with open("D:\\Users\\lucas\\Desktop\\Consigna Parcial Laboratorio 1-A Lucas Carabajal\\lista_alimentos.json","w",encoding="utf8") as alimentos:
        json.dump(lista_Alimentos, alimentos, indent = 2, ensure_ascii=False , separators=(", ", " : ")) #Aca tuve que deshabilitar el formato ascii porque sino salian \u00f3 en el medio del texto   
        print("El Archivo json se a creado con exito!")
      
def mostrarJson():
    """Muestra el archivo json creado con la funcion mostrarJson()
    """
    with open("lista_alimentos.json",'r',encoding="utf8") as archivo_json:
        insumos = json.load(archivo_json)
        for insumo in insumos:
            print(f"ID:{insumo['id']:2s} | NOMBRE:{insumo['nombre']:21s} | MARCA:{insumo['marca']:20s} | PRECIO:{insumo['precio']} | DESCRIPCION:{insumo['descripcion']:25s}")
            print("--------------------------------------------------------------------------------------------------------------------------")

def aumentoPrecio(lista:list):
    """Realiza un aumento de precio del 8.4% en la lista que ingresaron en el parametro

    Args:
        lista (list): lista con diccionario
    """
    with open("insumos.csv",'w',encoding="utf8") as archivo:
           
        precios_aumentados = (list(map(lambda item: round(item['precio']*8.4/100 + item['precio'],2),lista)))    
        contador = -1
        for insumo in lista:
            contador += 1
            insumo['precio'] = precios_aumentados[contador]       
            nuevaLinea = f"{insumo['id']},{insumo['nombre']},{insumo['marca']},${insumo['precio']},{insumo['descripcion']}\n"
            archivo.write(nuevaLinea)
        