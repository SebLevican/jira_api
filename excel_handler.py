from requests.auth import HTTPBasicAuth
from formid import JiraHandler
from dotenv import load_dotenv
import os
import openpyxl


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
    return f"Excel saved as {save_as}"