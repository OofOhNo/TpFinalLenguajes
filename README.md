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

se calcula la correlacion entre presupuesto y rating usando pearson y spearman. se arma tambien un grafico de dispersion para ver si efectivamente hay relacion o si es puro humo.

2. duracion de peliculas por decada

se analiza como fueron cambiando las duraciones a lo largo del tiempo. se usan medianas para que no molesten los valores raros.

3. directores con mejor promedio de rating

se arma un ranking de directores con mejor rating promedio, filtrando por una cantidad minima de peliculas asi no aparece alguno con una sola peli de suerte.



