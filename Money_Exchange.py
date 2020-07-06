menu = """
Welcome to the Money Exchange 💲

1. COP
2. ARG
3. MXN

Choose one of the currencies in order to exchange to USD.

"""

opcion = input(menu)

if opcion == "1":
    usd = input("How many USD you want to exchenge to COP? ")
    usd = float(usd)
    cop_value = 0.00027
    cop = usd / cop_value
    cop = round(cop, 2)
    cop = str(cop)
    print("You currently have $" + cop + " COP")
elif opcion == "2":
    pass
    usd = input("How many USD you want to exchenge to ARG? ")
    usd = float(usd)
    arg_value = 0.014
    arg = usd / arg_value
    arg = round(arg, 2)
    arg = str(arg)
    print("You currently have $" + arg + " ARG")
elif opcion == "3":
    usd = input("How many USD you want to exchenge to MXN? ")
    usd = float(usd)
    mxn_value = 0.045
    mxn = usd / mxn_value
    mxn = round(mxn, 2)
    mxn = str(mxn)
    print("You currently have $" + mxn + " MXN")
else:
    print("Choose a valid option")


