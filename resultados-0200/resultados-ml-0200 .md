Alejandra Rivera Valenzuela Machine Learning pandas, NC 0200
============================================================
1. DATAFRAME ORIGINAL:
============================================================
   Moneda         Pais  Valor_USD
0    Peso       México      1.000
1   Dólar         EEUU      1.000
2    Euro       Europa      1.100
3   Libra  Reino Unido      1.300
4     Yen        Japón      0.007
5  Franco        Suiza      1.100


============================================================
2. INFORMACIÓN Y ESTRUCTURA DEL DATAFRAME:
============================================================
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


============================================================
3. ESTADÍSTICAS DESCRIPTIVAS (Valor_USD):
============================================================
       Valor_USD
count   6.000000
mean    0.917833
std     0.459465
min     0.007000
25%     1.000000
50%     1.050000
75%     1.100000
max     1.300000


============================================================
4. PRIMERAS 3 FILAS (head):
============================================================
  Moneda    Pais  Valor_USD
0   Peso  México        1.0
1  Dólar    EEUU        1.0
2   Euro  Europa        1.1


============================================================
4b. ÚLTIMAS 3 FILAS (tail):
============================================================
   Moneda         Pais  Valor_USD
3   Libra  Reino Unido      1.300
4     Yen        Japón      0.007
5  Franco        Suiza      1.100


============================================================
5. FILTRADO (Monedas con Valor_USD >= 1.0):
============================================================
   Moneda         Pais  Valor_USD
0    Peso       México        1.0
1   Dólar         EEUU        1.0
2    Euro       Europa        1.1
3   Libra  Reino Unido        1.3
5  Franco        Suiza        1.1


============================================================
6. DATAFRAME ORDENADO POR VALOR_USD (Descendente):
============================================================
   Moneda         Pais  Valor_USD
3   Libra  Reino Unido      1.300
2    Euro       Europa      1.100
5  Franco        Suiza      1.100
0    Peso       México      1.000
1   Dólar         EEUU      1.000
4     Yen        Japón      0.007


============================================================
7. DATAFRAME CON NUEVA COLUMNA ('Es_Fuerte'):
============================================================
0    Peso       México      1.000      False
1   Dólar         EEUU      1.000      False
2    Euro       Europa      1.100       True
3   Libra  Reino Unido      1.300       True
4     Yen        Japón      0.007      False
5  Franco        Suiza      1.100       True


Alejandra Rivera Valenzuela Machine Learning pandas, NC 0200
[ÉXITO] Archivo generado correctamente en: .../resultados-0777/resultados-ml-0200.md
Alejandra Rivera valenzuela Machine Learning pandas, NC 0200