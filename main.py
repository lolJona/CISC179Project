import csv
import tkinter
from tkinter import filedialog
import os
from csv import reader
from pandas import *
import pandas as pd

"""
Establish current directory
"""
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

"""
Define Functions
"""

def testpanda():
    panda_df.to_csv("Dow Jones Stocks February.csv", sep='-')

def outfile_error_label_disappear():
    outfile_error.pack_forget()


def outfile_error_label_appear():
    outfile_error.pack()


def openfile():
    openedfile = filedialog.askopenfilename()
    print(openedfile)

def singleclick():
    singlebuttonpress.config(state="disabled")

def csvrun():
    global default
    inname = filedialog.askopenfilename()
    if default == False:
        outname = str(outfilename_entry.get())
    else:
        outname = defaultname
    try:
        newfile = open(outname, "x")
    except:
        outfile_error_label_appear()
    if default == False:
        delim = str(newdelim.get())
    else:
        delim = "-"
    with open(inname, newline='') as infile, open(dir_path + "/" + outname, 'a', newline='') as outfile:
        reader = csv.reader(infile, delimiter=',')
        writer = csv.writer(outfile, delimiter=delim)
        for csvrow in reader:
            writer.writerow(csvrow)
        outfile_error_label_disappear()


def disable():
    global default
    newdelimlabel.config(state="disabled")
    newdelim.config(state="disabled")
    outfilename_label.config(state="disabled")
    outfilename_entry.config(state="disabled")
    convertButton.config(state="disabled")
    default = True


def enable():
    global default
    newdelimlabel.config(state="normal")
    newdelim.config(state="normal")
    outfilename_label.config(state="normal")
    outfilename_entry.config(state="normal")
    convertButton.config(state="normal")
    default = False


"""
A bunch of code which preps the second outfile, FebStockTips.  
Code continues around Line 288.
"""

infile = "Dow Jones Stocks February.csv"
with open(infile, "r") as csv_file:
    csv_reader = reader(csv_file)
    header = next(csv_reader)
    rows = list(csv_reader)

for row in rows:
    del row[0]
row0 = rows[0]
row1 = rows[1]
row2 = rows[2]
row3 = rows[3]
row4 = rows[4]
row5 = rows[5]
row6 = rows[6]
row7 = rows[7]
row18 = rows[18]
# row1sum = sum(float(row1))
row0sum = 0
row18sum = 0

for num in row0:
    num = float(num)
    row0sum = row0sum + num

for num in row18:
    num = float(num)
    row18sum = row18sum + num

# reading CSV file
data = read_csv(infile)

# converting column data to list
date = data[header[0]].tolist()
stock1 = data[header[1]].tolist()
stock2 = data[header[2]].tolist()
stock3 = data[header[3]].tolist()
stock4 = data[header[4]].tolist()
stock5 = data[header[5]].tolist()
stock6 = data[header[6]].tolist()
stock7 = data[header[7]].tolist()
stock8 = data[header[8]].tolist()

# converting lists to dicts
stock1dict = dict(zip(date, stock1))
stock2dict = dict(zip(date, stock2))
stock3dict = dict(zip(date, stock3))
stock4dict = dict(zip(date, stock4))
stock5dict = dict(zip(date, stock5))
stock6dict = dict(zip(date, stock6))
stock7dict = dict(zip(date, stock7))
stock8dict = dict(zip(date, stock8))

stock1_max = max(stock1dict.values())
stock1_max_date = max(stock1dict, key=stock1dict.get)
stock1_min_date = min(stock1dict, key=stock1dict.get)
stock1_min = min(stock1dict.values())
stock1_avg = sum(stock1dict.values()) / len(stock1dict)
stock1start = stock1dict.get("2/3/2020")
stock1end = stock1dict.get("2/28/2020")
stock1net = stock1end - stock1start

stock2_max = max(stock2dict.values())
stock2_max_date = max(stock2dict, key=stock2dict.get)
stock2_min_date = min(stock2dict, key=stock2dict.get)
stock2_min = min(stock2dict.values())
stock2_avg = sum(stock2dict.values()) / len(stock2dict)
stock2start = stock2dict.get("2/3/2020")
stock2end = stock2dict.get("2/28/2020")
stock2net = stock2end - stock2start

stock3_max = max(stock3dict.values())
stock3_max_date = max(stock3dict, key=stock3dict.get)
stock3_min_date = min(stock3dict, key=stock3dict.get)
stock3_min = min(stock3dict.values())
stock3_avg = sum(stock3dict.values()) / len(stock3dict)
stock3start = stock3dict.get("2/3/2020")
stock3end = stock3dict.get("2/28/2020")
stock3net = stock3end - stock3start

