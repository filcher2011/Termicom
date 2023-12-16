#Server for Termicom v.1.0.3-2023.29.11R by filcher2011
import socket

def start():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 2500))
        server.listen(4)
        while True:
            print('Server 127.0.0.1:2500 starting...')
            client, address = server.accept()
            data = client.recv(1024).decode('utf-8')
            print('A new user has appeared on the server!')
            text = load(data)
            client.send(text)
            client.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        server.close()
        print('Shutdown. . .')

def load(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    res = ''
    try:
        with open('html'+path, 'rb') as file:
            res = file.read()
        return HDRS.encode('utf-8') + res
    except FileNotFoundError:
        print(HDRS_404 + ':Not find file html!')

if __name__ == '__main__':
    start()