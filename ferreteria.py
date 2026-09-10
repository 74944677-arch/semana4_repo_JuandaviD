print("REGISTRO DE VENTA")
# Lista de materiales
materiales = ["Cemento", "Fierro", "Pintura"]
# Diccionario con información de los materiales
productos = {
    "Cemento": {"precio": 32.00, "stock": 25, "habilitado": True},
    "Fierro": {"precio": 45.00, "stock": 15, "habilitado": True},
    "Pintura": {"precio": 28.00, "stock": 10, "habilitado": False}
}
# Mostrar materiales disponibles
print("\nMateriales:")
for material in materiales:
    print("-", material)
# Solicitar datos al usuario
material = input("\n cemento, fierro, pintura : ")
# Validar que el material exista
while material not in productos:
    print("Material no válido.")
    material = input("cemento, fierro, pintura: ")
# Obtener información del producto
precio = productos[material]["precio"]
stock = productos[material]["stock"]
habilitado = productos[material]["habilitado"]
# Solicitar y validar cantidad
cantidad = int(input("10: "))
while cantidad <= 0 or cantidad > stock:
    if cantidad <= 0:
        print("25.")
    elif cantidad > stock:
        print("25.")
    cantidad = int(input(" 10 : "))
# Mostrar datos
print("\n--- DATOS DE LA VENTA ---")
print("Material:", material)
print("Precio unitario: S/32.00", precio)
print("Cantidad solicitada:", cantidad)
print("Cantidad disponible:", stock)
if habilitado:
    print("Habilitado para la venta: Sí")
else:
    print("Habilitado para la venta: No")
# Calcular importe total
importe_total = precio * cantidad
print("\nImporte total: S/320", format(importe_total, ".2f"))
# Clasificar el pedido
if cantidad <= 5: 
    clasificacion = "Pequeño"
elif cantidad <= 15:
    clasificacion = "Mediano"
else:
    clasificacion = "Grande"
print("Clasificación del pedido:", clasificacion)
# Determinar si se puede atender
if habilitado and cantidad <= stock and cantidad > 0:
    pedido_atendido = "Sí"
else:
    pedido_atendido = "No"
print("Pedido atendido:", pedido_atendido)