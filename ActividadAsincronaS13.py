def Programa_On():
    estudiantes = [{'nombres': "Josue Aaron",  "apellidos": "Castillo Valdiviezo","edad": "21","sexo": "Masculino","departamento": "Chalatenango","municipio":"Dulce Nombre de Maria","direccion":"Barrio Concepcion" },
         {'nombres': "Rolando Alexander",  "apellidos": "Perez Lopez","edad": "17","sexo": "Masculino","departamento": "Chalatenango","municipio":"Nombre de jesus","direccion":"Barrio el centro"  },
         {'nombres': "Gerardo Antonio",  "apellidos": "Rosa Menjivar","edad": "17","sexo": "Masculino", "departamento": "Chalatenango","municipio":"Chalatenango","direccion":"Barrio el calvario, Chalatenango" },
         {'nombres': "Jose Nicolas",  "apellidos": "Abrego Salguero","edad": "18","sexo": "Masculino","departamento": "Chalatenango","municipio":"Dulce Nombre de María","direccion":"Barrio San José" },
         {'nombres': "Bryan Edenilson",  "apellidos": "Quintanilla Alberto","edad": "22","sexo": "Masculino","departamento": "Chalatenango","municipio":"Chalatenango","direccion":"Colonia Fatima, Calle al tanque"  },
         {'nombres': "Rocio Marbelly", "apellidos": "Moreno Erazo", "edad": "17", "sexo": "Femenino", "departamento": "Chalatenango", "municipio": "Agua Caliente", "direccion": "Barrio El Carmen"}]
    
    #variables
    onlyname = []
    intentos = 3
    count = 0
    j = 1
    continuar = True
    #Bucle para poder regresar si quiere volver a consultar un integrante
    while continuar:
        #Preguntamos si quieres ejecutar el programa
        respuesta = input("¿Quieres ejecutar el programa? (SI/NO) :")
        #condicional si desea ejecutar el programa
        if respuesta.lower() == "si" or respuesta == "s":
            #ciclo for para lista de integrantes del grupo
            for persona in estudiantes:
                onlyname.append(persona["nombres"])
                print(f"{j}-",persona['nombres'])
                j += 1 
            #declaramos variables de intentos 
            intentos_maximos = 3
            intentos = 0
            nombre_correcto = False
            #ciclo while  con doble condicion negamos el valor booleano y revisamos los intentos 
            while not nombre_correcto and intentos < intentos_maximos:
                buscar = input("Ingrese el nombre de uno de los integrantes del grupo: ")
                #ciclo iteramos los estudiantes y con el condicional if verificamos que se encuentre en la lista de estudiantes y si esta imprimos los resultados
                for i in range(len(estudiantes)):
                    if buscar == estudiantes[i]["nombres"]:
                        nombre_correcto = True
                        print("-----------------------------------------------------------")
                        print("Datos del integrante:")
                        print("-----------------------------------------------------------")
                        print(f"Nombres: {estudiantes[i]['nombres']} \nApellidos: {estudiantes[i]['apellidos']} \nSexo: {estudiantes[i]['sexo']} \nEdad: {estudiantes[i]['edad']} \nDepartamento: {estudiantes[i]['departamento']} \nMunicipio: {estudiantes[i]['municipio']} \nDireccion: {estudiantes[i]['direccion']}")                        
                        print("-----------------------------------------------------------")
                        #despues de imprimirlo preguntamos si quiere seguir probando 
                        respuesta = input("¿Desea consultar otro dato de los integrantes? (S/N) ").upper()
                        #si la respuesta es no salimos del programa
                        if respuesta == "N":
                            print("Saliendo del Programa....")
                            print("Programa Finalizado...")
                            continuar = False
                            break
                        else:
                            #si es si volvera al inicio
                            print("Volvera desde el principio...")
                #si no se encentra el nombre puede ser que se equivoco al ingresar el nombre entonces aumentamos los intentos
                if not nombre_correcto:
                    intentos += 1
                    if intentos < intentos_maximos:
                        print("Nombre incorrecto, intente nuevamente...")
                        print(f"Te quedan {intentos_maximos-intentos} intentos")
                    else:
                        print("Demasiados intentos incorrectos, vuelva a intentarlo desde el principio.") 
        #aqui si desde el principio dice que no el programa no se ejecuta y se cierra
        else:    
            print("Programa no ejecutado.")
            print("Programa Finalizado...")
Programa_On()