import sys as sys
import os as os

html_basic = """
<!DOCTYPE html>
<html>
  <body>
    <h1>HELLO WORLD!</h1>
  </body>
</html>
"""

js_basic = """

function addElem(x)
{
  if(x == null || x == undefined) return x;
  document.body.appendChild(x);
  return x;
}
"""

css_basic = """
h1 {
  color : green;
}
"""

def makeProject(name: str):
  os.mkdir(name)
  os.chdir(name)
  open("index.html","x").write(html_basic)
  open("style.css","x").write(css_basic)
  open("main.js","x").write(js_basic)

if len(sys.argv) <= 2:
  raise RuntimeError("Expected project name")

if sys.argv[1] == "create":
  makeProject(sys.argv[2])
