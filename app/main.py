from fastapi import FastAPI

app = FastAPI(
    title="Raízes do Nordeste API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "API funcionando"}