numeros =  [21, 5, 34, 8, 16, ]
soma  = sum(map(lambda n: n if n % 2 == 0 else 0, numeros))
soma_impares = sum(map(lambda n: n if n % 2 != 0 else 0, numeros ))
print(f"A soma dos valores pares e {soma} e dos impares é {soma_impares}")