import json
import os
import requests
from bs4 import BeautifulSoup

USERNAME = "1GabsFps"
URL = f"https://github.com/users/{USERNAME}/contributions"

def fetch():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Erro ao buscar contribuições: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    days_data = []
    
    for cell in soup.find_all("td", class_="ContributionCalendar-day"):
        date = cell.get("data-date")
        level = cell.get("data-level", "0")
        if date:
            days_data.append({"date": date, "level": int(level)})
            
    days_data.sort(key=lambda x: x["date"])
    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(days_data, f, indent=2)
    print("Dados de contribuição salvos com sucesso!")

if __name__ == "__main__":
    fetch()
