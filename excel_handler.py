from requests.auth import HTTPBasicAuth
from formid import JiraHandler
from dotenv import load_dotenv
import os
import openpyxl
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

load_dotenv()


aws_access_key_id = os.getenv('AWS_ACCESS_KEY')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

def update_excel(ask_question, excel_file='oc.xlsx', save_as='prueba.xlsx'):
    """
    Actualiza las celdas del archivo Excel con las respuestas obtenidas.

    Args:
        ask_question (dict): Diccionario con las preguntas y respuestas.
        excel_file (str): El archivo Excel a modificar.
        save_as (str): El nombre con el que se guardará el archivo modificado.
    """
    # Cargar el archivo Excel
    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active

    # Rellenar las celdas específicas con las respuestas del formulario de Jira
    sheet['F12'] = ask_question.get('Nombre solicitud', 'No disponible')
    sheet['F16'] = ask_question.get('Destino de envio', 'No disponible')
    sheet['F18'] = ask_question.get('Solicitante', 'No disponible')
    sheet['F20'] = ask_question.get('Telefono contacto', 'No disponible')
    sheet['F22'] = ask_question.get('Correo contacto', 'No disponible')

    # Guardar el archivo Excel modificado
    wb.save(save_as)

    filename = 'prueba.xlsx'
    file_path = os.path;join(os.getcws(),filename)
    bucket_name = 'solicitudoc'


    try:
        s3_client.upload_file(file_path,bucket_name,filename)
        file_url = f'https://{bucket_name}.s3.amazonaws.com/{filename}'
        return f'Archivo subido a s3 en {file_url}'
    except NoCredentialsError:
        return "Error: Credenciales no encontradas"
