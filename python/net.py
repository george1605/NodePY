import socket
import requests
buf_siz = 8192
localhost = "127.0.0.1"
localport = 65432 # some arbritary port - you can change it - 
serverhost = '0.0.0.0'
serverport = 8000

def to_bytes(n: str) -> bytes:
  return bytes(n, "utf-8")

http_code = {"OK" : 200, "NOT_FOUND": 404, "SERVER_ERR": 400, "DENIED": 403}

def create():
  return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(sock, host = localhost, port = localport):
  sock.connect((host, port))
  return sock

def test_sock(sock):
  sock.sendall(to_bytes("Hello!"))
  return sock.recv(buf_siz)

def setopt(server_socket):
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  return server_socket

def sock(sock):
  sock = create()
  return setopt(sock)

def close(sock):
  sock.close()

def end(sock):
  sock.shutdown(socket.SHUT_RDWR)

#waits for a client to connect
def waitClient(sock): 
  sock.bind((serverhost, serverport))
  sock.listen(1)

def acceptConn(sock, func):
  conn, addr = sock.accept()
  func(conn, addr)

def getConn(sock):
  conn, addr = sock.accept()
  return conn

def make_header(req = "GET", file = "/index.html"):
  x = req + " " + file + " HTTP/1.0\n"
  x = x + "Content-type: text/html"
  return x

def makeRequest(type: str, site : str):
  if type == "GET":
    return requests.get(site)
  elif type == "POST":
    return requests.post(site)
  else:
    return {"contents":""}

def recv(sock):
  return sock.recv(buf_siz)

def send(sock, msg = b"Hello!"):
  sock.send(msg)

def sendHeader(conn):
  header = 'HTTP/1.0 200 OK\n\n'
  conn.send(header.encode())

def sendContent(conn, msg):
  conn.send(msg.encode())

# gets a client connection
def getClient(sock):
  waitClient(sock)
  return getConn(sock)

def getRequest(client_connection):
   request = client_connection.recv(1024).decode()
   print(request)