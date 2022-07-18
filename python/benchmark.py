import os
import sys
import psutil

def platform():
  return str(os.uname().sysname)

def version():
  return str(os.uname().version)

def cpu_usage(secs=4):
  return psutil.cpu_percent(secs)

def cpu_avg():
  n = psutil.getloadavg()
  cpu_usage = (n/os.cpu_count()) * 100
  return cpu_usage