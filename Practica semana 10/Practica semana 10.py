import pandas as pd

def crear_dataframe():
    data = {
        'Nombre': ['Ana', 'Luis', 'Marta', 'Pedro'],
        'Edad': [23, 30, 25, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
        'Puntaje': [85, 90, 78, 92]
    }
    return pd.DataFrame(data)

def ejercicio_1():
    df = crear_dataframe()
    print("\nEjercicio 1 - DataFrame creado:")
    print(df)

def ejercicio_2():
    df = crear_dataframe()
    filtro_edad = df[df['Edad'] > 25]
    print("\nEjercicio 2 - Filas con edad mayor a 25:")
    print(filtro_edad)

def ejercicio_3():
    df = crear_dataframe()
    edad_media = df['Edad'].mean()
    edad_maxima = df['Edad'].max()
    edad_minima = df['Edad'].min()
    puntaje_medio = df['Puntaje'].mean()
    print("\nEjercicio 3 - Estadisticas basicas:")
    print(f"Edad media: {edad_media}")
    print(f"Edad maxima: {edad_maxima}")
    print(f"Edad minima: {edad_minima}")
    print(f"Puntaje medio: {puntaje_medio}")

def ejercicio_4():
    df = crear_dataframe()
    df['Aprobado'] = df['Puntaje'].apply(lambda x: 'Si' if x >= 80 else 'No')
    print("\nEjercicio 4 - DataFrame con columna Aprobado:")
    print(df)

def mostrar_menu():
    print("\n=== MENU DE EJERCICIOS - PRACTICA SEMANA 10 ===")
    print("1. Crear un DataFrame")
    print("2. Filtrar datos (edad > 25)")
    print("3. Calcular estadisticas basicas")
    print("4. Agregar columna Aprobado")
    print("5. Salir")
    print("=======================================")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = input("Seleccione una opcion (1-5): ")
            opcion = int(opcion)  # Intentar convertir a entero

            if opcion == 1:
                ejercicio_1()
            elif opcion == 2:
                ejercicio_2()
            elif opcion == 3:
                ejercicio_3()
            elif opcion == 4:
                ejercicio_4()
            elif opcion == 5:
                print("\nGracias por usar el programa! Hasta luego.")
                break
            else:
                print("\nError: Opcion no valida. Por favor, seleccione un numero entre 1 y 5.")
        
        except ValueError:
            print("\nError: Debe ingresar un numero entero. Letras o caracteres especiales no son validos.")
        except Exception as e:
            print(f"\nError inesperado: {e}. Por favor, intenta de nuevo.")
        
        # Pausa para que el usuario pueda leer el resultado antes de volver al menu
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()