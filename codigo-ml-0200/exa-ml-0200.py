# ==============================================================================
# EXAMEN DE PANDAS
# Número de Lista: 49
# Nombre: Alejandra Rivera Valenzuela
# Número de Control: 0200
# ==============================================================================

import pandas as pd
print("Alejandra Rivera Valenzuela Machine Learning pandas, NC 0200")
# ------------------------------------------------------------------------------
# Punto 14: Selección e inicialización del diccionario asignado 
# ------------------------------------------------------------------------------
datos_monedas = {
    "Moneda": ["Peso", "Dólar", "Euro", "Libra", "Yen", "Franco"],
    "Pais": ["México", "EEUU", "Europa", "Reino Unido", "Japón", "Suiza"],
    "Valor_USD": [1.0, 1.0, 1.1, 1.3, 0.007, 1.1]
}

# ------------------------------------------------------------------------------
# 1. Crear el DataFrame a partir del diccionario
# ------------------------------------------------------------------------------
df = pd.DataFrame(datos_monedas)

print("="*60)
print("1. DATAFRAME ORIGINAL:")
print("="*60)
print(df)
print("\n")

# ------------------------------------------------------------------------------
# 2. Información general del DataFrame
# ------------------------------------------------------------------------------
print("="*60)
print("2. INFORMACIÓN Y ESTRUCTURA DEL DATAFRAME:")
print("="*60)
df.info()
print("\n")

# ------------------------------------------------------------------------------
# 3. Resumen estadístico descriptivo
# ------------------------------------------------------------------------------
print("="*60)
print("3. ESTADÍSTICAS DESCRIPTIVAS (Valor_USD):")
print("="*60)
print(df.describe())
print("\n")

# ------------------------------------------------------------------------------
# 4. Mostrar solo las primeras y últimas filas (head y tail)
# ------------------------------------------------------------------------------
print("="*60)
print("4. PRIMERAS 3 FILAS (head):")
print("="*60)
print(df.head(3))
print("\n")

print("="*60)
print("4b. ÚLTIMAS 3 FILAS (tail):")
print("="*60)
print(df.tail(3))
print("\n")

# ------------------------------------------------------------------------------
# 5. Filtrado de datos (Ejemplo: Monedas con Valor_USD mayor o igual a 1.0)
# ------------------------------------------------------------------------------
print("="*60)
print("5. FILTRADO (Monedas con Valor_USD >= 1.0):")
print("="*60)
filtro_valor = df[df["Valor_USD"] >= 1.0]
print(filtro_valor)
print("\n")

# ------------------------------------------------------------------------------
# 6. Ordenar datos por columna (Valor_USD de mayor a menor)
# ------------------------------------------------------------------------------
print("="*60)
print("6. DATAFRAME ORDENADO POR VALOR_USD (Descendente):")
print("="*60)
df_ordenado = df.sort_values(by="Valor_USD", ascending=False)
print(df_ordenado)
print("\n")

# ------------------------------------------------------------------------------
# 7. Agregar una nueva columna calculada o condicional
# ------------------------------------------------------------------------------
print("="*60)
print("7. DATAFRAME CON NUEVA COLUMNA ('Es_Fuerte'):")
print("="*60)
# Agrega True si el valor es mayor a 1.0 USD, de lo contrario False
df["Es_Fuerte"] = df["Valor_USD"] > 1.0
print(df)
print("\n")
print("Alejandra Rivera Valenzuela Machine Learning pandas, NC 0200")