n = int(input("Ingresa un número natural mayor o igual que 2: "))

if n >= 2:
    i = n
    while i >= 2:
        if i % 2 == 0:
            print(i) 
        i = i - 1
else:
    print("El número debe ser mayor o igual que 2.")
