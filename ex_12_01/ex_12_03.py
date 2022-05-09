import urllib.request, urllib.parse, urllib.error
url=input("Enter url-")
try:
    url=url.split("//")
    url=url[1]
    fhand=urllib.request.urlopen(url)
    character_count=0
    for line in fhand:
        character=line.decode()
        for cha in character:
            character_count+=1
            if character_count==3000:
                print(line.decode().strip())
    print(character_count)
except:
    print("Url is improperly formatted or non-existent: ", url)
