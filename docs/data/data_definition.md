# Definición de los datos

## Origen de los datos

- Los datos fueron obtenidos de la FRED (Federal Reserve Economic Data).

### Tasa de Interés
- La serie de la tasa de interés fue obtenida de la FRED en el siguiente link: [DFEDTARU Series](https://fred.stlouisfed.org/series/DFEDTARU).
  - Es importante distinguir entre esta serie y la serie de la tasa efectiva de los fondos federales.
  - DFEDTARU representa el límite superior del rango objetivo de los fondos federales establecido por el Comité Federal de Mercado Abierto (FOMC).

### Serie de Inflación
- La serie de inflación también fue obtenida de la FRED: [CPIAUCSL Series](https://fred.stlouisfed.org/series/CPIAUCSL).
  - Para construir la brecha de inflación, se restó el valor de la inflación objetivo de USA (2% anual) de esta serie.

### Brecha del Producto
- La serie de brecha del producto fue obtenida del FRED: [FRED Graph](https://fred.stlouisfed.org/graph/?g=f1cZ).
  - La serie tiene frecuencia trimestral pero fue mensualizada en R con la librería tempdisagg.

### Índices de Halconismo y Palomismo
- Los índices de halconismo y palomismo fueron construidos en el diplomado anterior de procesamiento de lenguaje natural.
  - BERT-uncased fue re-entrenado con etiquetas de halconismo palomismo.

## Especificación de los scripts para la carga de datos

- El script para la carga de datos así como la base de datos (Muy pequeña) se encuentra dentro de este repositorio.
  - Más específicamente, la carga de datos se realiza en el siguiente enlace [Carga-Datos](https://github.com/peterpaulcc/BERTFED/blob/master/docs/business_understanding/Carga%20de%20Datos.py)

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- La ubicación de los archivos de los datos fue mencionada previamente.
- La estructura de los datos es de series de tiempo, es decir, series que están indexadas en el tiempo.
- No se requirió de limpieza de los datos.

### Base de datos de destino

- La base de datos de destino se encuentra en el repositorio, accesible en [DataLstmandPronostic](https://github.com/peterpaulcc/BERTFED/tree/master/docs/business_understanding).
- Es una base de datos estructurada indexada por fechas.
- Describir los procedimientos de carga y transformación de los datos en la base de datos de destino:
  - Se importa la biblioteca Pandas.
  - Se define la ruta al archivo Excel.
  - Se carga el archivo Excel.
  - Cada hoja del archivo Excel se guarda como un archivo CSV, nombrado igual que la hoja de Excel y sin incluir el índice del DataFrame.
