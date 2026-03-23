import json

def check_titles():
    try:
        with open('silappatikaram_full.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            with open('json_titles.txt', 'w', encoding='utf-8') as out:
                out.write(f"Total chapters in JSON: {len(data)}\n")
                for i, item in enumerate(data):
                    out.write(f"{i+1}: {item['title']}\n")
            print("Saved json_titles.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_titles()
