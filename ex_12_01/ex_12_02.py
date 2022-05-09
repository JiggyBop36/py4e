import socket
url=input("Enter url-")
try:
    url=url.split("//")
    url=url[1]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url, 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
except:
    print("Url is improperly formatted or non-existent: ", url)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    lst=data.decode(),end=''
    print(lst)
    print(len(lst))
    #print(data.decode(),end='')
mysock.close()
