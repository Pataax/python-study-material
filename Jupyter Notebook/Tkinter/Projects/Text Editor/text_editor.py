from tkinter import *
from tkinter import filedialog
from tkinter import font

def new_file():
    my_text.delete(1.0, END)
    root.title('New File - TextPad!')
    status_bar.config(text = 'New File')

def open_file():
    # my_text.delete(1.0, END)
    text_file = filedialog.askopenfilename(title = 'Open File', 
                filetypes = (('Text Files', '*.txt'),))
    
    name = text_file
    status_bar.config(text= name)

    if text_file:  # somente se eu selecionar algum arquivo
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        my_text.insert('end', stuff)

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension = '.*', title = 'Save File',
                filetypes = (('Text Files', '*.txt'),))

        


root = Tk()
root.title('Codemy.com - TextPad!')
root.geometry('1200x600')

# create main frame
my_frame = Frame(root)
my_frame.pack(pady = 5)

# create scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = 'right', fill = 'y')

# create text box
my_text = Text(my_frame, width = 97, height = 20, font = ('helvetica', 16), 
        selectbackground = 'yellow', selectforeground = 'black', undo = True,
        yscrollcommand = text_scroll.set)
my_text.pack()

# configure scrollbar
text_scroll.config(command = my_text.yview)

# create menu
my_menu = Menu(root)
root.config(menu = my_menu)

# add file menu
# retira a opção de destacar o menu
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'New', command = new_file)
file_menu.add_command(label = 'Open', command = open_file)
file_menu.add_command(label = 'Save')
file_menu.add_command(label = 'Save As', command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command = root.quit)

# add edit menu
edit_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = 'Edit', menu = edit_menu)
edit_menu.add_command(label = 'Cut')
edit_menu.add_command(label = 'Copy')
edit_menu.add_command(label = 'Undo')
edit_menu.add_command(label = 'Redo')

# add status bar to bottom of app
status_bar = Label(root, text = 'Ready', anchor = 'e')
status_bar.pack(fill = 'x', side = 'bottom', ipady = 5)


root.mainloop()