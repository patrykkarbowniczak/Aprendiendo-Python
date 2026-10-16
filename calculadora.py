cuenta = float(input("¿Cuanto es la cuenta? "))
porcentaje = float(input("¿Cuanta propina quiere dejar? "))

propina = cuenta * porcentaje / 100
total = cuenta + propina

print("Su cuentas es de", cuenta, "más la propina", propina, "el total sería de", total)
