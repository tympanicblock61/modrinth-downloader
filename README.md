# modrinth-downloader

credits
```
crosby: Crosby#9153 - helped with alot of stuff

```

config file syntax; it can contain either mod id or name and it works to get the mod from both <br>
location is the location the mods will be downloaded to or if its set to none then the downloader will use the name of the config file <br>
if delete is set to true and the location is set then if that location has any file it will delete them
```
{
  "loader": "fabric",
  "version": "1.19.2,
  "location": "test",
  "delete": true,
  "modrinth": [
     "LQ3K71Q1",
     "dynamic-fps"
  ]
}
```
tutorial on ids and name<br />
[![Watch the video]()](https://files.catbox.moe/zmv9nz.mp4)
