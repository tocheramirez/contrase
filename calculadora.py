
menu="""
1-suma
2-resta
3-suma
4- divicion
"""

print('calculadora')
opcion = int(input(menu))
if opcion== 1:
   nu1=int(input())
   nu2=int(input())
   resultado = nu1+ nu2
   print(resultado)
elif opcion == 2:
    nu1=int(input())
    nu2=int(input())
    resultado = nu1 - nu2
    print(resultado)
elif opcion== 3:
    nu1=int(input())
    nu2=int(input())
    resultado = nu1 * nu2
    print(resultado)
elif opcion== 3:
    nu1=int(input())
    nu2=int(input())
    resultado = nu1 / nu2
    print(resultado)
else:
    print("ingrese una obcion correcta")
