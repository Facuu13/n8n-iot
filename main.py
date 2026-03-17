from fastapi import FastAPI

app = FastAPI()

@app.post("/evaluate")
def evaluate(data: dict):
    temp = data.get("temp", 0)

    if temp > 40:
        severity = "critical"
    elif temp > 35:
        severity = "warning"
    else:
        severity = "normal"

    return {
        "temperature": temp,
        "severity": severity
    }