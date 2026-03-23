import json

def check_varantharu():
    try:
        with open('silappatikaram_full.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            target = [item for item in data if 'வரந்தரு' in item['title']]
            if target:
                item = target[0]
                print(f"FOUND: {item['title']}")
                print(f"Verse Length: {len(item.get('verse', ''))}")
                print(f"Urai Length: {len(item.get('urai', ''))}")
                if item.get('urai'):
                    print("\nUrai Preview:")
                    print(item['urai'][:500] + "...")
            else:
                print("வரந்தரு காதை not found in JSON.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_varantharu()
