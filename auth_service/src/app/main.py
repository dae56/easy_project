import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title="Auth Service",
    version="0.0.1",
)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
