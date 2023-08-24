# decalara variables

continuar = True
totalVenta = 0
cantidadVenta = 0

def inputNumber(mensaje, isFloat = False):
    while True:
        try:
            if isFloat:
                return float(input(mensaje))
            return int(input(mensaje))
        except ValueError:
            print("Opps!! no es una entrada valida intenta de nuevo")

while continuar == True:
    cantidad = inputNumber("Ingresa la cantidad de producto: ")
    precio = inputNumber("Ingresa el precio por unidad: ", True)
    


    totalSinDescuento = cantidad * precio 

    if cantidad >= 5 and cantidad <= 10:
        totalVenta += totalSinDescuento - (totalSinDescuento*0.05)
    elif cantidad >= 11 and cantidad <= 20:
        totalVenta += totalSinDescuento - (totalSinDescuento*0.10)
    elif cantidad > 20:
        totalVenta += totalSinDescuento - (totalSinDescuento*0.15)
    else:
        totalVenta += (cantidad*precio)

    cantidadVenta += cantidad 

    opcion = input ("continuar? S/N: ")

    if opcion.upper () == "N":
        continuar =False
        print("Gracias por comprar!")

print("Total de la venta ${0}".format (totalVenta))
print("Unidades totales ${0}: ".format (cantidadVenta))

