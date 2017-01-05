import tkinter as tk

def toggle():

    if btn.config('text')[-1] == 'ON':

        btn.config(text='OFF')
        # my ON code here
        print("on")

    else:

        btn.config(text='ON')
        # my Off code here
        print("OFF")

root = tk.Tk()
btn = tk.Button(text="ON", width=12, command=toggle)
btn.pack(pady=5)

root.after(30000, lambda: root.destroy()) # 30 sec
root.mainloop()


