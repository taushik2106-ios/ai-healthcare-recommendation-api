from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Healthcare Recommendation API")

class HealthData(BaseModel):
    age: int
    bmi: float
    daily_steps: int
    heart_rate: int
    sleep_hours: float

def assess_health_risk(data: HealthData):
    risk_score = 0

    if data.bmi >= 30:
        risk_score += 2
    elif data.bmi >= 25:
        risk_score += 1

    if data.daily_steps < 5000:
        risk_score += 2
    elif data.daily_steps < 8000:
        risk_score += 1

    if data.heart_rate > 100:
        risk_score += 2

    if data.sleep_hours < 6:
        risk_score += 2
    elif data.sleep_hours < 7:
        risk_score += 1

    if risk_score <= 2:
        return "Low Risk"
    elif risk_score <= 5:
        return "Medium Risk"
    else:
        return "High Risk"

def generate_recommendations(risk_level):
    if risk_level == "Low Risk":
        return [
            "Maintain regular physical activity",
            "Continue balanced diet",
            "Keep good sleep routine"
        ]
    elif risk_level == "Medium Risk":
        return [
            "Increase daily exercise",
            "Reduce sugar and processed foods",
            "Aim for 7-8 hours of sleep"
        ]
    else:
        return [
            "Consult a healthcare professional",
            "Adopt structured fitness routine",
            "Improve sleep hygiene",
            "Monitor vitals regularly"
        ]

@app.post("/health-analysis")
def analyze_health(data: HealthData):
    risk = assess_health_risk(data)
    recommendations = generate_recommendations(risk)

    return {
        "health_risk_level": risk,
        "personalized_recommendations": recommendations
    }

@app.get("/")
def home():
    return {
        "message": "AI Healthcare Recommendation API - Early Prototype"
    }
