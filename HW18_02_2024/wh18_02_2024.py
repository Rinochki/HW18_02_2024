from tkinter import *
root = Tk()

text = '<3 дихайте <3 0_0'
text1 = 'x_x не дихайте x_x'

nom = 0

def on_button_click(event):
    global nom
    nom += 1
    root.title(f"Клацнуто: {nom}")
    if label.cget("text") == text:
        label.config(text=text1)
    else:
        label.config(text=text)


w1 = root.winfo_screenwidth() # ширина екрану
h1 = root.winfo_screenheight() # висота екрану
root.geometry(f"200x200+{int(w1/2-100)}+{int(h1/2-100)}")

label = Label(root, text=text)
label.pack()

button = Button(root, bg="Gray", text="Натисни мене!")
button.pack()
button.bind("<Button-1>", on_button_click)

root.mainloop()