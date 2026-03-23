import json
import time
from scrape_structured import get_chapter_links, scrape_chapter

def append_missing():
    try:
        # 1. Load existing data
        print("Loading existing dataset...")
        with open('silappatikaram_full.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
            
        existing_titles = {item['title'] for item in existing_data}
        print(f"Loaded {len(existing_data)} existing chapters.")
        
        # 2. Get fixed link list
        print("Fetching fixed chapter list...")
        all_chapters = get_chapter_links()
        
        missing_chapters = []
        for ch in all_chapters:
            title = ch['title_text']
            is_missing = True
            for existing in existing_titles:
                if title in existing:
                    is_missing = False
                    break
            if is_missing:
                missing_chapters.append(ch)
                
        print(f"Found {len(missing_chapters)} missing chapters to process.")
        
        if not missing_chapters:
            print("No missing chapters to append.")
            return
            
        # 3. Scrape missing
        new_entries = []
        for i, ch in enumerate(missing_chapters):
            print(f"[{i+1}/{len(missing_chapters)}] Scraping missing: {ch['title_text']}")
            data = scrape_chapter(ch)
            if data:
                new_entries.append(data)
            time.sleep(1)
            
        # 4. Append and Save
        existing_data.extend(new_entries)
        
        # Optional: Sort if required, but usually user appends at end
        # Let's keep existing order and append at end.
        
        with open('silappatikaram_full.json', 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully appended {len(new_entries)} chapters to silappatikaram_full.json")
        
    except Exception as e:
         print(f"Error appending missing chapters: {e}")

if __name__ == "__main__":
    append_missing()
