from tkinter import *
from PIL import ImageTk, Image
from random import randint

        
def states():
    hide_all_frames()

    state_frame.pack(fill = 'both', expand = 1)
    
    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady = 15)
    random_state()

    # create answer input box
    global answer_input
    answer_input = Entry(state_frame, width = 15, font = ('Helvetica', 18), bd = 2)
    answer_input.pack(padx = 10, pady = 15)

    # create button to randomize state images
    rando_button = Button(state_frame, text = "Pass", command = states)
    rando_button.pack(pady = 10)

    # create a button to answer the questions
    answer_button = Button(state_frame, text = "Answer", command = state_answer)
    answer_button.pack(pady = 5)

    # create a label to tell us if we got the answer right or not
    global answer_label
    answer_label = Label(state_frame, text = '', font = ('Helvetica', 18), bg = 'white')
    answer_label.pack(pady = 15)

def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill = 'both', expand = 1)
    my_label = Label(state_capitals_frame, text = 'Capitals')
    my_label.pack()

def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
        
    state_frame.pack_forget()    
    state_capitals_frame.pack_forget()    

def state_answer():
    # clear the entry box
    answer_input.delete(0, END)
    
    global random_state
    answer = answer_input.get()
    answer = answer.replace(" ", "")

    # determne if our answer is right or wrong
    if answer.lower()  == our_states[rando]:
        response = "Correct! " + our_states[rando]
    else:
        response = "Inorrect! " + our_states[rando]

    answer_label.config(text = response.lower())

    random_state()

def random_state():
    # create a list of state names
    global our_states
    our_states = ['california', 'florida', 'illinois', 'kentucky',                      'nebraska', 'nevada', 'newyork', 'oregon', 'texas',                   'vermont']

    # generate a random number
    global rando
    rando = randint(0, len(our_states) - 1)
    state = 'states/' + our_states[rando] + '.png' 

    # create our state images
    global state_image  # usar global no pillow pra evitar bugs
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state.config(image = state_image, bg = 'white')



root = Tk()
root.title('Geography Flashcards!')
# root.geometry("500x500")

my_menu = Menu(root)
root.config(menu = my_menu)

states_menu = Menu(my_menu)
my_menu.add_cascade(label = 'Geography', menu = states_menu)
states_menu.add_command(label = 'States', command = states)
states_menu.add_command(label = 'State Capitals', command = state_capitals)
states_menu.add_separator()
states_menu.add_command(label = 'Exit', command = root.destroy)

# create our frames
state_frame = Frame(root, width = 500, height = 500, bg = 'white')
state_capitals_frame = Frame(root, width = 500, height = 500)


root.mainloop()