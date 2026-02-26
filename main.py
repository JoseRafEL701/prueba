import random
numero_secreto = random.randint(1,30)
print("adivina el numero entre el 1 y el 30")

while True:
    intento = int(input("tu numero: "))
    if intento == numero_secreto: 
        print(" ¡Ganaste!" )
        break
    elif intento < numero_secreto:
        print("muy bajo")
    else:
        print("muy alto")

