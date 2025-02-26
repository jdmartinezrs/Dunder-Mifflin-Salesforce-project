import os
import pandas as pd

# Obtener el directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas de los archivos CSV
ruta_pedidos = os.path.join(script_dir, "../reducidos/pedidos_actualizados.csv")
ruta_productos = os.path.join(script_dir, "../documents/ProductoExport.csv")
ruta_salida = os.path.join(script_dir, "../reducidos/pedidos_actualizadosFinal.csv")

# Cargar los archivos CSV
pedidos_df = pd.read_csv(ruta_pedidos, dtype=str, encoding="utf-8")
productos_df = pd.read_csv(ruta_productos, dtype=str, encoding="utf-8")

# Crear diccionario de mapeo para productos
producto_dict = dict(zip(productos_df["Nombre del Producto"], productos_df["Record ID"]))

# Reemplazar los valores en la columna "Producto Comprado"
pedidos_df["Producto Comprado"] = pedidos_df["Producto Comprado"].map(producto_dict)

# Eliminar filas donde no se encontró un Record ID para Producto Comprado
pedidos_df = pedidos_df.dropna(subset=["Producto Comprado"])

# Guardar el nuevo archivo CSV corregido
pedidos_df.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"✅ Archivo 'pedidos_actualizados.csv' generado correctamente en: {ruta_salida}")