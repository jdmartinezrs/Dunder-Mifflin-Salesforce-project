import pandas as pd
import os

# Obtener la ruta del script
script_dir = os.path.dirname(__file__)

# Rutas de los archivos CSV
ruta_csv = os.path.join(script_dir, "../reducidos/pedidos_filtrados.csv")
ruta_salida = os.path.join(script_dir, "../reducidos/pedidos_filtrados1.csv")

# Cargar el archivo CSV con la codificación correcta
df = pd.read_csv(ruta_csv, encoding="latin1")

# Reemplazar caracteres mal interpretados
df = df.map(lambda x: x.encode('latin1').decode('utf-8') if isinstance(x, str) else x)

# Formatear fechas a YYYY-MM-DD
df['Fecha del Pedido'] = pd.to_datetime(df['Fecha del Pedido'], errors='coerce').dt.strftime('%Y-%m-%d')

# Reemplazar valores vacíos en "Monto Total" por 50,000 y asegurar 2 decimales
df["Monto Total"] = df["Monto Total"].fillna(50000).astype(float).apply(lambda x: f"{x:.2f}")

# Corregir estados mal escritos
dict_correccion_estados = {
    "Pendientee": "Pendiente",
    "Entregadoo": "Entregado",
    "Evido": "Enviado"
}
df["Estado del Pedido"] = df["Estado del Pedido"].replace(dict_correccion_estados)

# Asegurar que solo haya un producto comprado por registro
df["Producto Comprado"] = df["Producto Comprado"].astype(str).apply(lambda x: x.split(",")[0])

# Guardar el archivo corregido
df.to_csv(ruta_salida, index=False, encoding="utf-8")

print(f"Archivo corregido guardado en '{ruta_salida}'")
