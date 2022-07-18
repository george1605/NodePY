import os as os
import re

__globals = {"null" : 0}
__macros = {"@get" : "__import__", "@file" : "__file__", "@init" : "__init__"}

def rem_ext(x : str) ->str: # remove .py extension
  return x.split(".py")[0]

class Module:
  props = {}
  fname: str
  def __init__(self, name = "main.py"):
    self.fname = name
    self.props["__main__"] = 0
    self.props = __import__(rem_ext(name), globals(), locals(), [], 0)
  def unimport(self):
    self.props.clear()

def require(fname : str) :
  if not os.path.exists(fname):
    return Module().props
  return Module(fname).props

def include(fname : str):
  s = open(fname,"r").read()
  if ".tpy" in fname:
    for i in __macros.keys():
      s = s.replace(i, __macros[i])
  eval(s , __globals, [])

def addMacro(name : str, code : str):
  __macros[name] = code

def resolveImport(file: str):
  x = re.match("import *", file)
  require(x[0].replace("import ", ""))

def runProject(file = "main.py"):
  if os.path.exists(file):
    include(file)