stock4_max = max(stock4dict.values())
stock4_max_date = max(stock4dict, key=stock4dict.get)
stock4_min_date = min(stock4dict, key=stock4dict.get)
stock4_min = min(stock4dict.values())
stock4_avg = sum(stock4dict.values()) / len(stock4dict)
stock4start = stock4dict.get("2/3/2020")
stock4end = stock4dict.get("2/28/2020")
stock4net = stock4end - stock4start

stock5_max = max(stock5dict.values())
stock5_max_date = max(stock5dict, key=stock5dict.get)
stock5_min_date = min(stock5dict, key=stock5dict.get)
stock5_min = min(stock5dict.values())
stock5_avg = sum(stock5dict.values()) / len(stock5dict)
stock5start = stock5dict.get("2/3/2020")
stock5end = stock5dict.get("2/28/2020")
stock5net = stock5end - stock5start

stock6_max = max(stock6dict.values())
stock6_max_date = max(stock6dict, key=stock6dict.get)
stock6_min_date = min(stock6dict, key=stock6dict.get)
stock6_min = min(stock6dict.values())
stock6_avg = sum(stock6dict.values()) / len(stock6dict)
stock6start = stock6dict.get("2/3/2020")
stock6end = stock6dict.get("2/28/2020")
stock6net = stock6end - stock6start

stock7_max = max(stock7dict.values())
stock7_max_date = max(stock7dict, key=stock7dict.get)
stock7_min_date = min(stock7dict, key=stock7dict.get)
stock7_min = min(stock7dict.values())
stock7_avg = sum(stock7dict.values()) / len(stock7dict)
stock7start = stock7dict.get("2/3/2020")
stock7end = stock7dict.get("2/28/2020")
stock7net = stock7end - stock7start

stock8_max = max(stock8dict.values())
stock8_max_date = max(stock8dict, key=stock8dict.get)
stock8_min_date = min(stock8dict, key=stock8dict.get)
stock8_min = min(stock8dict.values())
stock8_avg = sum(stock8dict.values()) / len(stock8dict)
stock8start = stock8dict.get("2/3/2020")
stock8end = stock8dict.get("2/28/2020")
stock8net = stock8end - stock8start

monthlygain = row18sum - row0sum
if monthlygain < 0:
    monthlygain = monthlygain * -1
    monthlygain1 = f"In the month of February, the overall value of this portfolio decreased by ${monthlygain:.2f}.\n"
else:
    monthlygain1 = f"In the month of February, the overall value of this portfolio increased by ${monthlygain:.2f}.\n"

if stock1net < 0:
    stock1net = stock1net * -1
    stock1net1 = f"{header[1]} decreased by ${stock1net:.2f} over the month.\n"
else:
    stock1net1 = f"{header[1]} increased by ${stock1net:.2f} over the month.\n"
if stock2net < 0:
    stock2net = stock2net * -1
    stock2net1 = f"{header[2]} decreased by ${stock2net:.2f} over the month.\n"
else:
    stock2net1 = f"{header[2]} increased by ${stock2net:.2f} over the month.\n"
if stock3net < 0:
    stock3net = stock3net * -1
    stock3net1 = f"{header[3]} decreased by ${stock3net:.2f} over the month.\n"
else:
    stock3net1 = f"{header[3]} increased by ${stock3net:.2f} over the month.\n"
if stock4net < 0:
    stock4net = stock4net * -1
    stock4net1 = f"{header[4]} decreased by ${stock4net:.2f} over the month.\n"
else:
    stock4net1 = f"{header[4]} increased by ${stock4net:.2f} over the month.\n"
if stock5net < 0:
    stock5net = stock5net * -1
    stock5net1 = f"{header[5]} decreased by ${stock5net:.2f} over the month.\n"
else:
    stock5net1 = f"{header[5]} increased by ${stock5net:.2f} over the month.\n"
if stock6net < 0:
    stock6net = stock6net * -1
    stock6net1 = f"{header[6]} decreased by ${stock6net:.2f} over the month.\n"
else:
    stock6net1 = f"{header[6]} increased by ${stock6net:.2f} over the month.\n"
if stock7net < 0:
    stock7net = stock7net * -1
    stock7net1 = f"{header[7]} decreased by ${stock7net:.2f} over the month.\n"
else:
    stock7net1 = f"{header[7]} increased by ${stock7net:.2f} over the month.\n"
if stock8net < 0:
    stock8net = stock8net * -1
    stock8net1 = f"{header[8]} decreased by ${stock8net:.2f} over the month.\n"
else:
    stock8net1 = f"{header[8]} increased by ${stock8net:.2f} over the month.\n"


