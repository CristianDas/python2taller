n_alumnos = 40
n_materias = 5
promedios = []

for i in range(n_alumnos):
    print(f"Ingrese las calificaciones del alumno {i+1}:")
    calificaciones = []
    for j in range(n_materias):
        calif = float(input(f"Calificación {j+1}: "))
        calificaciones.append(calif)
    
    promedio = sum(calificaciones) / n_materias
    promedios.append(promedio)


no_aprobados = sum(1 for p in promedios if p < 70)


print(f"Cantidad de alumnos que no tienen derecho al examen de nivelación: {no_aprobados}")
