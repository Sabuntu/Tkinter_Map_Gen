from Tkinter import *
from ttk import Frame, Button, Style
import Tkinter as tk
import tkFileDialog

class MapGen(Frame):
    frame = []
    button_array = []
    type_list = []

    photo1 = ""
    photo2 = ""

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.frame = tk.Frame(self, relief=RAISED, borderwidth=1)

        self.parent = parent

        self.initUI()

    def buttonAction(self, event):
        print "This is an event binding test"
        print event.widget['text']

        for n in range(0,1560):
            if int(event.widget['text']) == n:
                self.buttonType(n)


    def buttonType(self, n):
        if self.type_list[n] == 1:
            self.type_list[n] = 0
            self.button_array[n].configure(image = self.photo1)
            self.button_array[n].image = self.photo1
            tr = ""
            for n in range(0,1560):
                tr += str(self.type_list[n])

            print tr
        if self.type_list[n] == 0:
            self.type_list[n] = 1
            self.button_array[n].configure(image = self.photo2)
            self.button_array[n].image = self.photo2
            tr = ""
            for n in range(0,1560):
                tr += str(self.type_list[n])

            print tr

    def loadFile(self):
        file_type = [('Python files', '*.switch')]
        load_dialog = tkFileDialog.Open(self, filetypes = file_type)
        f = load_dialog.show()

        if f != '':
            loadable = self.readFile(f)
            print loadable
            # Loop splits file characters into the list

            for n in range(0,1560):
                self.type_list[n] = int(loadable[n])

            for n in range(0,1560):
                print str(self.type_list[n])

                if self.type_list[n] == 0:
                    self.button_array[n].configure(image = self.photo1)
                    self.button_array[n].image = self.photo1

                if self.type_list[n] == 1:
                    self.button_array[n].configure(image = self.photo2)
                    self.button_array[n].image = self.photo2


    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text

    def initUI(self):
        # sets name and style of window
        self.parent.title("MapGen")
        self.style = Style()
        self.style.theme_use("default")

        self.photo1 = tk.PhotoImage(file="sprites/floorSprite.gif")
        self.photo2 = tk.PhotoImage(file="sprites/wallSprite.gif")

        self.frame.pack(fill=BOTH, expand=1)

        for n in range(0,1560):
            self.type_list.append(0)

        count = 1
        row = 0
        col = 0
        for n in range(0,1560):
            self.button_array.append(tk.Button(self.frame, text = str(n),
                image = self.photo1, height = 18, width = 18, borderwidth= -1,
                padx = 0, pady = 0, relief=FLAT))
            self.button_array[n].image = self.photo1
            self.button_array[n].bind('<Button-1>', self.buttonAction)
            self.button_array[n].grid(row=row , column=col)

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

        loadButton = Button(self, text="Load Map", command = self.loadFile)
        loadButton.pack(side=RIGHT, padx=5, pady=5)

def main():

    root = Tk()
    root.geometry("800x815")
    app = MapGen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
