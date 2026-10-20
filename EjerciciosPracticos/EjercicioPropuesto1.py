class Estudiante:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 5.0:
            self.__notas.append(nota)
        else:
            print(f"Error: La nota {nota} no es válida. Debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self):
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        else:
            return 0

    @property
    def notas(self):
        return self.__notas.copy()

    def obtener_nombre(self):
        return self.__nombre


est1 = Estudiante("Alvaro")
est1.agregar_nota(4.5)
est1.agregar_nota(3.8)
est1.agregar_nota(-1.5)
est1.agregar_nota(5.2)
est1.agregar_nota(4.0)
est1.agregar_nota(3.5)

print(f"Estudiante: {est1.obtener_nombre()}")
print(f"Notas: {est1.notas}")
print(f"Promedio: {est1.calcular_promedio()}")