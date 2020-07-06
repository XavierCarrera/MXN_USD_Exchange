usd = input("How many USD you want to exchenge to MXN? ")
usd = float(usd)
mxn_value = 0.045
mxn = usd / mxn_value
mxn = round(mxn, 2)
mxn = str(mxn)
print("You currently have $" + mxn + " MXN")
