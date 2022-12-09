import os
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, get_settings


app = FastAPI()


register_tortoise(
    app,
    generate_schemas=False,
    add_exception_handlers=True,
    db_url=os.environ.get('DATABASE_URL'),
    modules={"models": ["app.models.tortoise"]}
)


@app.get('/ping')
def pong(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong',
        'testing': settings.testing,
        'environment': settings.environment

    }
