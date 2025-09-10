# Autor: Juan Camilo Páez Guaspud
# Se realizará un ejercicio práctico para usar clases, objetos y atributos en Python.

# Autor: Juan Camilo Páez Guaspud
# Ejercicio práctico de clases, objetos y atributos en Python.

# Se crea la clase Perro
class Perro:
    def __init__(self, nombre, felicidad=0):
        self.nombre = nombre
        self.felicidad = felicidad

# Se crean dos métodos: ladrar y hacer_feliz.
# El método ladrar devuelve un string y la salida "Guau Guau" cuando se pida.
    def ladrar(self):
        return f"{self.nombre}: Guau Guau"

# El método hacer_feliz recibe una acción y aumenta la felicidad del perro un 25% por cada una hasta un máximo del 100% de felicidad.
    def hacer_feliz(self, accion):
        if self.felicidad < 100:
            self.felicidad += 25
            if self.felicidad > 100:
                self.felicidad = 100

# Se imprimen mensajes diferentes según la acción realizada.
            print(f"\nHas elegido {accion}.")
            print(f"¡Ahora {self.nombre} es más feliz!\n{self.nombre} tiene {self.felicidad}% de felicidad.\n")
        else:
            print(f"{self.nombre} ya está completamente feliz")

# Inmput pide el nombre del perro para crear un objeto de la clase Perro.
nombre_perro = input("Ingrese el nombre del perro: ")
perro1 = Perro(nombre_perro)

# Se usa bucle while que permite al usuario elegir entre las 3 acciones para hacer feliz al perro hasta que su felicidad llegue al 100%.
while perro1.felicidad < 100:
    accion = input(f"Elije cómo quieres hacer feliz a {perro1.nombre}:\n- jugar\n- alimentar\n- acariciar\n")
    perro1.hacer_feliz(accion)

# Si la felicidad del perro llega al 100%, se imprime un mensaje indicando que el perro está completamente feliz y se llama al método ladrar para que el perro ladre de felicidad.
print(f"\n!{perro1.nombre} ahora sí está completamente feliz¡")
print(perro1.ladrar())

