import pandas as pd
import os

# Obtener la ruta del script
script_dir = os.path.dirname(__file__)

# Rutas de los archivos CSV
ruta_clientes = os.path.join(script_dir, "../documents/CLIENTES.csv")
ruta_clientes_salida = os.path.join(script_dir, "../correctedDocuments/clientes_filtrados.csv")

# Procesar CLIENTES.csv
df_clientes = pd.read_csv(ruta_clientes, encoding="latin1")

# Asegurar que "Volumen de Compra Mensual" tenga siempre dos decimales
df_clientes["Volumen de Compra Mensual"] = df_clientes["Volumen de Compra Mensual"].astype(float).apply(lambda x: f"{x:.2f}")

# Filtrar "Tipo de Cliente" para que solo contenga valores válidos
tipos_validos = {"Pequeña Empresa", "Mediana Empresa", "Corporativo", "Gobierno"}
df_clientes["Tipo de Cliente"] = df_clientes["Tipo de Cliente"].apply(lambda x: x if x in tipos_validos else "Corporativo")

# Guardar el archivo corregido
df_clientes.to_csv(ruta_clientes_salida, index=False, encoding="utf-8")

print(f"Archivo corregido guardado en '{ruta_clientes_salida}'")
