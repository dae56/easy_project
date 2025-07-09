import uvicorn
from fastapi import FastAPI, Request

app = FastAPI(
    title="Auth Service",
    description="Auth Service using FastAPI",
    version="0.0.1",
)


@app.get("/")
async def root(requets: Request):
    return requets.headers


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)