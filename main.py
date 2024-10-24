from fastapi import FastAPI, Request
from requests.auth import HTTPBasicAuth
from formid import JiraHandler  # Importa la clase desde tu módulo
from dotenv import load_dotenv
import os
from excel_handler import update_excel

load_dotenv()

issue_key = os.getenv('ISSUE_KEY')
jira_user = os.getenv('JIRA_USER')
jira_api_token = os.getenv('JIRA_API_TOKEN')


app = FastAPI()


# Ruta para recibir el webhook de Jira
@app.post('/webhook')
async def handle_webhook(request: Request):
    try:
        payload = await request.json()
    except Exception as e:
        return {'error':'invalid or missing json payload'}

    bot = JiraHandler(issue_key, jira_user, jira_api_token)
    ask_question = bot.extract_responses()

    message = update_excel(ask_question)

    return {"message": message}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
