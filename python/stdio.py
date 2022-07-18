import os

class StdIn:
  file = ""
  def __init__(self, fname = ""):
    self.file = fname
  def read(self):
    if self.file != "":
      return open(self.file).read()
    return input("")

class StdOut:
  file = ""
  def __init__(self, fname = ""):
    self.file = fname
  def write(self, value):
    if self.file != "":
      return open(self.file).write(value)
    return print(value)

class StdErr:
  file = "" # logging
  def __init__(self, file = "err.log"):
    self.file = ""
  def write(self, value):
    if self.file != "":
      return open(self.file).write(value)
    raise RuntimeError(value)
  def read(self):
    if self.file != "":
      return open(self.file).read()
    return ""

stdin = StdIn()
stdout = StdOut()
stderr = StdErr()

def log(x):
  stdout.write(str(x))

def open_stdin():
  return os.fdopen(0, os.O_RDONLY)

def open_stdout():
  return os.fdopen(1, os.O_WRONLY)

def open_stderr():
  return os.fdopen(2, os.O_RDWR)