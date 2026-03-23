import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# We know Chapter 2 page URL or can get it
INDEX_URL = "https://www.tamilvu.org/slet/l3100/l3100lf1.jsp"
BASE_URL = "https://www.tamilvu.org"

def get_chapter_2_url():
    res = requests.get(INDEX_URL)
    soup = BeautifulSoup(res.text, "html.parser")
    all_links = soup.find_all("a")
    EXCLUDE = ["பதிகம்", "உரை", "கட்டுரை"]
    seen = set()
    links = []
    
    for a_tag in all_links:
        text = a_tag.get_text(strip=True)
        href = a_tag.get("href")
        if href and "l3100pd5.jsp" in href:
            full_link = urljoin(BASE_URL, href)
            if not any(word in text for word in EXCLUDE):
                if full_link not in seen:
                    seen.add(full_link)
                    links.append(full_link)
    return links[1] if len(links) > 1 else None

ch2_url = get_chapter_2_url()
print(f"Chapter 2 URL: {ch2_url}")

if ch2_url:
    res = requests.get(ch2_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, "html.parser")
    urai_links = []
    link_tds = soup.find_all("td", class_="link")
    for td in link_tds:
        for a in td.find_all("a"):
            if a.get_text(strip=True) == "உரை":
                urai_links.append(urljoin(BASE_URL, a.get("href")))
                
    print(f"Total Urai links in Ch2: {len(urai_links)}")
    if urai_links:
         test_urai = urai_links[0]
         print(f"Inspecting Urai: {test_urai}")
         res_u = requests.get(test_urai)
         soup_u = BeautifulSoup(res_u.text, "html.parser")
         with open("urai_ch2_test.html", "w", encoding="utf-8") as f:
              f.write(soup_u.prettify())
         print("Saved urai_ch2_test.html")
