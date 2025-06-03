# Este programa imprime los números del 1 al 100 junto con sus cuadrados

# Empezamos con el número 1
numero = 1

# Usamos un ciclo "while" para repetir las instrucciones mientras el número sea menor o igual a 100
while numero <= 100:
    # Calculamos el cuadrado del número
    cuadrado = numero * numero

    # Mostramos el número y su cuadrado en la pantalla
    print("Número:", numero, "-> Cuadrado:", cuadrado)

    # Aumentamos el número en 1 para pasar al siguiente
    numero = numero + 1

# Cuando el número es mayor que 100, el programa termina
