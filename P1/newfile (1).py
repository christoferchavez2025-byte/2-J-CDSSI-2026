# Programa para calcular documento y costo de viaje

print("PROGRAMA DE VIAJE")

# Datos del usuario
nombre = "Christofer Alberto Chávez Ceja"
edad = 15
destino = "Estados Unidos"
vigencia = 1

print("Nombre:", nombre)
print("Edad:", edad)
print("Destino:", destino)
print("Vigencia del pasaporte:", vigencia, "año")

# Verificar documento
if destino == "Estados Unidos":
    print("Documento necesario: Pasaporte")

# Calcular costo
if vigencia == 1:
    costo = 800

print("Costo del pasaporte: $", costo, "pesos mexicanos")

print("Fin del programa")