n = int(input("Ingrese el número de vendedores que estaran  "))
sueldo_base = float(input("Ingrese el sueldo base de los vendedores: "))

for i in range(n):
    ventas = 3
    comisiones = ventas * sueldo_base * 0.1
    salario_total = sueldo_base + comisiones
    
    print(f"Vendedor {i+1}:")
    print(f"Comisiones por las 3 ventas realizadas: {comisiones}")
    print(f"Salario total: {salario_total}\n")
