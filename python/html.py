import re
import os
import net as net
import requests

def get_tag(html):
    return re.match("<(a-z)></(a-z)>", html)[0]


class Element:
    tag = ""
    style = {"background": "white"}
    outerHTML = "<template />"

    def __init__(self, html=""):
        self.outerHTML = html
        self.tag = get_tag(html)

    def addStyle(self, name: str, value):
        self.style[name] = value

class File:
    filename = ""

    def __init__(self, fname="index.html", content=""):
        self.filename = fname
        if content != "":
            open(fname, "x").write(fname)

    def open_in(self, browser="firefox"):
        if os.name == "posix":
            os.system(browser + " " + self.filename)
        os.system("start " + browser + " " + self.filename)

class Document(Element):
    def __init__(self, content):
        self.outerHTML = str(content)
    def findTag(self, tag):
        return re.match(f"<*{tag}^>", self.outerHTML)

def sendHtml(sock, x: Element):
    net.send(sock, x.outerHTML)

def sendHeader(c):
    c.send('HTTP/1.0 200 OK\n')
    c.send('Content-Type: text/html\n')
    c.send('\n')

def getPage(website) -> File:
    req = requests.get(website)
    return Document(req.content)

hello : str = Element("<h1>Welcome!</h1>")