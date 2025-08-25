notas = []
contador = 1

while contador < 10:
    notas.append(int(input(f'Informe a {contador} a nota: ')))
    contador += 1
      
media = sum(notas) / len(notas)
print(F"Sua media final foi {media}")

if media >= 7:
    print("Aprovado")
else:
    notas.append(int(input(f"Informe sua nota da prova final: ")))
    media = sum(notas) / len(notas)
    print  ("Sua media final foi {media}")
    
    if media >= 5:
        print("APROVADO")
    else: 
        print("REPROVADO ")
        