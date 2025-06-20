turistas ={
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
	"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def turistas_por_pais(pais):
    turistas_en_pais=[]
    for turista in turistas:
        if turistas[turista][1].lower() == pais.lower():
            turistas_en_pais.append(turistas[turista][0])
    if len(turistas_en_pais) ==0:
        print(f"No hay turistas pertenecientes a {pais.capitalize()}")
    else:
        print(f"Lista de turistas que pertenecen a {pais.capitalize()}: {turistas_en_pais}")

def turistas_por_mes(mes):
    turistas_mes=0
    for clave in turistas:
        fecha=turistas[clave][2].split("-")
        if int(fecha[1][0]) == 0:
            if int(mes) == int(fecha[1][1]):
                turistas_mes+=1
        else:
            if int(mes) == int(fecha[1]):
                turistas_mes+=1
    print(turistas_mes)
    porcentaje=round((turistas_mes/len(turistas))*100,1)
    return porcentaje

def eliminar_turista():
    claves_eliminar=[]
    nombre=input("Ingrese el nombre del turista que quiere eliminar: ").lower()
    for clave in turistas:
        if turistas[clave][0].lower() == nombre:
            claves_eliminar.append(clave)

    if len(claves_eliminar)==0:
        print("Turista no encontrado. No se pudo eliminar")
        return
    else:
        for elemento in claves_eliminar:
            del(turistas[elemento])
    print("Turista eliminado con exito")
    
    



while True:
    print("*** MENU PRINCIPAL ***\n1.-Turistas por país\n2.-Turistas por mes\n3.-Eliminar turista\n4.-Salir")
    while True:
        try:
            op=int(input("Ingrese una opcion: "))
            break
        except ValueError as error:
            print("Opción inválida")
    
    if op == 1:
        buscar_pais=input("Ingrese el pais que desea buscar: ")
        turistas_por_pais(buscar_pais)
    elif op ==2:
        while True:
            buscar_mes=input("Ingrese el mes que desea buscar: ")
            try:
                if int(buscar_mes) >=1 and int(buscar_mes)<=12:
                    porcentaje= turistas_por_mes(buscar_mes)
                    break
                else:
                    print("Debe ingresar un mes entre 1 y 12")
            except ValueError:
                print("Ingrese un mes válido")
        print(f"El porcentaje de turistas que vinieron a chile en el mes {buscar_mes} es: {porcentaje}")
    elif op ==3:
        eliminar_turista()
    elif op ==4:
        print("Progama terminado...")
        break
    else:
        print("Seleccione una opcion valida")