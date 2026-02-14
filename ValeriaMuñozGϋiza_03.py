a=int(input("Dame el primer número entero: "))
b=int(input("Dame el segundo número entero: "))
c=int(input("Dame el tercer número entero: "))

suma=a+b+c
promedio=suma/3
if a>b and a>c:
    mayor= a
    print(f"El mayor es {a}")
elif b>a and b>c:
    mayor= b
    print(f"El mayor es {b}")
elif c>a and c>b:
    mayor= c
    print(f"El mayor es {c}")

if a==b:
    igual= [a,b]
    print(f"Hay dos numeros iguales: {igual}")
    if a==c:
        print(f"El tercer numero igual es {c}")

   
elif b==c:
    igual= [b,c]
    print(f"Hay dos numeros iguales: {igual}")
   
elif c==a:
    igual= [c,a]
    print(f"Hay dos numeros iguales: {igual}")

   
print(f"La suma es {suma}")
print(f"El promedio es {promedio}")




