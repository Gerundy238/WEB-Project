import asyncio
import httpx

async def fetch_wikipedia_data(query):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "titles": query,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))
        return page.get("extract", "Статья не найдена.")

async def main():
    query = "Web scraping"  
    try:
        data = await fetch_wikipedia_data(query)
        print("Информация из Википедии:", data)
    except httpx.HTTPError as e:
        print(f"Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    asyncio.run(main())
