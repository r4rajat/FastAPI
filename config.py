from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount('/static', StaticFiles(directory='./static'), name='static')
template = Jinja2Templates(directory='./templates')

from views import api
