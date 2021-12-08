ValorTotal = float(input("Por gentileza, informe o valor do deposito: "))
TaxaJuros = float(input("Por gentileza, informe a taxa de juros: "))

for c in range(12):
    if c > 0: 
        ValorMensal = float(input("Informe o valor a ser depositado: "))
        ValorTotal = ValorTotal + ValorMensal
    ValorTotal = ValorTotal + ( ValorTotal * (TaxaJuros/100 ))
    print(f"No mes {c +1} o valor total com juros foi de: {ValorTotal:.2f}")
