from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
async def healcheck():
    return {"status": "ok"}