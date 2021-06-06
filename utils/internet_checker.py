import requests

def check():
   try:
      requests.get("https://github.com")
   except Exception:
      print ("Соединения к интернету отсутствует! Скрипт не может продолжать работу")
      exit()
