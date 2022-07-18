import webbrowser as webbrowser
import tkinterweb
import requests
import tkinter as tk

class Window:
    history = []
    gui_handle = None
    def __init__(self):
       self.history = ["about:blank"]
    def toURL(self, string):
        return "https://" + string
    def open(self, URL, args=None):
        if args == "newtab":
            webbrowser.open_new_tab(URL)
        else:
            webbrowser.open_new(URL)
        self.history.append(URL)
    def newNative(self):
        self.gui_handle = tk.Tk("Browser")
    def openNative(self, string):
        root = tk.Tk()
        frame = tkinterweb.HtmlFrame(root)
        frame.load_website(string)
        frame.pack(fill="both", expand=True)
        root.mainloop()
        self.gui_handle = root
        self.history.append(string)
    def go(self, index):
        self.open(self.history[index])
    def closeNative(self) -> bool:
        if self.gui_handle == None:
            return False
        self.gui_handle.destroy()
        return True
    def loadImg(self, url, w=100, h=100):
        r = requests.get(url)
        canvas = tk.Canvas(self.gui_handle, width=w, height=h)
        canvas.pack()
        image = tk.PhotoImage(data=r.content, format="ico")
        canvas.create_image(20, 20, anchor=tk.NW, image=image)
