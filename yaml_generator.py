import json

with open('emojis.json', 'r') as file:
    data = json.loads(file.read())

table_of_clean_emojis = [
    # ('0x1f36c', ':code:')
]

with open('emoji_top.json', 'r') as file:
    data_top = json.loads(file.read())

data_items = data.items()

for key, value in data_items:
    hex_unicode = hex(ord(value[:1]))[2:]

    table_of_clean_emojis.append((f'{hex_unicode}.png', key ))

from pathlib import Path

print(len(table_of_clean_emojis))

import shutil

Path('72x72_to_srv').mkdir(parents=True, exist_ok=True)

for entry in table_of_clean_emojis:
    (pic_location, emoji_code) = entry
    pic_full_location = (Path('72x72') / pic_location)
    pic_srv_full_path = Path('72x72_to_srv') / pic_location
    
    if pic_full_location.exists():
        shutil.copy(pic_full_location, pic_srv_full_path)
    else:
        print(f"cant find image for {entry}")

        table_of_clean_emojis.remove(entry)

print(len(table_of_clean_emojis))

header = """
"""

body = ""

for (pic_location, emoji_code) in table_of_clean_emojis:
    body+=f"""
  {emoji_code}:
    permission: gg
    show_in_gui: true
    path: "72x72/{pic_location[:-4]}"
    scale_ratio: 10
    y_position: 8
"""

full_yaml = header+body

with open('output.yaml', 'w') as file:
    file.write(full_yaml)
