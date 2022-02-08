'''
So basically this is a mock up of taking in some different domain free stories as text files, check out the csv file I added to see which stories.
This combines a mix of GUI and python inputs.

'''
import tkinter as tk
import tkinter.scrolledtext as tkst
from turtle import position
import pandas as pd
import requests
from io import StringIO
import requests

url='https://raw.githubusercontent.com/colbychambers25/immersive-ebook/main/Domain_Free_eBook.csv'
book_library = pd.read_csv(url)

def get_from_library(target_url):
    response = requests.get(target_url)
    data = response.text
    return(data)


diction = {}
i = 0
for row in book_library['Title']:
    diction[book_library['Title'][i]] = i
    print(diction)
    i+=1
print("Which book would you like to read?")
print(book_library["Title"])
book_to_get = str(input())
index = diction[book_to_get]
story = get_from_library(target_url = book_library['URL'][index])

window = tk.Tk()
window.title("Immersive Reading")
window.configure(bg="gray")
window.geometry("650x700")

frame = tk.Frame(window)
frame.pack()

wid = 500
hei = 675

canvas = tk.Canvas(frame, bg="dark gray", width=wid, height=hei)
canvas.config(highlightthickness=0)
canvas.pack()

canvas.create_text(300, 60, text=story, fill="black", font=('Helvetica 8'))
canvas.pack()

window.mainloop()
'''
window = tk.Tk()
window.title("Immersive Reading")
window.configure(bg="gray")
window.geometry("650x700")

frame = tk.Frame(window)
frame.pack()

wid = 500
hei = 675

canvas = tk.Canvas(frame, bg="dark gray", width=wid, height=hei)
canvas.config(highlightthickness=0)
canvas.pack()

btn = tk.Button(
    window,
    text="My Button",
    height=2,
    width=10,
)

btn.pack(side="left")
btn.place(x=10, y=hei / 2)

window.mainloop()
'''
