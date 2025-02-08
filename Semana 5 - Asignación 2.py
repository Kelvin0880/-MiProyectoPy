class ContadorDePalabras:
    def __init__(self):
        self.contador = 0

    def contar_palabras(self, texto):
        palabras = texto.split()
        self.contador += len(palabras)

    def obtener_contador(self):
        return self.contador


mi_contador = ContadorDePalabras()


texto_ejemplo = "Me gusta jugar videojuegos de noche por que hay mejor internet a esas horas"
mi_contador.contar_palabras(texto_ejemplo)

# Mostrar el resultado del contador
print("Total de palabras contadas:", mi_contador.obtener_contador())