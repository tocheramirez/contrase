def conversor(tipo_pesos, valor_dolar):
    pesos=float(input("cuantos pesos "+tipo_pesos  +" tienes?: "))
    dolares= pesos/valor_dolar
    dolares= round(dolares,2)
    dolares=str(dolares)
    print("tienes "+ dolares+" dolares")

menu="""
conversor de monedas
1- colones 
2- cordobas
3- pesos colombianos

Elige una moneda
"""
opcion = int(input(menu))

if opcion== 1:
    conversor("colones",625.06)
elif opcion == 2:
    conversor("nicaraguenses",36)
elif opcion== 3:
    conversor("colombianos",4610.01)

else:
    print("ingrese una obcion correcta")
