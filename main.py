import json
import os
import requests


def stripstr(strw):
    oldstrw = strw
    for _ in range(len(oldstrw)):
        if oldstrw[_] not in string.ascii_letters + " ":
            strw = strw.replace(oldstrw[_], "")
    return strw


def md(id):
    e = requests.get(f'https://api.modrinth.com/v2/project/{id}/version?featured=true').json()
    thing = None
    name = None
    for item in e:
        if name is None:
            name = stripstr(item["name"])
            print(name)
        if versionWanted in item["game_versions"] and loaderWanted in item["loaders"]:
            for file in item["files"]:
                if file["primary"]:
                    thing = file
                    break
            break
    if thing is not None:
        with requests.get(thing["url"], stream=True) as r:
            with open(f"mods/{thing['filename']}", 'wb') as f:
                f.write(r.content)
                print(thing['filename'])
    else:
        print(f"cannot find {name} for version {versionWanted}")
        
if __name__ == "__main__":
    file = input("config file: ")
    if not os.path.exists("mods"):
        os.makedirs("mods")
    with open(file, "r") as r:
        config = json.load(r)
        modrinthIds = config["modrinth"]
        loaderWanted = config["loader"] or "fabric"
        versionWanted = config["version"] or "1.19.2"  # or use a api to get latest version of the game

    for id in modrinthIds:
        if id is not None:
            md(id)
