import requests
from bs4 import BeautifulSoup

chapter_url = "https://www.tamilvu.org/slet/l3100/l3100pd5.jsp?bookid=50&pno=3"
urai_url = "https://www.tamilvu.org/slet/l3100/l3100uri.jsp?slno=300&subid=30000"

def save_html(url, filename):
    try:
        res = requests.get(url)
        res.encoding = 'utf-8' # Ensure UTF-8
        soup = BeautifulSoup(res.text, "html.parser")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        print(f"Saved {url} to {filename}")
    except Exception as e:
        print(f"Error saving {url}: {e}")

save_html(chapter_url, "chapter_page.html")
save_html(urai_url, "urai_page.html")
