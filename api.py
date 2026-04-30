from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import get_solar_forecast, daily_summary

app = FastAPI()

class CityInput(BaseModel):
    city: str


@app.get("/")
def home():
    return {"message": "Solar API running"}

@app.post("/predict")
def predict(data: CityInput):
    try:
        loc, df = get_solar_forecast(data.city.strip())
        daily = daily_summary(df)

        return {
            "location": loc,
            "daily": daily.to_dict(orient="records"),
            "df": df.to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))