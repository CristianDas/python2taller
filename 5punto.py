
menor_a_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_a_80 = 0


for i in range(100):
    calificacion = int(input("Ingrese la calificación del estudiante " + str(i+1) + ": "))
    

    if calificacion < 50:
        menor_a_50 += 1
    elif calificacion >= 50 and calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion >= 70 and calificacion < 80:
        entre_70_y_80 += 1
    else:
        mayor_a_80 += 1

print("Cantidad de estudiantes con la calificación menor a 50: :((" + str(menor_a_50))
print("Cantidad de estudiantes con la calificación de 50 a menos de 70: " + str(entre_50_y_70))
print("Cantidad de estudiantes con la calificación de 70 a menos de 80: " + str(entre_70_y_80))
print("Cantidad de estudiantes con calificación mayor o igual a 80: " + str(mayor_a_80))
