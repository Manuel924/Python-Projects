# concatenated
a = "uno"
b = "dos"
c = a + b # c es "unodos"
print (c)
c = a * 3 # c es "unounouno"
print (c)
print("\nOperations with variables")
a = 14
b = 12
c = a + b
print (a,"hola", b, '=', c)
print("\nFin")

# convertir grado faranhaigeth a celcius.

f = 120
c = ((f-32)*5/9)

print ("La temperatura en grados celcius es = ", c)

# empresa para tomar una decision
# si el monto total de compra excede de 500,000 tendra que invertir del propio dinero del 55% pedir prestado al banco un 30% y el resto lo 
# pagara solicitando un credito al fabricante y si el monto total no excede de la cantidad mencionada al principio , la empresa invertira su 
# propio dinero en un 70% y el 30 solicitando un credito al fabricante el fabricate cobra 20% sobre la cantidad a pagar a credito

print("Ingrese el monto total de la compra")
compra = float (input())

def calcular_inversion_compra(monto_total):
    if monto_total > 500000:
        inversion_propia = monto_total * 0.55
        prestamo_banco = monto_total * 0.30
        credito_fabricante = monto_total - inversion_propia - prestamo_banco
        costo_credito_fabricante = credito_fabricante * 0.20
    #se calcula la inversion que se debe hacer si es menor a lo especificado en el problema
    else:
        inversion_propia = monto_total * 0.70
        credito_fabricante = monto_total * 0.30

    costo_credito_fabricante = credito_fabricante * 0.20
    total_a_pagar = monto_total + costo_credito_fabricante

    return {
        "Inversión Propia": inversion_propia,
        "Préstamo del Banco": prestamo_banco if monto_total > 500000 else 0, #se asigna 0 si es menor ya que no hay necesidad de prestamo de banco 
        "Crédito al Fabricante": credito_fabricante,
        "Costo del Crédito al Fabricante": costo_credito_fabricante,
        "Total a Pagar": total_a_pagar
    }

resultado = calcular_inversion_compra(compra)

print("\nDetalle de la inversión:")
for key, value in resultado.items(): #iteracion for para imprimir los resultados del 
    print(f"{key}: ${value:.2f}") 
