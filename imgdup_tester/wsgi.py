from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


app = FastAPI()


@app.get("/")
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


