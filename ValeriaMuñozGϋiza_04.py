
#Recreando los espacios de un tablero de ajedrez con una matriz cuadrada 8x8

espacio=1

for i in range (1,9):
    for j in range(1,9):
        print(f"{espacio:2d}", end=" ")
        espacio +=1
    print()

