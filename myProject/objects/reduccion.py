import pandas as pd
import os

# Obtener la ruta del script
script_dir = os.path.dirname(__file__)

# Rutas de los archivos CSV
ruta_clientes = os.path.join(script_dir, "../correctedDocuments/clientes_filtrados.csv")
ruta_pedidos = os.path.join(script_dir, "../correctedDocuments/pedidos_filtrados.csv")
ruta_empleados = os.path.join(script_dir, "../correctedDocuments/EMPLEADOS.csv")
ruta_productos = os.path.join(script_dir, "../correctedDocuments/PRODUCTOS.csv")

ruta_clientes_salida = os.path.join(script_dir, "../reducidos/clientes_filtrados.csv")
ruta_pedidos_salida = os.path.join(script_dir, "../reducidos/pedidos_filtrados.csv")
ruta_empleados_salida = os.path.join(script_dir, "../reducidos/empleados_filtrados.csv")
ruta_productos_salida = os.path.join(script_dir, "../reducidos/productos_filtrados.csv")

# Cargar datos
df_clientes = pd.read_csv(ruta_clientes, encoding="latin1")
df_pedidos = pd.read_csv(ruta_pedidos, encoding="latin1")
df_empleados = pd.read_csv(ruta_empleados, encoding="latin1")
df_productos = pd.read_csv(ruta_productos, encoding="latin1")

# Asegurar que "Volumen de Compra Mensual" tenga siempre dos decimales
df_clientes["Volumen de Compra Mensual"] = df_clientes["Volumen de Compra Mensual"].astype(float).apply(lambda x: f"{x:.2f}")

# Filtrar "Tipo de Cliente" para que solo contenga valores válidos
tipos_validos = {"Pequeña Empresa", "Mediana Empresa", "Corporativo", "Gobierno"}
df_clientes["Tipo de Cliente"] = df_clientes["Tipo de Cliente"].apply(lambda x: x if x in tipos_validos else "Corporativo")

# Filtrar empleados referenciados en clientes o pedidos
empleados_referenciados = set(df_clientes["Ejecutivo de Cuenta"]).union(set(df_pedidos["Ejecutivo Responsable"]))
df_empleados = df_empleados[df_empleados["Nombre del Empleado"].isin(empleados_referenciados)]

# Reducir empleados en un 25%
df_empleados = df_empleados.sample(frac=0.75, random_state=42)

# Filtrar clientes con ejecutivo válido
df_clientes = df_clientes[df_clientes["Ejecutivo de Cuenta"].isin(df_empleados["Nombre del Empleado"])]

# Reducir clientes en un 15%
df_clientes = df_clientes.sample(frac=0.85, random_state=42)

# Filtrar pedidos con cliente y ejecutivo válido
df_pedidos = df_pedidos[df_pedidos["Cliente"].isin(df_clientes["Nombre de la Empresa"]) & df_pedidos["Ejecutivo Responsable"].isin(df_empleados["Nombre del Empleado"])]

# Reducir pedidos en un 20%
df_pedidos = df_pedidos.sample(frac=0.8, random_state=42)

# Filtrar productos que aparecen en los pedidos
productos_referenciados = set(df_pedidos["Producto Comprado"].str.split(", ").explode())
df_productos = df_productos[df_productos["Nombre del Producto"].isin(productos_referenciados)]

# Reducir productos en un 17%
df_productos = df_productos.sample(frac=0.83, random_state=42)

# Guardar los archivos filtrados
df_clientes.to_csv(ruta_clientes_salida, index=False, encoding="utf-8")
df_pedidos.to_csv(ruta_pedidos_salida, index=False, encoding="utf-8")
df_empleados.to_csv(ruta_empleados_salida, index=False, encoding="utf-8")
df_productos.to_csv(ruta_productos_salida, index=False, encoding="utf-8")

print("Archivos corregidos y guardados en la carpeta 'reducidos'")