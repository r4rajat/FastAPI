from config import app, template
import constant
from fastapi import Request


@app.get('/')
async def index(request: Request):
    return template.TemplateResponse('index.html', {constant.REQUEST: request})


@app.get('/hello-world')
async def helloWorld():
    """ This is Another Route."""
    return {constant.MESSAGE: "Hello World!!"}
