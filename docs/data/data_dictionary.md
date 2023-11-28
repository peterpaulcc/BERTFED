# Diccionario de datos

## Base de datos 1: Data LSTM and Pronostic

**Descripción de la tabla o fuente de datos:** Esta base de datos contiene diversas series de tiempo relacionadas con indicadores económicos y financieros clave.

### SentimentIndex (Índices de Sentimiento)

| Variable  | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --------- | ----------- | ------------ | ---------------------- | --------------- |
| Date      | Fecha del registro | Fecha | Varía | Comunicados de la FED |
| INDEX1    | Índice de sentimiento ponderado por igual | Numérico | Varía | BERT-UNCASED con etiquetas de halconismo y palomismo |
| INDEX2    | Índice de sentimiento ponderado por longitud de la oración | Numérico | Varía | BERT-UNCASED con etiquetas de halconismo y palomismo |
| INDEX3    | Índice de sentimiento con umbrales de halconismo | Numérico | Varía | BERT-UNCASED con etiquetas de halconismo y palomismo |

### Tasa de Interés (Fedrate rate daily)

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| -------- | ----------- | ------------ | ---------------------- | --------------- |
| Date     | Fecha del registro | Fecha | Varía | [DFEDTARU Series](https://fred.stlouisfed.org/series/DFEDTARU) |
| Rate     | Tasa de interés diaria | Numérico | Varía | FRED |

### Fedfunds (Fondos Federales)

| Variable      | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| ------------- | ----------- | ------------ | ---------------------- | --------------- |
| Date          | Fecha del registro | Fecha | Varía | FRED |
| FEDFUNDS      | Tasa de fondos federales | Numérico | Varía | FRED |
| tipo_politica | Tipo de política monetaria | Numérico | -1, 0, 1 | FRED |

### InflationGAP (Brecha de Inflación)

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| -------- | ----------- | ------------ | ---------------------- | --------------- |
| Date     | Fecha del registro | Fecha | Varía | [CPIAUCSL Series](https://fred.stlouisfed.org/series/CPIAUCSL) |
| Inflation | Inflación actual | Numérico | Varía | FRED |
| GAP      | Brecha de inflación | Numérico | Varía | FRED |

### OutputGAP (Brecha del Producto)

| Variable    | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| ----------- | ----------- | ------------ | ---------------------- | --------------- |
| Observation | Fecha del registro | Fecha | Varía | [FRED Graph](https://fred.stlouisfed.org/graph/?g=f1cZ) |
| Output_Gap  | Brecha del producto | Numérico | Varía | FRED |
