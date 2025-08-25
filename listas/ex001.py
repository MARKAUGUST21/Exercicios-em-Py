notas = []
contador = 1

while contador < 5:
     notas.append(float(input(f"Informe a {contador} a nota: ")))
     contador += 1
     
     
maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)

print(f"A media final é {media:.2f}. A maior nota foi {maior_nota:.2f}. A menor nota foi {menor_nota:.2f}")