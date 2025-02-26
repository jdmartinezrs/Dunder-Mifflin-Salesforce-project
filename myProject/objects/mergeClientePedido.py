import os
import pandas as pd

# Obtener el directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas de los archivos CSV
ruta_pedidos = os.path.join(script_dir, "../reducidos/pedidos_filtrados1.csv")
ruta_empleados = os.path.join(script_dir, "../documents/EmpleadoExport.csv")
ruta_clientes = os.path.join(script_dir, "../documents/ClienteExport.csv")
ruta_salida = os.path.join(script_dir, "../reducidos/pedidos_actualizados.csv")

# Cargar los archivos CSV
pedidos_df = pd.read_csv(ruta_pedidos, dtype=str, encoding="utf-8")
empleados_df = pd.read_csv(ruta_empleados, dtype=str, encoding="utf-8")
clientes_df = pd.read_csv(ruta_clientes, dtype=str, encoding="utf-8")

# Crear diccionarios de mapeo
empleado_dict = dict(zip(empleados_df["Nombre del Empleado"], empleados_df["Record ID"]))
cliente_dict = dict(zip(clientes_df["Nombre_de_la_Empresa__c"], clientes_df["Id"]))

# Reemplazar los valores en las columnas correspondientes
pedidos_df["Ejecutivo Responsable"] = pedidos_df["Ejecutivo Responsable"].map(empleado_dict)
pedidos_df["Cliente"] = pedidos_df["Cliente"].map(cliente_dict)

# Eliminar filas donde no se encontró un Record ID o Cliente ID
pedidos_df = pedidos_df.dropna(subset=["Ejecutivo Responsable", "Cliente"])

# Guardar el nuevo archivo CSV corregido
pedidos_df.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"✅ Archivo 'pedidos_actualizados.csv' generado correctamente en: {ruta_salida}")