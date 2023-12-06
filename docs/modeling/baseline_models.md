# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es una Red Neuronal Recurrente con arquitectura LSTM (Long Short-Term Memory), diseñada para pronosticar la tasa de interés `FEDRATE`. Este es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores.

## Variables de entrada

Las variables de entrada utilizadas en el modelo son:
- `INDEX1`
- `Inflation GAP`
- `Output GAP`

## Variable objetivo

La variable objetivo utilizada en el modelo es `FEDRATE`, que representa la tasa de interés federal.

## Evaluación del modelo

### Métricas de evaluación

Las métricas utilizadas para evaluar el rendimiento del modelo son:
- Pérdida durante el entrenamiento (Train Loss)
- Pérdida durante la prueba (Test Loss)

### Resultados de evaluación

Los resultados de la evaluación del modelo baseline son los siguientes:

| Métrica       | Valor                   |
|---------------|-------------------------|
| Train Loss    | 0.05270108953118324     |
| Test Loss     | 0.04109855368733406     |

## Análisis de los resultados

El modelo baseline muestra una pérdida baja tanto en el conjunto de entrenamiento como en el de prueba, indicando un buen ajuste del modelo a los datos. Sin embargo, es importante considerar la posibilidad de sobreajuste y realizar pruebas adicionales para confirmar la generalización del modelo.

## Conclusiones

El modelo baseline proporciona una base sólida para el pronóstico de `FEDRATE`. Las futuras iteraciones del modelo podrían explorar la inclusión de más variables de entrada, ajustes en la arquitectura de la red o el uso de diferentes hiperparámetros para mejorar la precisión y la robustez del modelo.

## Referencias

- Documentación de Keras y LSTM para la construcción de modelos de redes neuronales recurrentes.
- Datos históricos de tasas de interés y variables económicas para el entrenamiento del modelo.
