from tkinter import * 

root = Tk()

def my_click():
    greeting = f'Hello, {e.get()}!'
    my_label = Label(root, text = greeting)
    my_label.pack() 
    e.delete()

e = Entry(
    root,
    width = 50,
    bg = 'gray',
    fg = 'white',
    borderwidth = 3
    )
e.pack()
e.insert() 

my_button = Button(root, text = "Click Me!", command = my_click).pack()

root.mainloop()