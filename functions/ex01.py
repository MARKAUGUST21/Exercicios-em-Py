def numero_par_ou_impar(numero):
    if numero % 2 == 0:
        return f"O numero é {numero} é par "
    return f"O numero {numero} é impar"

numero = int(input('Informe um numero inteiro qualquer : '))
print(numero_par_ou_impar(numero))