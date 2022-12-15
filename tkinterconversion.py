import csv
import tkinter as tk
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Root Window
        self.title('CSV Converter')
        self.geometry('300x300')

        #Main Frame
        self.frame = tk.Frame(self)
        self.headlabel = tk.Label(self, text="CSV Converter", font="Osaka 36")
        self.singlebuttonpress = tk.Button(self, text="1-click",
                                   command=lambda: [testpanda(), printer(), singleclick()])
        self.testlabel = tk.Label(self, text="Would you like to use additional features?")
        self.optional = tk.Radiobutton(self, text="Yes", value=1, command=enable)
        self.optional_no = tk.Radiobutton(self, text="No", value=0, command=disable)
        # OPTIONAL widgets
        self.newdelimlabel = tk.Label(self, text="New Delimiter:")
        self.newdelim = tk.Entry(self, width=2)
        self.outfile_error = tk.Label(self, text="This file already exists!", font="Calibri 9", fg="red")
        self.outfilename_label = tk.Label(self, text="New outfile name:")
        self.outfilename_entry = tk.Entry(self, width=30)

        # NOT OPTIONAL
        self.openfilebutton = tk.Button(self, text="Open", command=openfile)
        self.convertButton = tk.Button(self, text="Convert File", command=lambda: [csvrun(), printer()])
        self.quitButton = tk.Button(self, text="Quit", command=mainframe.quit)

        self.frame.pack()
        self.headlabel.pack()
        self.singlebuttonpress.pack()
        self.testlabel.pack()
        self.optional.pack()
        self.optional_no.pack()
        self.newdelimlabel.pack()
        self.newdelim.pack()
        self.outfile_error.pack()
        self.outfilename_label.pack()
        self.outfilename_entry.pack()
        self.openfilebutton.pack()
        self.convertButton.pack()
        self.quitButton.pack()
app = App()
app.mainloop()