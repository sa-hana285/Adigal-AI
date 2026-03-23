import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

INDEX_URL = "https://www.tamilvu.org/slet/l3100/l3100lf1.jsp"
BASE_URL = "https://www.tamilvu.org"

def inspect_links():
    res = requests.get(INDEX_URL)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, "html.parser")
    all_links = soup.find_all("a")
    
    with open("output_links.txt", "w", encoding="utf-8") as f:
        f.write("--- ALL LINKS CONTAINING l3100pd5.jsp ---\n")
        seen = set()
        for a_tag in all_links:
            text = a_tag.get_text(strip=True)
            href = a_tag.get("href")
            if href and "l3100pd5.jsp" in href:
                full_link = urljoin(BASE_URL, href)
                f.write(f"Text: '{text}' | href: {href}\n")
                seen.add(full_link)
                
        # Check for the missing ones specifically
        missing = ["கனாத்திறம்", "கட்டுரை காதை", "வரந்தரு காதை"]
        f.write("\n--- CHECKING MISSING CHAPTERS FEASIBILITY ---\n")
        for a_tag in all_links:
            text = a_tag.get_text(strip=True)
            if any(m in text for m in missing):
                f.write(f"FOUND MATCHING TEXT: '{text}' | href: {a_tag.get('href')}\n")

if __name__ == "__main__":
    inspect_links()
