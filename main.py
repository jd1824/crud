from fastapi import FastAPI
import uvicorn
from routes.user import user

app = FastAPI()

app.include_router(user)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)