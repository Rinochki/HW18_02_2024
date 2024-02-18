from tkinter import *
root = Tk()

text = 'Мопти'
text1 = 'Йопти'

nom = 0

def on_button_click(event):
    global nom
    nom += 1
    root.title(f"Клацнуто: {nom}")






w1 = root.winfo_screenwidth() # ширина екрану
h1 = root.winfo_screenheight() # висота екрану
root.geometry(f"500x500+{int(w1/2-250)}+{int(h1/2-250)}")


button = Button(root, bg="Gray", text="Натисни мене!")
button.pack()
button.bind("<Button-1>", on_button_click)

root.mainloop()