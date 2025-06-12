from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/map", response_class=HTMLResponse)
async def map_view(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})

@app.get("/faction", response_class=HTMLResponse)
async def faction_view(request: Request):
    return templates.TemplateResponse("faction.html", {"request": request})

@app.get("/bestiary", response_class=HTMLResponse)
async def bestiary_view(request: Request):
    return templates.TemplateResponse("bestiary.html", {"request": request})

@app.get("/alchemy", response_class=HTMLResponse)
async def alchemy_view(request: Request):
    return templates.TemplateResponse("alchemy.html", {"request": request})

@app.get("/inventory", response_class=HTMLResponse)
async def inventory_view(request: Request):
    return templates.TemplateResponse("inventory.html", {"request": request})
