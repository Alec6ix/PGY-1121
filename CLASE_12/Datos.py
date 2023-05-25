# Ejemplo de uso de GitHub
print("Ingreso de datos")
print("————————————    \n")
nom = str(input("Ingrese su nombre: "))
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except:
        print("Dato ingresado inválido.")
print("————————————————————————")
print(f"Su nombre es: {nom}")
print(f"Su edad es: {edad}")
print("Programa finalizado.")