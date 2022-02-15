'''
TITLE: Tome To Read
AUTHOR: James Thomason
DESCRIPTION: So far this is the welcome page. Probably will integrate most things from this file into the main file. \
            However, this is just the skeleton for the main page that displays the Logo as well as a welcome.
            The welcome screen itself will have the functionality of being able to click anywhere on screen to switch
            over to the main screen. 

'''
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


def welcome_page():
    # Tkinter Root object
    window = tk.Tk()
    # Title of the window
    window.title("Tome to Read")
    # Setting geometry of window
    window.geometry("900x800")
    # Creating a frame from the window
    frame = Frame(window)
    frame.pack()
    add_main_logo(window)
    instructions(window)
    return window

def add_main_logo(window):
    '''
    This function is strictly only to be called within the welcome_page fucntion. 
    '''
    # Creating the Image object
    logo = Image.open("TomeToRead_Logo.png")
    # Resizing image to be bigger
    logo = logo.resize((350,380))
    # Convert logo to Tkinter Image
    logo = ImageTk.PhotoImage(logo)
    # Logo widget
    logo_label = Label(window,image=logo)
    logo_label.image = logo
    # Place image in the window relatively centered
    logo_label.place(relx=.5, rely=.3, anchor= CENTER)
    
def instructions(window):
    '''
    This function is strictly only to be called within the welcome_page function
    '''
    instructions = Label(window,text="Click anywhere to begin!", font=("Raleway", 32))
    instructions.place(relx=.5,rely=.75, anchor= S)


def main():
    # Main window that pops up
    window = welcome_page()
    window.mainloop()

if __name__ == "__main__":
    main()