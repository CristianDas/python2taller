import random

n = int(input("Ingrese el número de clientes en la tienda: "))
precio_base = float(input("Ingrese el precio base de los productos: "))

for i in range(n):
 
    color_bolita = random.choice(["rojo", "amarillo", "blanco"])
    
    
    if color_bolita == "rojo":
        descuento = precio_base * 0.4
    elif color_bolita == "amarillo":
        descuento = precio_base * 0.25
    else:
        descuento = 0
    
    
    importe_total = precio_base - descuento
    
    print(f"Cliente {i+1}:")
    print(f"Color de bolita: {color_bolita}")
    print(f"Descuento es el : {descuento}")
    print(f"Importe total a pagar: {importe_total}\n")
