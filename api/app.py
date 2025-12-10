from fastapi import FastAPI
import json
import pandas as pd

app = FastAPI(title="TMDB Analysis API",
              description="API local con los resultados de los análisis 2, 3 y 4",
              version="1.0")

@app.get("/correlacion_budget_rating")
def correlacion_budget_rating():
    with open("api/resultados/correlacion_budget_rating.json",
              "r",
              encoding="utf-8") as f:
        data = json.load(f)
    return data

@app.get("/runtime_por_decada")
def runtime_por_decada():
    df = pd.read_json("api/resultados/runtime_por_decada.json")
    return df.to_dict(orient="records")

@app.get("/directores_top")
def directores_top(limit: int = 20):
    df = pd.read_json("api/resultados/directores_top.json")
    return df.head(limit).to_dict(orient="records")
