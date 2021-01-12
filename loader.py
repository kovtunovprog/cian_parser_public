import os
from pathlib import Path
from openpyxl import load_workbook

emails = open('emails.txt')
wb = load_workbook('param_excel.xlsx')
chromedriver_path = 'chromedriver'
