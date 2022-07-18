from require import require

net = require("net.py")
window = require("window.py")
process = require("process.py")

def server():
    server_sock = net.sock()
    net.waitClient(server_sock)

    conn = net.getConn(server_sock)
    net.getRequest(conn)
    response = "<h1>Hello!</h1>"
    net.sendHeader(conn)
    net.sendContent(conn, response)
    conn.close()

    server_sock.close()

serv = process.newProc(server)
serv.join()
win = window.Window()
win.openNative("0.0.0.0:8080")
