import os
import multiprocessing as proc

def __defworker():
  print("Working...")

def newProc(func = __defworker):
  p = proc.Process(target = func)
  p.start()
  return p

def closeProc(p : proc.Process):
  p.close()

def pid():
  return os.getpid()

def getProcInfo(p : proc.Process):
  return {"pid" : p.pid, "ret" : p.exitcode, "parent" : p.daemon}
  