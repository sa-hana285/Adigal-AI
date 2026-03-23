import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin

BASE_URL = "https://www.tamilvu.org"
INDEX_URL = "https://www.tamilvu.org/slet/l3100/l3100lf1.jsp"

def get_chapter_links():
    """Fetches and filters chapter links from the index page."""
    print("Fetching index page...")
    res = requests.get(INDEX_URL)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, "html.parser")
    
    links = []
    seen = set()
    EXCLUDE_EXACT = ["பதிகம்", "உரை பெறு கட்டுரை", "நூல் கட்டுரை"]
    
    all_links = soup.find_all("a")
    for a_tag in all_links:
        text = a_tag.get_text(strip=True)
        href = a_tag.get("href")
        
        if href and "l3100pd5.jsp" in href:
            full_link = urljoin(BASE_URL, href)
            
            # Skip unwanted sections exactly
            if text in EXCLUDE_EXACT:
                continue

                
            if full_link not in seen:
                seen.add(full_link)
                links.append({"title_text": text, "url": full_link})
                
    print(f"Found {len(links)} valid chapter links.")
    return links

def scrape_urai(urai_url):
    """Fetches an Urai page and extracts clean explanation text."""
    try:
        res = requests.get(urai_url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 1. Locate the header element with text "உரை"
        # Usually inside <td bgcolor="#FFFFF9">
        header_td = soup.find("td", bgcolor="#FFFFF9")
        if header_td and "உரை" in header_td.get_text():
             # Navigate up to the top row in the container table
             # td -> tr -> table -> td -> tr
             try:
                 top_tr = header_td.find_parent("tr").find_parent("table").find_parent("td").find_parent("tr")
                 content_tr = top_tr.find_next_sibling("tr")
                 
                 if content_tr:
                      # Clean footnotes/references (Decompose <sup> tags)
                      for sup in content_tr.find_all("sup"):
                           sup.decompose()
                      text = content_tr.get_text(separator=" ", strip=True)
                      return text
             except AttributeError:
                 pass # Fallback to backup if structure fails
                 
        # 2. Fallback: Search for first row with valign="top" if structure differs
        tr = soup.find("tr", valign="top")
        if tr:
            for sup in tr.find_all("sup"):
                sup.decompose()
            return tr.get_text(separator=" ", strip=True)
            
        return ""
    except Exception as e:
        print(f"Error scraping Urai {urai_url}: {e}")
        return ""


def scrape_chapter(chapter_entry):
    """Scrapes content from a chapter page and linked Urai pages."""
    url = chapter_entry['url']
    print(f"\nProcessing Chapter: {chapter_entry['title_text']}")
    
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, "html.parser")
        
        # 1. Title Extraction
        title_p = soup.find("p", class_="phead")
        if title_p:
             # Clean extra spaces inside title
             title_text = " ".join(title_p.get_text().split()) 
        else:
             title_text = chapter_entry['title_text']
             
        # 2. Verse Extraction
        verse_chunks = []
        poem_tds = soup.find_all("td", class_="poem")
        for td in poem_tds:
             # Preserve line breaks for verses
             text = td.get_text(separator="\n", strip=True)
             verse_chunks.append(text)
        verse_content = "\n\n".join(verse_chunks)
        
        # 3. Urai Link Extraction
        urai_links = []
        link_tds = soup.find_all("td", class_="link")
        for td in link_tds:
            for a in td.find_all("a"):
                if a.get_text(strip=True) == "உரை":
                     href = a.get("href")
                     if href:
                          urai_links.append(urljoin(BASE_URL, href))
                          
        print(f"  Found {len(urai_links)} Urai links. Fetching...")
        
        # 4. Fetch and combine Urai content
        urai_contents = []
        for i, u_link in enumerate(urai_links):
             urai_text = scrape_urai(u_link)
             if urai_text:
                  urai_contents.append(urai_text)
             # Polite delay between requests
             time.sleep(0.5) 
             
        combined_urai = "\n\n".join(urai_contents)
        
        return {
            "title": title_text,
            "verse": verse_content,
            "urai": combined_urai,
            "source": "TamilVU"
        }
        
    except Exception as e:
        print(f"Error processing chapter {url}: {e}")
        return None

def main():
    chapters = get_chapter_links()
    
    if not chapters:
        print("No chapters found.")
        return
        
    print(f"Total chapters found: {len(chapters)}")
    print("Starting full scraping pipeline (this will take several minutes due to politeness delays)...")
    
    results = []
    for i, entry in enumerate(chapters):
         print(f"[{i+1}/{len(chapters)}] Processing Chapter: {entry['title_text']}")
         data = scrape_chapter(entry)
         if data:

              results.append(data)
         time.sleep(1) # Delay between chapters
         
    # Save output to file
    output_file = "silappatikaram_full.json"
    with open(output_file, "w", encoding="utf-8") as f:
         json.dump(results, f, ensure_ascii=False, indent=2)
         
    print(f"\nSaved full output to {output_file}")

    
if __name__ == "__main__":
    main()
