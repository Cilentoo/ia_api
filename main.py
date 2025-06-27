from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "API de IA funcionando!"}

# rodar esta API com: uvicorn main:app --reload