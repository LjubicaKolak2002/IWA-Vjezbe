import socket, requests

def connect_server(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    return s

def get_code(s, ip, page):
    
    CRLF = '\r\n'
    request = "GET /" + page + " HTTP/1.1" + CRLF
    request += "Host: "
    request += ip + CRLF + CRLF
    
    s.send(request.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    return response
    

def get_link(response):
    
    index = 0
    while True:
        begin = response.find('href="', index)
        if begin == -1:
            return links
        
        end = response.find('"', begin + 6)
        link = response[begin + 6: end]
        
        if link[-4:] == "html" and link not in links and requests.get("https://" + ip + "/1280/" + link).status_code == 200:
            links.append(link)
        index = end + 1
        


links = []
ip = "www.optimazadar.hr"
port = 80
page = "1280/djelatnost1280.html"

while True:
    if (len(links) == 0):
        s = connect_server(ip, port)
        response = get_code(s, ip, page)
        print(response)
        get_link(response)
        print(links)
        
        
    elif (len(links) < 10):
        for link in links:
            s = connect_server(ip, port)
            response = get_code(s, ip, '1280/' + link)
            print(response)
            get_link(response)
            print(links)
        break
    
    
    else:
        print("Svi su pronadeni")
        break
        
  