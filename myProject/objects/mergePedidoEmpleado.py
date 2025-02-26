import os
import pandas as pd

# Obtener el directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas de los archivos CSV
ruta_pedidos = os.path.join(script_dir, "../reducidos/pedidos_actualizados.csv")
ruta_empleados = os.path.join(script_dir, "../documents/ClienteExport.csv")
ruta_salida = os.path.join(script_dir, "../reducidos/pedidos_actualizados1.csv")

# Cargar los archivos CSV
pedidos_df = pd.read_csv(ruta_pedidos, dtype=str, encoding="utf-8")
empleados_df = pd.read_csv(ruta_empleados, dtype=str, encoding="utf-8")

# Crear un diccionario de mapeo entre "Nombre del Empleado" y "Record ID"
empleado_dict = dict(zip(empleados_df["Nombre del Empleado"], empleados_df["Record ID"]))

# Reemplazar los valores en la columna "Ejecutivo Responsable" con los Record ID
pedidos_df["Ejecutivo Responsable"] = pedidos_df["Ejecutivo Responsable"].map(empleado_dict)

# Eliminar filas donde no se encontró un Record ID
pedidos_df = pedidos_df.dropna(subset=["Ejecutivo Responsable"])

# Guardar el nuevo archivo CSV corregido
pedidos_df.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"✅ Archivo 'pedidos_actualizados.csv' generado correctamente en: {ruta_salida}")