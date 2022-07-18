import require as req

net = req.require("../net")
html = req.require("../html")
window = req.require("./window")

def createSimpleServer(location="8000"):
    sock = net.setopt(net.create())
    conn = net.getClient(sock)
    net.serverport = int(location)
    while True:
        data = net.recv(conn)
        if data == "exit":
            break
        html.sendHeader(conn)
        html.sendHtml(conn, html.hello)

def showGUI(location) -> window.Window:
    win = window.Window()
    win.openNative(location)
    return win
