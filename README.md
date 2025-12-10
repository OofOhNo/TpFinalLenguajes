# Tp Final Lenguajes

descripcion general

este proyecto corresponde al trabajo final de la materia lenguajes 2025 (ucalp). el objetivo es analizar el dataset tmdb 5000 movies utilizando python, realizar analisis descriptivos, generar graficos, producir un informe academico y exponer resultados a traves de una mini api local.

objetivos del proyecto

realizar limpieza y preprocesamiento del dataset

aplicar analisis descriptivo y visualizaciones

responder preguntas de interes basadas en los datos

generar archivos json con resultados resumidos

exponer resultados mediante una mini api local usando fastapi

analisis realizados

este proyecto desarrolla tres analisis:

1. presupuesto vs rating

se calcula la correlacion entre presupuesto y rating utilizando metodos pearson y spearman. se incluye un grafico de dispersion para visualizar la relacion.

2. evolucion del runtime por decadas

se analiza como varia la duracion de las peliculas a lo largo de las decadas. se utiliza la mediana para evitar el efecto de valores extremos.

3. directores con mejor rating promedio

se identifican los directores con mayor rating promedio, considerando un minimo de peliculas para asegurar consistencia. se genera una tabla ordenada y un archivo json con los mejores directores.

