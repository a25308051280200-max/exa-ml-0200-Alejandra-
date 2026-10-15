# Reporte de Análisis de Datos - Pandas

`Alejandra Rivera Valenzuela NC 0200`

## 1. DataFrame Convertido
```text
   Moneda         Pais  Valor_USD
0    Peso       México      1.000
1   Dólar         EEUU      1.000
2    Euro       Europa      1.100
3   Libra  Reino Unido      1.300
4     Yen        Japón      0.007
5  Franco        Suiza      1.100
```

## 2.1 Primeras Filas (head)
```text
  Moneda    Pais  Valor_USD
0   Peso  México        1.0
1  Dólar    EEUU        1.0
```

## 2.2 Últimas Filas (tail)
```text
   Moneda   Pais  Valor_USD
4     Yen  Japón      0.007
5  Franco  Suiza      1.100
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Moneda           str
Pais             str
Valor_USD    float64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Moneda     6 non-null      str    
 1   Pais       6 non-null      str    
 2   Valor_USD  6 non-null      float64
dtypes: float64(1), str(2)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Moneda'
```text
count        6
unique       6
top       Peso
freq         1
Name: Moneda, dtype: object
```

## 4. Ordenar Ascendente por Moneda
```text
   Moneda         Pais  Valor_USD
1   Dólar         EEUU      1.000
2    Euro       Europa      1.100
5  Franco        Suiza      1.100
3   Libra  Reino Unido      1.300
0    Peso       México      1.000
4     Yen        Japón      0.007
```

## 5. Ordenar Descendente por Valor_USD
```text
   Moneda         Pais  Valor_USD
3   Libra  Reino Unido      1.300
2    Euro       Europa      1.100
5  Franco        Suiza      1.100
0    Peso       México      1.000
1   Dólar         EEUU      1.000
4     Yen        Japón      0.007
```

`Alejandra Rivera Valenzuela NC 0200`