# UPNET
# Bienvenido al sistema de carga de datos de los alumnos 


nombreEstudiante = str("")
edadEstudiante = int(0)
numeroDeDocumentoEstudiante = int(0)
carreraEstudiante = int(0)
textoFinalizadorSystema = str("")

edadDelAlumnoMasJoven = int(0)
nombreDelAlumnoMasJoven = str("")

edadDelAlumnoMasVeterano = int(0)
nombreDelAlumnoMasVeterano = str("")

contadorCarreraIngenieria = int(0)
contadorCarreraLicenciatura = int(0)

promedioEdadesAlumnos = int(0)

porcentajeAlumnosEnIngenia = int(0)
porcentajeAlumnosEnLicenciatura = int(0)

numeroDeDocumentoMasAltoRegistrado = int(0)

numeroErroresAlIngresarEdadesODocumentos = int(0)

i = int(0)

while(textoFinalizadorSystema != "FIN"):
 
   

    nombreEstudiante = str(input("Ingrese el nombre del estudiante")).upper()
    edadEstudiante = int(input("Ingrese la edad del estudiante"))
    
     if( i == 0):
        edadDelAlumnoMasJoven = edadEstudiante 
        edadDelAlumnoMasVeterano = edadEstudiante 
        nombreDelAlumnoMasJoven = nombreEstudiante
        nombreDelAlumnoMasVeterano = nombreEstudiante
    if (edadEstudiante > 

    numeroDeDocumentoEstudiante = int(input("Ingresar el numero de documento sin puntos. Tiene que ser mayor a 0"))
    carreraEstudiante = int(input(f"Cual carrera el estudiante se inscribe?\nIngrese 1 si es Ingenieria y 2 si es Licenciatura :"))
        
    if(carreraEstudiante == 1):
        contadorCarreraIngenieria = contadorCarreraIngenieria + 1
    elif(carreraEstudiante == 2):
        contadorCarreraLicenciatura = contadorCarreraLicenciatura + 1
        
    while(numeroDeDocumentoEstudiante == 0):
        numeroDeDocumentoEstudiante = int(input("Ingresar el numero de documento sin puntos. Tiene que ser mayor a 0. Intente de Nuevo"))

    textoFinalizadorSystema = str(input("Quiere finalizar la carga de usuarios? De ser SI su repuesta ingresar (FIN)")).upper()

print("Se finalizo el programa")
if(contadorCarreraIngenieria > contadorCarreraLicenciatura):
    print(f"La carrera con mas alumnos es Ingenieria, con un total de: {contadorCarreraIngenieria}")
elif(contadorCarreraIngenieria == contadorCarreraLicenciatura):
    print(f"Ambas carreras tiene {contadorCarreraIngenieria } estudiantes")
else:
    print(f"La carrera con mas alumnos es Licenciatura, con un total de: {contadorCarreraLicenciatura}")
print(f"El porcentaje de alumnos en Ingenieria es: {porcentajeAlumnosEnIngenia}%\nEl porcentaje de alumnos en Licenciatura es: {porcentajeAlumnosEnLicenciatura}%")