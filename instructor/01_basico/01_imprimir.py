
#Mi primera ejecusion
print('Python Ejecutandose 1111')


"""
"""
print('Python Ejecutandose 2222')


#Variables
# nombre = valor
# nombre:tipo = valor

nombre_completo='Luis Perez'
edad = 35

print(type(nombre_completo))
print(type(edad))

# 1) Clasico (Texto + Variables)
print('Nombre='+nombre_completo+'y edad'+ str(edad))

# 2) Concatenar Texto + Variables con comas
print('Nombre=',nombre_completo,'y Edad=', str(edad))

# 3) Concatenar Texto + Variables con formato rapido
print(f'Nombre = {nombre_completo} y Edad={edad} ')

# 4) Concatenar Texto + Variables con formato general
mensaje = 'Nombre = {0} y Edad={1} '
#print(mensaje.format(nombre_completo,edad))
print(mensaje.format("Ana Sanchez",25))

# Futuro/Profesionales
"""
nombre_completo2:str='Luis Perez'
edad2:int = 35
"""