# Meti-KK2

Detta projet har byggts upp med hjälp utav FastAPI och Pandas. Som gör att användaren kan ladda upp sin egen CSV-fil, få statistik om dataset samt ställa frågor till ai-modellen som är implementerad i projektet.

projektet innehåller en väldigt simpel ai-modell bestående utav 3 olika pipelines:
- PromptBuilder
- LLMRunner
- ResponseParser

- ## Hur man sätter upp programmet:
- -Uv sync

- ## Hur Projektet startas
- uv run uvicorn main:app --reload

- API har Swagger implementerat också: http://127.0.0.1:8000/docs

- ## Hur man kör Tester i programmet:
- PYTHONPATH= uv run pytest

## Olika Endpoints som är implementerade i programmet:
GET /health (en kontroll på att API'et är i stabil funktion).

POST/data/upload (Ska ha möjlighet att ladda upp en CSV-fil).

GET /data/stats (som visar statistik baserad på den CSV-fil som man har laddats upp.

POST /ai/ask (en AI-modell som går att ställa frågor om.
Exempel:
{
   "question"; "What is the average release year?"
}