def printer():
    with open("February Stock Tips.txt", "a") as q:
        print(
            f"Stock {header[1]} had its highest value of ${stock1_max:.2f} on {stock1_max_date}, and its lowest value of ${stock1_min:.2f} on {stock1_min_date}.\n"
            f"The average price of {header[1]} was ${stock1_avg:.2f}.\n"
            f"{stock1net1}\n"
            f"Stock {header[2]} had its highest value of ${stock2_max:.2f} on {stock2_max_date}, and its lowest value of ${stock2_min:.2f} on {stock2_min_date}.\n"
            f"The average price of {header[2]} was ${stock2_avg:.2f}.\n"
            f"{stock2net1}\n"
            f"Stock {header[3]} had its highest value of ${stock3_max:.2f} on {stock3_max_date}, and its lowest value of ${stock3_min:.2f} on {stock3_min_date}.\n"
            f"The average price of {header[3]} was ${stock3_avg:.2f}.\n"
            f"{stock3net1}\n"
            f"Stock {header[4]} had its highest value of ${stock4_max:.2f} on {stock4_max_date}, and its lowest value of ${stock4_min:.2f} on {stock4_min_date}.\n"
            f"The average price of {header[4]} was ${stock4_avg:.2f}.\n"
            f"{stock4net1}\n"
            f"Stock {header[5]} had its highest value of ${stock5_max:.2f} on {stock5_max_date}, and its lowest value of ${stock5_min:.2f} on {stock5_min_date}.\n"
            f"The average price of {header[5]} was ${stock5_avg:.2f}.\n"
            f"{stock5net1}\n"
            f"Stock {header[6]} had its highest value of ${stock6_max:.2f} on {stock6_max_date}, and its lowest value of ${stock6_min:.2f} on {stock6_min_date}.\n"
            f"The average price of {header[6]} was ${stock6_avg:.2f}.\n"
            f"{stock6net1}\n"
            f"Stock {header[7]} had its highest value of ${stock7_max:.2f} on {stock7_max_date}, and its lowest value of ${stock7_min:.2f} on {stock7_min_date}.\n"
            f"The average price of {header[7]} was ${stock7_avg:.2f}.\n"
            f"{stock7net1}\n"
            f"Stock {header[8]} had its highest value of ${stock8_max:.2f} on {stock8_max_date}, and its lowest value of ${stock8_min:.2f} on {stock8_min_date}.\n"
            f"The average price of {header[8]} was ${stock8_avg:.2f}.\n"
            f"{stock8net1}\n"
            f"{monthlygain1}", file=q)


"""
Set up tkinter GUI
"""
# Root Window
a = tkinter.Tk()
a.geometry("300x300")
a.title("CSV Toy")

# Build frame(s) and widgets
mainframe = tkinter.Frame(a)
headlabel = tkinter.Label(mainframe, text="CSV Converter", font="Osaka 36")
singlebuttonpress = tkinter.Button(mainframe, text="1-click",
                                   command=lambda: [testpanda(), printer(), singleclick()])
testlabel = tkinter.Label(mainframe, text="Would you like to use additional features?")
optional = tkinter.Radiobutton(mainframe, text="Yes", value=1, command=enable)
optional_no = tkinter.Radiobutton(mainframe, text="No", value=0, command=disable)

# OPTIONAL widgets
newdelimlabel = tkinter.Label(mainframe, text="New Delimiter:")
newdelim = tkinter.Entry(mainframe, width=2)
outfile_error = tkinter.Label(mainframe, text="This file already exists!", font="Calibri 9", fg="red")
outfilename_label = tkinter.Label(mainframe, text="New outfile name:")
outfilename_entry = tkinter.Entry(mainframe, width=30)

# NOT OPTIONAL
openfilebutton = tkinter.Button(mainframe, text="Open", command=openfile)
convertButton = tkinter.Button(mainframe, text="Convert File", command=lambda: [csvrun(), printer()])
quitButton = tkinter.Button(mainframe, text="Quit", command=mainframe.quit)

"""
PACKING EVERYTHING
"""
mainframe.pack()
headlabel.pack()
singlebuttonpress.pack()
testlabel.pack()
optional.pack()
optional_no.pack()
newdelimlabel.pack()
newdelim.pack()
outfile_error.pack()
outfilename_label.pack()
outfilename_entry.pack()
# openfilebutton.pack()
convertButton.pack(side='left')
quitButton.pack(side='right')

# SETTING DEFAULTS and VARIABLES
disable()
defaultname = "Dow Jones Stocks February.csv"
default = True
delim = "-"
outfile_error_label_disappear()
inname = dir_path + "/" + "Dow Jones Stocks February.csv"
panda_df = pd.read_csv(inname)

"""
RUN TKINTER WINDOW
"""
a.mainloop()
