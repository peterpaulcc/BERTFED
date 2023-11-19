# Project Charter - Entendimiento del Negocio-Marco del Proyecto 
## PEDRO PABLO CALDERÓN
## ANDRÉS DAVID NIVIA
## Nombre del Proyecto

Entrenamiento de Red Neuronal LSTM para Pronósticos de Inflación

## Objetivo del Proyecto

Desarrollar un modelo de red neuronal LSTM que mejore la precisión de los pronósticos de la inflación en EE. UU., integrando variables económicas tradicionales con un índice de halconismo y palomismo basado en las posturas comunicadas por la FED. El control de las versiones de esta red se realizará con MLflow para poder encontrar los mejores parámetro.

## Alcance del Proyecto

### Incluye:

- Análisis y procesamiento de series temporales económicas.
- Reentrenamiento y ajuste de un modelo BERT uncased para la generación de un índice de halconismo y palomismo.
- Desarrollo y validación de una red neuronal LSTM para la predicción de inflación.
- Implementación de MLflow para el seguimiento y control del entrenamiento del modelo.

### Excluye:

- Análisis de variables macroeconómicas no relacionadas directamente con la inflación.
- Modelos de pronóstico que no utilizan técnicas de Deep Learning.

## Metodología

Se seguirá una metodología ágil para el desarrollo del modelo, con iteraciones semanales, revisiones continuas y adaptaciones basadas en los resultados obtenidos y el feedback del equipo de proyecto.

## Cronograma

| Etapa                                  | Duración Estimada | Fechas                      |
|---------------------------------------|------------------|-----------------------------|
| Entendimiento del negocio y carga de datos | 2 semanas        |
| Preprocesamiento y análisis exploratorio    | 1 semanas        |
| Modelamiento y extracción de características | 1 semanas        | 
| Despliegue                               | 1 semanas        |
| Evaluación y entrega final                | 1 semanas        | 

*Las fechas son tentativas y sujetas a ajustes según la evolución del proyecto.

## Equipo del Proyecto

- [PEDRO CALDERON], Ingeniero de ML, Economista
- [ANDRES DAVID NIVIA], Analista de Datos, Economista 


## Presupuesto

El presupuesto para este proyecto está cubierto por completo por el equipo del proyecto 

## Stakeholders

- [Banrep ], Jefe de Política Monetaria


Los stakeholders tendrán revisiones periódicas del progreso y se espera que proporcionen orientación y validación en cada etapa del proyecto.

## Aprobaciones

- [Nombre del aprobador], Director de Análisis Económico
- Firma: ___________________
- Fecha de aprobación: _______

---

## Información Adicional del Proyecto Anterior

### Trasfondo del Negocio

**Cliente o beneficiarios del proyecto**: El cliente principal es el Banco, con economistas y analistas financieros como beneficiarios indirectos.

**Dominio**: Economía y política monetaria.

**Problemas del negocio**: Predicción de la inflación basada en variables económicas tradicionales y comunicados de la FED que informan sobre las posturas de halconismo y palomismo.

### Alcance

**Solución basada en Deep Learning**: Implementación de una red neuronal LSTM para pronosticar la inflación.

**Uso del producto**: El modelo ayudará al Banco a tomar decisiones informadas sobre política monetaria.

### Datos

**Origen de los datos**: Comunicados de la FED y series de tiempo de fuentes oficiales como FRED y el Banco Mundial.

**Herramienta o proceso**: API de Google Drive para descargar archivos y reentrenamiento de BERT uncased.

**Tipo de datos**: Textuales de comunicados de la FED y datos tabulares de series de tiempo.

### Resumen de la Calidad de los datos

Hay algunos datos faltantes, pero el conjunto de datos es consistente y adecuado para el análisis propuesto.

### Tipos de variables

La variable objetivo es la inflación, una variable continua, junto con el índice de halconismo-palomismo y variables tradicionales.

