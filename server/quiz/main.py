from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from fastapi import FastAPI
from src.api import surveys
from src.api import users
from src.api import results
from src.api import auth


app = FastAPI(
    title='QUIZ',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://client:5173",
    "http://client:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(surveys.router, prefix="/surveys", tags=["surveys"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(results.router, prefix="/results", tags=["results"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='0.0.0.0', port=8000,
    )
