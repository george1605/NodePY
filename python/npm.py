# recreating the npm 
import require as req
import net as net
import os
import sys
import requests

npm_dir = os.getcwd() + "/npm"
npm_url = "https://www.github.com" # where the packages are hosted

def get_args():
  if sys.argv[1] == "--help":
    print("Usage: npm install <package-name>")
    return ""
  if sys.argv[1] != "install":
    raise RuntimeError("Bad Syntax: Type npm --help for usage")
    return ""
  else:
    return sys.argv[2]

def isInstalled(module : str):
  if not ".py" in module:
    module += ".py"
  return os.path.exists(npm_dir + "/" + module)

def setDir(dirname : str):
  if not os.path.exists(dirname):
    os.mkdir(dirname)
  npm_dir = dirname

def downloadPack(pack_name : str):
  r = requests.get(npm_url + "/" + pack_name)
  open(npm_dir + "/file.py", "w").write(str(r.content))

def translatePack(js_pack : str): # translates from JS packages to Python packages
  if js_pack == "express":
    return "flask"
  if js_pack == "react":
    return "tkinter"
  return ""

def npm_require(pack):
  if not isInstalled(pack):
    downloadPack(pack)
  return req.require(pack)

#version control thing
def latestVersion(pack: str):
  return "1.0.1"

def isLatest(pack: str):
  x = pack.split("-")
  vers = x[len(x) - 1]
  return vers == latestVersion(pack)

def runNPM():
  setDir("./npm")
  x = get_args()
  if x != "":
    downloadPack(x)
  
runNPM()