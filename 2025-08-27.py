#Day Logger
print("Hello! Good morning! Please enter your name")

name = str(input("Enter your name: "))

print(f"Hi {name}")

age = int(input("What is your age?: "))

print(f"nice to meet you {name} your name is: {age}")

if(age >  25):
    print("your age is {age}")
    print("good good, do you have kids?")
    nHijos = int(input("ingresa la cantidad de hijos: "))
    print(f"tienes {nHijos} hijos que bien, me alegro")
    statusCasado = str(input("Estas casado o soltero?, Ingresa casado o soltero "))

    if(statusCasado == "casado"):
        print(f"que bueno que estes casado!")
        esFeliz = str(input("Eres Feliz?, ingrese si o No "))
        if(esFeliz == "si"):
            print(f"que bueno!")
        else:
            print(f"Uhh lo siento, aca tienes un numero deprevencion al suicidio 0800-No-Te-Cuelgues")
    else:
        print(f"que bueno bro!")
else:
    mascotas = int(input("Ingrese numero de mascotas "))
    print(f"tienes {mascotas} mascota? Mira  vos! ")

