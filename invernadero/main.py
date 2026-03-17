from fastapi import FastAPI

app = FastAPI()

@app.post("/evaluate-greenhouse")
def evaluate(data: dict):
    device = data.get("device")
    temp = data.get("temperature", 0)
    soil = data.get("soil_moisture", 0)

    # Reglas
    ventilation = temp > 30
    irrigation = soil < 30

    # Mensaje
    messages = []

    if ventilation:
        messages.append("High temperature")
    if irrigation:
        messages.append("Dry soil")

    message = " and ".join(messages) if messages else "Conditions normal"

    return {
        "device": device,
        "ventilation": ventilation,
        "irrigation": irrigation,
        "message": message
    }