from Tkinter import *
from ttk import Frame, Button, Style
import Tkinter as tk

class MapGen(Frame):
    frame = []
    ButtonArray = []

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.frame = tk.Frame(self, relief=RAISED, borderwidth=1)

        self.parent = parent

        self.initUI()

    def ButtonAction(self, event):
        print "This is an event binding test"
        print event.widget['text']
        photo2 = tk.PhotoImage(file="sprites/wallSprite.gif")

        count = 1
        row = 0
        col = 0
        for n in range(0,1560):
            if int(event.widget['text']) == n:
                self.ButtonArray[n].configure(image = photo2)
                self.ButtonArray[n].image = photo2
                #self.ButtonArray[n].grid(row=row , column=col)

            col += 1

            if count==40:
                row += 1
                col = 0
                count = 0

            count += 1


    def initUI(self):
        # sets name and style of window
        self.parent.title("MapGen")
        self.style = Style()
        self.style.theme_use("default")

        photo1 = tk.PhotoImage(file="sprites/floorSprite.gif")

        self.frame.pack(fill=BOTH, expand=1)

        count = 1
        row = 0
        col = 0
        for n in range(0,1560):
            self.ButtonArray.append(tk.Button(self.frame, text = str(n), image = photo1, height = 18,
                width = 18, borderwidth= -1, padx = 0, pady = 0, relief=FLAT))
            self.ButtonArray[n].image = photo1
            self.ButtonArray[n].bind('<Button-1>', self.ButtonAction)
            self.ButtonArray[n].grid(row=row , column=col)

            col += 1

            if count==40:
                row += 1
                col = 0
                count = 0

            count += 1

        self.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT, padx=5, pady=5)


def main():

    root = Tk()
    root.geometry("800x815")
    app = MapGen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
