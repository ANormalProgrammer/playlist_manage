import tkinter as tk

WIDTH = 50

def on_enter(e):
    e.widget['background'] = '#fafafa'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'

def create_button(window, text, width, command=None):
    button = tk.Button(window, text = text, width=width, command = command)
    button.pack()
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button

def if_can_add_to_playlist(song_name):
    global song_list
    if not song_name:
        return False
    if song_name in song_list:
        return False
    return True

def add():
    global song_list
    global list_song
    song_name = input_song_list.get()

    if  if_can_add_to_playlist(song_name):
        song_list.append(song_name)
        list_song.insert(len(song_list), song_name)
        print(song_list)
    input_song_list.delete(0, tk.END)


def remove():
    list_song.delete(tk.ANCHOR)
    
    

window = tk.Tk()
song_list = []
input_song_list = tk.Entry(window, width=WIDTH)
input_song_list.pack()

button_input = create_button(window, "add to playlist", WIDTH, add)

list_song = tk.Listbox(window, width = WIDTH)
list_song.pack()

button_delete = create_button(window, "remove from playlist", WIDTH, remove)


window.mainloop()


