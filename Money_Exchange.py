def exchange(pesos_type, value_usd):
    usd = input("How many USD you want to exchange? ")
    usd = float(usd)
    pesos = usd / value_usd
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("You currently have $" + pesos )
menu = """
Welcome to the Money Exchange 💲

1. COP
2. ARG
3. MXN

Choose one of the currencies in order to exchange it to USD.

"""
 
opcion = input(menu) 

if opcion == "1":
    exchange("COP", 0.00027)
elif opcion == "2":
    exchange("ARG", 0.014)
elif opcion == "3":
    exchange("MXN", 0.045)
else:
    print("Choose a valid option")

