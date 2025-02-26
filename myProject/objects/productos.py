import pandas as pd
import os
import chardet

# Obtener la ruta del script
script_dir = os.path.dirname(__file__)

# Rutas de los archivos CSV
ruta_csv = os.path.join(script_dir, "../documents/PRODUCTOS.csv")
ruta_salida = os.path.join(script_dir, "../correctedDocuments/PRODUCTOS.csv")

# 📌 1️⃣ Detectar la codificación del archivo
with open(ruta_csv, "rb") as f:
    resultado = chardet.detect(f.read())
    encoding_detectado = resultado["encoding"]

print(f"📢 Codificación detectada: {encoding_detectado}")

# 📌 2️⃣ Cargar el archivo en UTF-8 sin modificar caracteres
try:
    df = pd.read_csv(ruta_csv, encoding="utf-8", dtype=str)  # Forzar UTF-8
except UnicodeDecodeError:
    df = pd.read_csv(ruta_csv, encoding=encoding_detectado, dtype=str)  # Usar la codificación detectada

# 📌 3️⃣ Corregir valores negativos en la columna de stock
if "Stock Disponible" in df.columns:
    df["Stock Disponible"] = pd.to_numeric(df["Stock Disponible"], errors='coerce').fillna(0).apply(lambda x: max(x, 0))

# 📌 4️⃣ Formatear "Precio Unitario" con exactamente 2 decimales y sin símbolos
def formatear_precio(precio):
    try:
        if pd.isna(precio) or precio == "":
            precio = 10.00
        else:
            precio = str(precio).replace(',', '').replace('$', '')
            precio = float(precio)
        return "{:.2f}".format(precio)
    except ValueError:
        return "10.00"

if "Precio Unitario" in df.columns:
    df["Precio Unitario"] = df["Precio Unitario"].apply(formatear_precio)

# 📌 5️⃣ Eliminar duplicados basados en "Nombre del Producto" y "Proveedor"
if "Nombre del Producto" in df.columns and "Proveedor" in df.columns:
    df = df.drop_duplicates(subset=["Nombre del Producto", "Proveedor"])

# 📌 6️⃣ Guardar el archivo corregido en UTF-8 sin BOM
df.to_csv(ruta_salida, index=False, encoding="utf-8", lineterminator='\n')

print(f"✅ Archivo corregido guardado en '{ruta_salida}' en formato UTF-8")
