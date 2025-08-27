# preguntar el nombre de la mascota

hasAnimal = str(input("tienes alguna animal? si/no "))
if(hasAnimal == "si"):
    animalType = str(input("Que bueno!Que animal tienes?: "))
    if(animalType == "perro"):
        print("que lindo perrito")
    elif(animalType == "gato"):
        print("que lindo gatito")
    elif(animalType == "pajaro"):
        print("que lindo pajarito")
    else:
        print("Que interesante..")
else:
 print("deberias adoptar un pajarito, no comprar uno!")


