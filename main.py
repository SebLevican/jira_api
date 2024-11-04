from fastapi import FastAPI, Request
from requests.auth import HTTPBasicAuth
from formid import JiraHandler  # Importa la clase desde tu módulo
from dotenv import load_dotenv
import os
from excel_handler import update_excel
from pydantic import BaseModel

load_dotenv()

issue_key = os.getenv('ISSUE_KEY')
jira_user = os.getenv('JIRA_USER')
jira_api_token = os.getenv('JIRA_API_TOKEN')


app = FastAPI()

class IssuePayload(BaseModel):
    issue: dict
    issue_key: str

# Ruta para recibir el webhook de Jira
@app.post('/webhook')
async def handle_webhook(payload: IssuePayload):
    issue_key = payload.issue.get('key')

    try:
        bot = JiraHandler(issue_key, jira_user, jira_api_token)
        ask_question = bot.extract_responses()

        message = update_excel(ask_question)
    except Exception as e:
        return {'error':'invalid or missing json payload','details': str(e)}

    return {"message": message}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
