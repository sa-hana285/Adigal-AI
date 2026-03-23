import requests
from bs4 import BeautifulSoup

# Correct page (content frame)
url = "https://www.tamilvu.org/slet/l3100/l3100lf1.jsp"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

kadhai_links = []

all_links = soup.find_all("a")
EXCLUDE = ["பதிகம்", "உரை", "கட்டுரை"]

kadhai_links = []
seen = set()

for a_tag in all_links:
    text = a_tag.text.strip()
    href = a_tag.get("href")
    
    if href and "l3100pd5.jsp" in href:
        full_link = "https://www.tamilvu.org" + href
        
        # ❌ skip unwanted
        if any(word in text for word in EXCLUDE):
            continue
        
        if full_link not in seen:
            seen.add(full_link)
            kadhai_links.append((text, full_link))

print(f"Total filtered chapters: {len(kadhai_links)}\n")

for k in kadhai_links:
    print(k[0])

chapter_url = kadhai_links[0][1]
print(f"FIRST_CHAPTER_URL: {chapter_url}")


res = requests.get(chapter_url)
chapter_soup = BeautifulSoup(res.text, "html.parser")

print(chapter_soup.prettify()[:2000])
print(chapter_soup.get_text()[:2000])