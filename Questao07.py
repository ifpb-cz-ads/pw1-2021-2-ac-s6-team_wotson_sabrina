n1 = int(input("Informe o primeiro numero desejado: "))
n2 = int(input("Informe o sefundo numero desejado: "))
aux = 1
resultado = n1
while aux < n2:
    resultado = resultado + n1
    aux = aux + 1

print(resultado)