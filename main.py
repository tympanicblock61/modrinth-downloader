import json
import os
import requests


def getLatestVersion():
    versions = requests.get("https://api.modrinth.com/v2/tag/game_version").json()
    for version in versions:
        if version["major"]:
            return version["version"]


def md(id):
    name = requests.get(f"https://api.modrinth.com/v2/project/{id}").json()["title"]
    e = requests.get(f'https://api.modrinth.com/v2/project/{id}/version').json()
    thing = None
    for item in e:
        if versionWanted in item["game_versions"] and loaderWanted in item["loaders"]:
            for file in item["files"]:
                if file["primary"]:
                    thing = file
                    break
            break
    if thing is not None:
        with requests.get(thing["url"], stream=True) as r:
            with open(f"{location}/{thing['filename']}", 'wb') as f:
                f.write(r.content)
                print(thing['filename'])
    else:
        print(f"cannot find {name} for version {versionWanted} or for loader {loaderWanted}")


if __name__ == "__main__":
    mainFile = input("config file: ")
    with open(mainFile, "r") as r:
        config = json.load(r)
        modrinthIds = config["modrinth"]
        loaderWanted = config.get("loader", "fabric")
        versionWanted = config.get("version", getLatestVersion())
        location = config.get("location", os.path.splitext(mainFile)[0])
        delete = config.get("delete", False)

    if not os.path.isdir(location):
        os.mkdir(location)
    elif delete:
        for file in os.listdir(location):
            if file.endswith(".jar"):
                os.remove(f"{location}/{file}")
    for id in modrinthIds:
        if id is not None:
            md(id)
