import sys
import os
import io
import pandas as pd
import importlib.util

# 1. Ruta exacta al archivo dicc-0200.py
ruta_dicc = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "datos-de-entrada-ml-0200", "dicc-0200.py")
)

# 2. Cargar el módulo de forma dinámica
spec = importlib.util.spec_from_file_location("dicc_0200", ruta_dicc)
if spec is None or spec.loader is None:
    raise ImportError(f"No se pudo encontrar el archivo en: {ruta_dicc}")

dicc_0200 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dicc_0200)

nombre_estudiante = "Alejandra Rivera Valenzuela NC 0200"
print(nombre_estudiante)

# Variable para almacenar las salidas en Markdown
contenido_md = []
encabezado_pie = nombre_estudiante
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 3. Obtener el diccionario dinámicamente
diccionario_datos = None
if hasattr(dicc_0200, "datos_estaciones"):
    diccionario_datos = dicc_0200.datos_estaciones
elif hasattr(dicc_0200, "datos_estaciones_0200"):
    diccionario_datos = dicc_0200.datos_estaciones_0200
else:
    for atributo in dir(dicc_0200):
        if not atributo.startswith("__"):
            val = getattr(dicc_0200, atributo)
            if isinstance(val, dict):
                diccionario_datos = val
                break

if diccionario_datos is None:
    raise AttributeError("No se encontró ningún diccionario válido dentro de dicc-0200.py")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(diccionario_datos)

# Detectar nombres reales de columnas para evitar KeyError
col_pasajeros = next((c for c in df.columns if "pasajero" in c.lower()), df.columns[0])
col_trenes = next((c for c in df.columns if "tren" in c.lower()), df.columns[-1])

registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de la columna de pasajeros
registrar(f"3. Estadísticas Generales de la Columna '{col_pasajeros}'", df[col_pasajeros].describe())

# 4. Ordenar Ascendente por Pasajeros_dia
df_asc_pasajeros = df.sort_values(by=col_pasajeros, ascending=True)
registrar(f"4. Ordenar Ascendente por {col_pasajeros}", df_asc_pasajeros)

# 5. Ordenar Descendente por Trenes_dia
df_desc_trenes = df.sort_values(by=col_trenes, ascending=False)
registrar(f"5. Ordenar Descendente por {col_trenes}", df_desc_trenes)

# 7. Guardar el archivo resultados-ml-0200.md dentro de resultados-0200
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0200'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0200.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print(nombre_estudiante)