import os

def toPosix(path: str) -> str:
  if 'C:/' in path:
    path = path.replace('C:/','/home/')
  return path.replace('\\', '/')

def isValidFile(fname: str) -> bool:
  if ">" in fname or "<" in fname:
    return False
  return True

def absolutePath(path: str):
  return os.getcwd() + "/" + path

def exists(path: str):
  return os.path.exists(path)

def readFile(file: str, function):
  data = open(file).read()
  function(data)

def writeFile(file: str, content: str):
  open(file).write(content)

def readFileBuf(file: str, size: int):
  data = open(file).read(size)
  return data

def copyFile(file1: str, file2: str):
  buffer = open(file1, "r").read()
  open(file2, "x").write(buffer)

def mkdir(dir: str):
  os.mkdir(str)
