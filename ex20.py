dia = input("Digite o dia da semana: ").lower().strip()

if dia == "sábado" or dia == "domingo":
    print("Final de semana")
else:
    print("Dia útil")