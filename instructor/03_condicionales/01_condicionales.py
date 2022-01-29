venta=4000
comision=0.0
total_venta=0.
#Si venta > 3000 , comision 10%
#Caso contrario 1%


if venta>=3000 :
    comision=0.10
else :
    comision=0.01

total_venta = venta + (venta*comision)

print('Total Venta=',total_venta,', Comision=',comision)

# Accion + parametro/valor

# cd carpeta
# python archivo.py

