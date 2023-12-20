from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

Здесь мы импортируем классы и функции из библиотек FastAPI, Jinja2 (шаблонизатор для HTML) и Pydantic (для валидации данных).

Создание экземпляра FastAPI, настройка шаблонизатора:


app = FastAPI()
templates = Jinja2Templates(directory="templates")

Мы создаем экземпляр FastAPI (app) и шаблонизатор Jinja2 (templates), указывая папку, где будут находиться HTML-шаблоны.

Определение схемы валидации с помощью Pydantic:


class ComponentInput(BaseModel):
    power_supply: float
    motherboard: float
    gpu: float
    cpu: float
    ram: float
    storage: float

Создаем класс ComponentInput, который наследуется от BaseModel Pydantic. Этот класс определяет схему входных данных для оценки стоимости компонентов.

Обработка GET-запроса для отображения формы:

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home_js.html", {"request": request})

Обрабатываем GET-запрос, возвращая HTML-страницу home_js.html, где пользователь вводит стоимость комплектующих.

Обработка POST-запроса для расчета стоимости:

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

Обрабатываем POST-запрос, принимая данные в формате JSON и используя их для расчета общей стоимости комплектующих в рублях. Результат возвращается в формате JSON.

HTML-страница с JavaScript для отправки запроса и отображения результата:


<!DOCTYPE html>
<html>
<head>
    <title>Component Cost Calculator</title>
</head>
<body>
    <h1>Component Cost Calculator</h1>
    <label>Power Supply Cost:</label>
    <input type="number" id="power_supply" required><br>

    <!-- Остальные поля ввода для стоимости других комплектующих -->

    <button type="button" onclick="calculate()">Calculate</button>

    <div id="result"></div>

    <script>
        async function calculate() {
            // Получаем значения из полей ввода
            const powerSupply = parseFloat(document.getElementById("power_supply").value);
            // ... (получаем значения для остальных комплектующих)

            // Отправляем POST-запрос на сервер с использованием fetch
            const response = await fetch("/calculate/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    power_supply: powerSupply,
                    // ... (передаем значения для остальных комплектующих)
                })
            });

            // Получаем результат от сервера
            const result = await response.json();

            // Выводим результат под кнопкой "Calculate"
            document.getElementById("result").innerText = `Total Cost (RUB): ₽${result.total_cost_rub.toFixed(2)}`;
        }
    </script>
</body>
</html>

Эта HTML-страница содержит форму для ввода стоимости комплектующих и кнопку "Calculate". С использованием JavaScript (fetch), она отправляет POST-запрос на сервер, получает ответ и отображает итоговую стоимость под кнопкой "Calculate".