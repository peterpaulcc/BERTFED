# Reporte del Modelo Final

## Resumen Ejecutivo

Este modelo LSTM ha demostrado ser efectivo en la predicción de la tasa de interés `FEDRATE`. Con una pérdida de entrenamiento de 0.0527 y una pérdida de prueba de 0.0411, el modelo muestra una capacidad significativa para adaptarse y predecir con precisión la serie temporal dada.

## Descripción del Problema

El objetivo principal de este modelo era pronosticar la tasa de interés federal (`FEDRATE`), un indicador clave en la economía. Dada su importancia en la formulación de políticas económicas y su impacto en los mercados financieros, un modelo preciso para predecir `FEDRATE` es de gran valor para economistas y analistas financieros.

## Descripción del Modelo

El modelo final es una Red Neuronal Recurrente (RNN) con una arquitectura LSTM. Fue entrenado con variables como `INDEX1`, `Inflation GAP` y `Output GAP` para predecir `FEDRATE`. Se utilizó el escalado MinMax para normalizar los datos y se implementó una división de 80/20 para los conjuntos de entrenamiento y prueba.

## Evaluación del Modelo

El modelo se evaluó utilizando la pérdida de entrenamiento y de prueba como métricas principales. Estas métricas indican qué tan bien el modelo ha aprendido de los datos de entrenamiento y qué tan bien generaliza a nuevos datos.

| Métrica       | Valor                   |
|---------------|-------------------------|
| Train Loss    | 0.05270108953118324     |
| Test Loss     | 0.04109855368733406     |

## Conclusiones y Recomendaciones

El modelo demuestra ser un punto de partida sólido para pronosticar `FEDRATE`. Sin embargo, se recomienda explorar la inclusión de más variables y probar diferentes arquitecturas de red para mejorar aún más su precisión. Además, sería prudente implementar técnicas para evitar el sobreajuste y validar la generalización del modelo.

## Referencias

- Documentación de Keras y LSTM para la implementación de modelos de redes neuronales.
- Datos históricos de tasas de interés y variables económicas.
