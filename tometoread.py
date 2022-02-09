'''
So basically this is a mock up of taking in some different domain free stories as text files, check out the csv file I added to see which stories.
This combines a mix of GUI and python inputs.

'''
from tkinter import *
import tkinter.scrolledtext as tkst
from turtle import position
import pandas as pd
import requests
from io import StringIO
import PyPDF2

# url='https://raw.githubusercontent.com/colbychambers25/immersive-ebook/main/Domain_Free_eBook.csv'
# book_library = pd.read_csv(url)

def get_from_library(target_url):
    response = requests.get(target_url)
    data = response.text
    return(data)


# make this function an actual page on the tkinter page, prompts the user on the
# window to type in the wanted ebook. Show the available options of ebooks

def populate_book_dictionary_prompt_user():
    '''
    This function populates a dictionary of Title : URL pairs that are retrieved from a csv
    file. The csv file is read using pd.read_csv and then the key value pairs are added to a dictionary.
    The user is prompted in the tkinter window to select from a certain amount of stories to read.
    This dictionary is then used to make a request to the url value to get the story that the user
    wants to read. 
    '''
    url='https://raw.githubusercontent.com/colbychambers25/immersive-ebook/main/Domain_Free_eBook.csv'
    book_library = pd.read_csv(url)
    diction = {}
    library_str = ''
    for i,title in enumerate(book_library['Title']):
        diction[book_library['Title'][i]] = book_library.iloc[i]['URL']
        library_str += title + "\n"
        # print(diction) checking if its processing correctly
    
    print("Which book would you like to read?") # Asking user for input
    print(library_str) # Prints out the library to the user
    book_to_get = str(input())
    story = get_from_library(target_url = diction[book_to_get])
    return story


def main():
    i=25

    # James - I turned the story variable into a whole function that RETURNS story
    story = populate_book_dictionary_prompt_user()
    pages=story.strip().splitlines()
    print(len(pages))
    final_pages = []
    '''
    for page in pages:
        if i%25 ==0 or i== len(pages)-1:
            final_pages.append(page)
            print(page)
        i+=1
    print(len(final_pages))
    '''
    window = Tk()
    window.title("Immersive Reading")
    window.configure(bg="gray")
    window.geometry("700x800")

    frame = Frame(window)
    frame.pack()

    wid = 595
    hei = 770

    canvas = Canvas(bg="dark gray", width=wid, height=hei)
    canvas.place(relx=.5, rely=.5, anchor=CENTER)
    canvas.config(highlightthickness=0)
    text = canvas.create_text(300, 100, text=story, fill="black", font=('Times 15'),width=430)
    canvas.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
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
