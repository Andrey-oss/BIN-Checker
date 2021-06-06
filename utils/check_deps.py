import os

def check_deps():
   try:
      import requests
   except Exception:
      raise ImportError('Модуль requests не установлен!')
