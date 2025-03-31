#crear lista para almacenar ventas de la semana
ventas=[]
#usar un ciclo para ingresar las ventas 
for i in range(7): 
    venta=float(input(f"ingrese las ventas del dia {i+1}: "))
    ventas.append(venta)

print(ventas)

#procesar los datos
total_ventas=sum(ventas)
promedio_ventas=total_ventas/len(ventas)

#condicion para verificar si se alcanzo la meta
meta=5000

if total_ventas>=meta: 
    mensaje="felicidades haz alcanzado la meta"
else:
    mensaje="no se alcanzo la meta"

#imprimir resultado

print("\n----reporte---")
print(f"total de ventas:${total_ventas}")
print(f"promedio ${promedio_ventas}")
print(mensaje)
