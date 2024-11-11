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
jira_base_url = os.getenv('JIRA_URL')


app = FastAPI()

class IssuePayload(BaseModel):
    issue: dict

def attach_file_to_jira(issue_key, filepath):
    with open(file_path,"rb") as f:
        headers = {
            "X-atlassian-token":"no-check"
        }
        response = headers,
        auth=(jira_user,jira_api_token),
        file={"file":f}
    )
    if response.status_code ==200:
        return "archivo adjuntado con exito"
    else:
        return f"error al subir {response.context}"

# Ruta para recibir el webhook de Jira
@app.post('/webhook')
async def handle_webhook(payload: IssuePayload):
    try:
        issue_key = payload.issue.get('key')
        bot = JiraHandler(issue_key, jira_user, jira_api_token)
        ask_question = bot.extract_responses()
        file_path = update_excel(ask_question)

        attach_response = attach_file_to_jira(issue_key,file_path)
    except Exception as e:
        return {'error':'invalid or missing json payload','details': str(e)}

    return {"message": attach_response}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
