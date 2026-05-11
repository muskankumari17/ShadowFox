import re

import requests
from bs4 import BeautifulSoup


pages = [
    "https://en.wikipedia.org/wiki/Timeline_of_computing_1980%E2%80%931989",
    "https://en.wikipedia.org/wiki/Timeline_of_computing_1990%E2%80%931999",
    "https://en.wikipedia.org/wiki/Timeline_of_computing_2000%E2%80%932009",
    "https://en.wikipedia.org/wiki/Timeline_of_computing_2010%E2%80%932019",
    "https://en.wikipedia.org/wiki/Timeline_of_computing_2020%E2%80%93present",
]

print("Main Computer Inventions from 1980s to Present:")

printed = 0
keywords = ["released", "introduced", "launched", "created", "developed", "announced", "first"]
seen = set()


def clean_event(text):
    text = re.sub(r"\[\s*\d+\s*\]", "", text)
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"\s+", " ", text).strip()
    return text[:150] + "..." if len(text) > 150 else text

for url in pages:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", class_="mw-parser-output") or soup.find("body")

    if not content:
        continue

    year = ""
    page_count = 0

    for tag in content.find_all(["h2", "table", "ul"]):
        if tag.name == "h2":
            match = re.search(r"\b(19|20)\d{2}\b", tag.get_text())
            if match:
                year = match.group()

        elif tag.name == "table" and year:
            rows = tag.find_all("tr")[1:]

            for row in rows:
                cells = row.find_all("td")
                if not cells:
                    continue

                event = clean_event(cells[-1].get_text(" ", strip=True))

                if event not in seen and any(word in event.lower() for word in keywords):
                    seen.add(event)
                    print(f"{year} - {event}")
                    printed += 1
                    page_count += 1
                    break

        elif tag.name == "ul" and year:
            for item in tag.find_all("li", recursive=False):
                event = clean_event(item.get_text(" ", strip=True))

                if event not in seen and any(word in event.lower() for word in keywords):
                    seen.add(event)
                    print(f"{year} - {event}")
                    printed += 1
                    page_count += 1
                    break

        if page_count == 3:
            break

    if printed == 15:
        break
