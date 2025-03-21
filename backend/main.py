from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "SUA_API_KEY"
BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

@app.get("/convert")
def convert(from_currency: str, to_currency: str, amount: float):
    response = requests.get(f"{BASE_URL}{from_currency}")
    data = response.json()
    rate = data["rates"].get(to_currency)

    if rate:
        return {"converted_amount": amount * rate, "rate": rate}
    return {"error": "Moeda não encontrada"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    

