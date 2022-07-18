import sys
import require as req

fs = req.require("../fs.py")

if len(sys.argv) <= 1:
    raise RuntimeError("Expected argument [1] = file")

content = open(sys.argv[1], "r").read()
content = content.replace("int", "")

eval(content)