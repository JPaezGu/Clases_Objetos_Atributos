# Autor: Juan Camilo Páez Guaspud
# Se realizará un ejercicio práctico para usar clases, objetos y atributos en Python.

#

class Perro:
    def __init__(self, nombre, felicidad=0):
        self.nombre = nombre
        self.felicidad = felicidad

    def ladrar(self):
        return f"{self.nombre}: Guau Guau"

    def acariciar(self):
        if self.felicidad <= 80:
            self.felicidad += 20
            print(
                f"¡Ahora,{self.nombre} es más feliz \n{self.nombre} es {self.felicidad}% feliz")
        else:
            print(f"{self.nombre}ya es feliz")

    def alimentar(self):
        if self.felicidad <= 80:
            self.felicidad += 20
            print(
                f"¡Ahora,{self.nombre} es más feliz \n{self.nombre} es {self.felicidad}% feliz")

        else:
            print(f"{self.nombre}ya es feliz")

    def jugar(self):
        if self.felicidad <= 80:
            self.felicidad += 20
            print(
                f"¡Ahora,{self.nombre} es más feliz \n{self.nombre} es {self.felicidad}% feliz")
        else:
            print(f"{self.nombre}ya es feliz")

nombre_perro = input("Ingrese el nombre del perro: ")
perro1 = Perro(nombre_perro)

accion = input(
    f"Elija cómo quiere hacer al perro feliz\njugar\nalimentar\nacariciar\n")
if accion == "jugar":
    perro1.jugar()
elif accion == "alimentar":
    perro1.alimentar()
elif accion == "acariciar":
    perro1.acariciar()

# print(perro1.ladrar())
