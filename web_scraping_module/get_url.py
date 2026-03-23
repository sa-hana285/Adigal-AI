import requests
from bs4 import BeautifulSoup

url = "https://www.tamilvu.org/slet/l3100/l3100lf1.jsp"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

all_links = soup.find_all("a")
EXCLUDE = ["பதிகம்", "உரை", "கட்டுரை"]

for a_tag in all_links:
    text = a_tag.text.strip()
    href = a_tag.get("href")
    
    if href and "l3100pd5.jsp" in href:
        full_link = "https://www.tamilvu.org" + href
        if not any(word in text for word in EXCLUDE):
            print(f"URL: {full_link}")
            break
