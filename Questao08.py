n1 = int(input("Informe o primeiro numero desejado: "))
n2 = int(input("Informe o sefundo numero desejado: "))
aux = 0
aux2 = n1
resto = 0

if(n1 <= n2):

    print("Nao e possivel efertuar a operacao pois o dividendo é menor que o divisor.")

else:

    while n1 >= n2:
        n1 = n1 - n2
        aux = aux + 1

        if (n1 < n2):
            resto = n1

    print("A divisao de", aux2, "por", n2, "foi: ", aux, " e o resto foi: ", resto)

