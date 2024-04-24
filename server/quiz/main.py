from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title='QUIZ',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='0.0.0.0', port=8000,
    )
