n = int(input("Tabuada de: "))
inicio = int(input("Informe o inicio desejado: "))
fim = int(input("Informe o fim desejado: "))
x = inicio

while x <= fim:
	resultado = n * x
	print(n, "x", x, "=", resultado)
	x = x + 1
