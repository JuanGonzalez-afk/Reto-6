n = int(input("Ingresa un número natural (n ≥ 0): "))

if n >= 0:
    factorial = 1
    i = 1
    while i <= n:
        factorial = factorial * i   
        i = i + 1  

    print("El factorial de", n, "es:", factorial)
else:
    print("Por favor, ingresa un numero natural (mayor o igual a 0).")