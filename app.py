import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import re

def open_file(txt,root):
    txt.set("Loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a PDF to upload",filetype=[("Pdf file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        
        # Extracting text and fixing it from raw text, replacing foreign characters
        page_content = page.extractText()
        page_content = re.sub('[^a-zA-Z0-9 \n\.]', '', page_content)

        # text box
        text_box = tk.Text(root,height=10,width=75, padx=15, pady=15)
        text_box.insert(1.0,page_content)
        """text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")"""
        text_box.grid(column=1,row=3)

        txt.set("Browse Files")

def main():
    print("do Something")
    
    # Create Tkinter root object
    root = tk.Tk()

    # Tkinter Canvas Object
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.grid(columnspan=3,rowspan=3)

    # Logo for the App
    logo = Image.open("tome.png")
    # Convert to Tkinter Image
    logo = ImageTk.PhotoImage(logo)
    # Logo widget
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    
    # Place image in grid
    logo_label.grid(column=1,row=0)

    # Instructions on how to use
    instructions = tk.Label(root, text="Scan in a PDF to read!", font="Raleway")
    # Placing label on grid
    instructions.grid(columnspan=3, column=0, row=1)

    # Browse user files for upload
    browse_text = tk.StringVar()
    browse_button = tk.Button(root, textvariable=browse_text, command=lambda:open_file(browse_text, root), font="Raleway", bg="#20bebe",fg="white",height=2,width=15)
    browse_text.set("Browse Files")
    browse_button.grid(column=1,row=2)

    # Lazy way to add vertical margins
    canvas = tk.Canvas(root, width=800, height=200)
    canvas.grid(columnspan=3)
    # All changes to root before calling root.mainloop
    root.mainloop()
if __name__ == "__main__":
    main()