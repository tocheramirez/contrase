#def imprimir_mensaje():
#    print('Mensaje especial: ')
 #   print('Estoy aprendiendo a usar funciones!!! ')

#imprimir_mensaje()

def conversacion(mensaje):
    print('hola')
    print('como estas')
    print(mensaje)
    print(' adios')

opcion= int(input('Eligue una opcion(1,2,3):'))
if opcion == 1:
    conversacion('elegiste la opcion 1')
elif opcion == 2:
    conversacion('elegiste la opcion 2')
elif opcion == 3:
    conversacion('elegiste la opcion 3')
else:
    print('escribe la oncion correcta')
    