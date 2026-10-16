notas = float(input("Mi nota es "))

if notas < 0 or notas > 10:
    print("Nota no válida")
elif notas < 5:
    print("Suspenso")
elif notas <7:
    print("Aprobado")
elif notas <9:
    print("Notable")
else:
    print("Sobresaliente")