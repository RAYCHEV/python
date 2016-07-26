from tkinter import *
from time import sleep
root = Tk()

def btn_one():
    print('button one is pressed')
    return 1


top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button_one = Button(top_frame, text = "Button one", fg='red', bg='green', command = btn_one)
button_two = Button(top_frame, text = "Button two")
button_three = Button(top_frame, text = "Button three")
button_four = Button(bottom_frame, text = "Button four", fg='blue')

button_one.pack(side=LEFT)
button_two.pack(side=LEFT)
button_three.pack(side=LEFT)
button_four.pack(side=BOTTOM)

root.after(30000, lambda: root.destroy()) # 30 sec
root.mainloop()