def calculadora(num1, num2, operacion):
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "No se puede dividir por cero."
    

# Función para solicitar un numero entero al usuario
def solicitar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))  
            return numero
        except ValueError:  # Si no es un numero entero muestra un mensaje de error
            print("Debes ingresar un numero entero, Porfavor Intentalo de nuevo.")


num1 = solicitar_numero("Ingresa el primer numero: ")
num2 = solicitar_numero("Ingresa el segundo numero: ")


while True:
    operacion = input("Ingresa la operación (+, -, *, /): ")
    if operacion in ['+', '-', '*', '/']:  
        break
    else:
        print("Operacion no valida, Porfavor Intentalo de nuevo")

resultado = calculadora(num1, num2, operacion)
print("El resultado es:", resultado)