# THIS WILL BE THE MAIN PAGE CLASS!!!
# I AM STILL WORKING ON CONVERTING IT INTO THE CUSTOMTKINTER FORMAT
# SO THAT'S WHY IT'S NOT WORKING YET!

from tkinter import *
from turtle import color, position
import pandas as pd
import requests
import pygame
import customtkinter

pygame.mixer.init()

# Music: https://www.bensound.com
sound = "bensound-theelevatorbossanova.mp3"
theme = "blue"
photo = "tome.png"

class Menu:

    def __init__(self, sound, theme, photo):
        self.sound = sound
        self.theme = theme
        self.photo = photo
        if __name__ == "__main__":
            self.main()
    
    def main_menu(self, window):

        au_button = customtkinter.CTkButton(width=80, height=80, border_width=0, corner_radius=8, text = 'About Us', \
            image = self.photo, text_color='black', command = lambda: self.pages(window))
        au_button.pack(side="right")
        au_button.place(relx=.5, rely=.5,x=-410, anchor=CENTER)

        lib_button = customtkinter.CTkButton(width=80, height=80, border_width=0, corner_radius=8, text = 'Library', \
            image = self.photo, text_color='black', command = lambda: self.pages(window))
        lib_button.pack(side="right")
        lib_button.place(relx=.5, rely=.5,x=-410, anchor=CENTER)

        upl_button = customtkinter.CTkButton(width=80, height=80, border_width=0, corner_radius=8, text = 'Upload', \
            image = self.photo, text_color='black', command = lambda: self.pages(window))
        upl_button.pack(side="right")
        upl_button.place(relx=.5, rely=.5,x=-410, anchor=CENTER)

        set_button = Button(window, text = 'Settings') # buttons for Settings page
        set_button.place(x = 915, y = 578)

        set_button = customtkinter.CTkButton(width=80, height=80, border_width=0, corner_radius=8, text = 'Settings', \
            image = self.photo, text_color='black', command = lambda: self.pages(window))
        set_button.pack(side="right")
        set_button.place(relx=.5, rely=.5,x=-410, anchor=CENTER)

        logo = PhotoImage(file = 'tome.png') # inserts the logo
        logo_label = Label(image = logo) # names the logo
        logo_label.place(x = 625, y = 200) # places the logo on the canvas

        
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play(loops=3000)


    def main(self):
        ''' 
        Creates the window, and calls this diction function to get a key value pair linked by page number.
        Currently only supports .txt files because pdf files lack the functionality 
        to be manipulated and most domain stories use .txt or .epub not pdf.
        '''
        window = customtkinter.CTk()
        customtkinter.set_default_color_theme(self.theme)
        window.title("Immersive Reading")
        window.configure(bg = 'gray')
        window.geometry("1200x800")
        frame = Frame(window)
        frame.pack()
        window.counter = -1 #this is universal counter funtion that allows a user to traverse a story.
        self.main_menu(window)
        window.mainloop() #basically refreshes the window

Menu(sound, theme, photo)

