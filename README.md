# Autor: Juan Camilo Páez Guaspud
# Clases_Objetos_Atributos

-Se realizará un ejercicio práctico para usar clases, objetos y atributos en Python.

-El ejercicio consiste en crear una clase Perro, objetos y atributos, y que en base a una selección de acciones, el perro sea feliz, cuando el perro esté completamente feliz, ladrará.

    EJERCICIO - HACER AL PERRO FELIZ

Paso N_01
-Se empieza creando una clase, en este caso será una clase llamada Perro con dos atributos: nombre y felicidad (definida con valor 0 para actualizar su valor por cada acción de felicidad):

    def ladrar(self):
        return f"{self.nombre}: Guau Guau"


Paso N_02
-El método hacer_feliz recibe una acción y aumenta la felicidad del perro un 25% por cada una, hasta un máximo del 100% de felicidad:

    def hacer_feliz(self, accion):
        if self.felicidad < 100:
            self.felicidad += 25
            if self.felicidad > 100:
                self.felicidad = 100


Paso N_03
Dependiendo de la acción elegida (jugar, alimentar o acariciar), se imprimirá y luego se especificará el porcentaje de felicidad del perro:

            print(f"\nHas elegido {accion}.")
            print(f"¡Ahora {self.nombre} es más feliz!\n{self.nombre} tiene {self.felicidad}% de felicidad.\n")
        else:
            print(f"{self.nombre} ya está completamente feliz al 100%!")


Paso N_04
- Se usa el comando input para pedir el nombre del perro, con el fin de crear un objeto de la clase Perro con el mismo nombre:

    nombre_perro = input("Ingrese el nombre del perro: ")
           
    perro1 = Perro(nombre_perro)


Paso N_05
-Se usa el bucle while que permite al usuario elegir entre las 3 acciones disponibles para hacer feliz al perro, hasta que su felicidad llegue al 100% (límite):

    while perro1.felicidad < 100:
        accion = input(f"Elija cómo quiere hacer feliz a {perro1.nombre}:\n- jugar\n- alimentar\n- acariciar\n")
        perro1.hacer_feliz(accion)


Paso N_06
-Si la felicidad del perro llega al 100%, se imprimirá un mensaje (con el nombre del perro) indicando que está completamente feliz, luego, se llama a la acción .ladrar para que el perro ladre de felicidad:

    print(f"\n {perro1.nombre} ahora está completamente feliz")
    print(perro1.ladrar())

    RESULTADO - SALIDA

-Si todo ha salido bien, esta será la salida que nos dará el programa:

Ingrese el nombre del perro: Tobby
Elije cómo quieres hacer feliz a Tobby:
- jugar
- alimentar
- acariciar
jugar

Has elegido jugar.
¡Ahora Tobby es más feliz!
Tobby tiene 25% de felicidad.

Elije cómo quieres hacer feliz a Tobby:
- jugar
- alimentar
- acariciar
alimentar

Has elegido alimentar.
¡Ahora Tobby es más feliz!
Tobby tiene 50% de felicidad.

Elije cómo quieres hacer feliz a Tobby:
- jugar
- alimentar
- acariciar
acariciar

Has elegido acariciar.
¡Ahora Tobby es más feliz!
Tobby tiene 75% de felicidad.

Elije cómo quieres hacer feliz a Tobby:
- jugar
- alimentar
- acariciar
jugar

Has elegido jugar.
¡Ahora Tobby es más feliz!
Tobby tiene 100% de felicidad.


!Tobby ahora sí está completamente feliz¡
Tobby: Guau Guau




