# Informe de salida

## Resumen Ejecutivo

Este informe abarca el desarrollo y despliegue de un modelo de machine learning de Random Forest diseñado para predecir tasas, como la FED RATE, basándose en datos económicos. El proyecto pasó por varias fases, incluyendo la recolección de datos, preprocesamiento, modelado, evaluación y despliegue. El éxito del proyecto se mide por la precisión del modelo y su potencial para proporcionar insights valiosos que podrían influir en la toma de decisiones económicas.

## Resultados del proyecto

- Se implementaron modelos LSTM y Random Forest, con un enfoque en mejorar la precisión de las predicciones de tasas.
- El modelo de Random Forest superó al modelo base LSTM, con una pérdida de test significativamente menor.
- Los resultados indican que el modelo de Random Forest puede ser una herramienta valiosa para prever cambios en las tasas de interés, lo que tiene implicaciones directas en la planificación y estrategia financiera.

## Evaluación Técnica de Modelos

Durante la fase de evaluación, comparamos dos modelos LSTM, uno original y otro ampliado, con un modelo de Random Forest utilizando la métrica de error cuadrático medio (MSE) para evaluar la pérdida de test. El modelo de Random Forest demostró una pérdida de test de 0.0197, considerablemente menor en comparación con el LSTM Original (0.0412) y el LSTM Ampliado (0.0555), lo que indica una mayor precisión en la predicción de la FED RATE. La visualización gráfica de los resultados muestra que el Random Forest sigue más fielmente la tendencia de los valores reales, lo que sugiere una mayor aplicabilidad práctica del modelo en la toma de decisiones económicas.

## Lecciones aprendidas

- Uno de los principales desafíos fue la adecuada preparación y escalado de los datos para que sean consumidos eficientemente por los modelos LSTM y Random Forest.
- Se aprendió la importancia de la ingeniería de características y la selección de modelos en la mejora del rendimiento del modelo.
- Para futuros proyectos, se recomienda una exploración de datos más profunda y un ajuste fino más extenso de los hiperparámetros del modelo.

## Impacto del proyecto

- El modelo tiene el potencial de mejorar significativamente la predicción de tasas importantes, lo que podría resultar en una mejor gestión del riesgo y toma de decisiones.
- Existe la oportunidad de integrar este modelo en sistemas de análisis financiero más amplios y en procesos de toma de decisiones en tiempo real.

## Conclusiones

- El proyecto demostró el potencial del uso de técnicas avanzadas de machine learning en el análisis financiero.
- Los resultados obtenidos son prometedores y se recomienda la continuación del desarrollo del modelo, posiblemente integrando conjuntos de datos más amplios y explorando modelos más complejos.

## Agradecimientos

- Agradecimientos a todos los miembros del equipo por su dedicación y esfuerzo en llevar el proyecto desde la concepción hasta el despliegue.
- Un agradecimiento especial a Oscar que proporcionó la guía y los recursos necesarios para realizar este trabajo.
