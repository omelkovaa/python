"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""

import json
with open('character.json') as f:
    data = json.load(f)
planet = data.get("origin")
print(data.get("name",))
print(planet["name"])
print(data.get("episode"))