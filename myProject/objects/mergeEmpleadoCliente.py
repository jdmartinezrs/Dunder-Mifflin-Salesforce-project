import os
import pandas as pd

# Obtener el directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas de los archivos CSV
ruta_clientes = os.path.join(script_dir, "../reducidos/clientes_filtrados.csv")
ruta_empleados = os.path.join(script_dir, "../documents/EmpleadoExport.csv")
ruta_salida = os.path.join(script_dir, "../reducidos/cliente_actualizado.csv")

# Cargar los archivos CSV
clientes_df = pd.read_csv(ruta_clientes, dtype=str)
empleados_df = pd.read_csv(ruta_empleados, dtype=str)

# Crear un diccionario de mapeo entre "Nombre del Empleado" y "Record ID"
empleado_dict = dict(zip(empleados_df["Nombre del Empleado"], empleados_df["Record ID"]))

# Reemplazar los valores en la columna "Ejecutivo de Cuenta" con los Record ID
clientes_df["Ejecutivo de Cuenta"] = clientes_df["Ejecutivo de Cuenta"].map(empleado_dict)

# Eliminar filas donde no se encontró un Record ID
clientes_df = clientes_df.dropna(subset=["Ejecutivo de Cuenta"])

# Guardar el nuevo archivo CSV corregido
clientes_df.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"✅ Archivo 'cliente_actualizado.csv' generado correctamente en: {ruta_salida}")