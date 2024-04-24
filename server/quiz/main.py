from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from src.api import surveys


app = FastAPI(
    title='QUIZ',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)


app.include_router(surveys.router, prefix="/surveys", tags=["surveys"])


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='0.0.0.0', port=8000,
    )
