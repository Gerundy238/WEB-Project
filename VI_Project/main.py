from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class ComponentInput(BaseModel):
    power_supply: float
    motherboard: float
    gpu: float
    cpu: float
    ram: float
    storage: float


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home_js.html", {"request": request})


@app.post("/calculate/", response_class=JSONResponse)
async def calculate(components: ComponentInput):
    total_cost_rub = (
        components.power_supply +
        components.motherboard +
        components.gpu +
        components.cpu +
        components.ram +
        components.storage
    )
    return {"total_cost_rub": total_cost_rub}
