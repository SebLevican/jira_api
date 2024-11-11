import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

URL_JIRA = None

class JiraHandler:
    def __init__(self, issue_key, jira_user, jira_api_token):
        #self.cloudId = cloudId
        self.issue_key = issue_key
        self.jira_user = jira_user
        self.jira_api_token = jira_api_token
        self.auth = HTTPBasicAuth(jira_user, jira_api_token)

        self.headers = {
          "Accept": "application/json"
        }

    def get_cloud_id(self):
        
        url = f'https://{URL_JIRA}.atlassian.net/_edge/tenant_info'

        headers = {
          "Accept": "application/json"
        }

        response = requests.request(
          "GET",
          url,
          headers=headers
        )

        data = json.loads(response.text)
        # Obtén el valor de "cloudId"
        cloud_id = data.get("cloudId")

        return cloud_id

    
    def get_form_id(self):
        cloudId = self.get_cloud_id()

        ISSUE_KEY = self.issue_key
        
        url = f"https://api.atlassian.com/jira/forms/cloud/{cloudId}/issue/{ISSUE_KEY}/form" #formid

        response = requests.request(
          "GET",
          url,
          headers=self.headers,
          auth=self.auth
        )

        response_data = json.loads(response.text)

        if isinstance(response_data, list):
        # Si es una lista, accedemos al primer elemento
          response_data = response_data[0]

        self.form_id = response_data.get("id", None) if isinstance(response_data, dict) else None

    def extract_responses(self):
        self.get_form_id()
        cloudId = self.get_cloud_id()
        ISSUE_KEY = self.issue_key
        formId = self.form_id
        
        url = f"https://api.atlassian.com/jira/forms/cloud/{cloudId}/issue/{ISSUE_KEY}/form/{formId}"

        headers = {
          "Accept": "application/json",
          "Content-Type": "application/json"
        }

        payload = json.dumps( {
            'answers':{}
        })

        response = requests.request(
            "PUT",
            url,
            data = payload,
            headers=headers,
            auth= self.auth
        )
        

        response_data = json.loads(response.text)

        print(response_data)

        questions = response_data['design']['questions']
        answers = response_data['state']['answers']

        question_answer_dict = {}

        for q_id, question in questions.items():
            question_label = question['label']
            answer_text = answers.get(q_id, {}).get('text','No response')

            question_answer_dict[question_label] = answer_text
        
        return question_answer_dict


    
if __name__ == "__main__":
    load_dotenv()
    # Parámetros necesarios para la conexión
    #cloudId = "your-cloud-id"


    bot = JiraHandler(issue_key,jira_user,jira_api_token)
    bot.extract_responses()
    

