import require as req

fs = req.require("fs.py")
net = req.require("net.py")

def test_fs():
  return (fs.isValidFile("<<well") == False and fs.exists("tests.py") == True)

class UnitTest:
  values = []
  expected = []
  funcs = []
  def __init__(self, f = [test_fs], exp = [True]):
    self.funcs = f
    self.expected = exp
  