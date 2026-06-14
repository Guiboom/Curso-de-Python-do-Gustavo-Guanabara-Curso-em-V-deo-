import requests

try:
    print("O site Pudim está acessivel no momento!" if requests.get("https://pudim.com.br/", timeout=5).ok else "Offline")
except:
    print("O site Pudim não está acessivel no momento!")