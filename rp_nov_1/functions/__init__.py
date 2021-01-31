from tkinter import *
from tkinter import filedialog
import pygame


def should_round_down(val: float):
    if val < 0:
        return ((val * -1) % 1) < 0.5
    return (val % 1) < 0.5


def round1(val: float, ndigits=2):
    import math
    if ndigits > 0:
        val *= 10 ** (ndigits - 1)
    is_positive = val > 0
    tmp_val = val
    if not is_positive:
        tmp_val *= -1
    rounded_value = math.floor(tmp_val) if should_round_down(val) else math.ceil(tmp_val)
    if not is_positive:
        rounded_value *= -1
    if ndigits > 0:
        rounded_value /= 10 ** (ndigits - 1)
    return rounded_value


bnm = '#2F4F4F'
bhj = '#7969E1'
bdwd = 1
relif = 'groove'
global ply
ply = False

global paused
paused = False

global vol
vol = round1(0.2, 2)

global mudo
mudo = 0.0

global parametro
parametro = False

root = Tk()
root.title('Codemy.com MP3 Player')
root.iconbitmap('C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/toque1.ico')
root.geometry("605x300")
root.configure(background=bnm)

# Inicializar pygame music

pygame.mixer.init()


# Add song function


def add_song():
    songs = filedialog.askopenfilenames(initialdir='K:/Music',
                                        title='Choose a song',
                                        filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        if '.mp3' in song or '.flac' in song:
            song_box.insert(END, song)


def play():
    global ply
    global parametro
    song = song_box.get(ACTIVE)
    if song:
        ply = True
        parametro = True
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)


def stop():
    global ply
    global parametro
    ply = False
    parametro = False
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)


def volume_me():
    global ply
    global vol
    global parametro
    if ply:
        if parametro:
            if vol >= 0.1:
                vol -= round1(0.1, 2)
            pygame.mixer.music.set_volume(round1(vol, 2))


def volume_ma():
    global ply
    global vol
    global parametro
    if ply:
        if parametro:
            if vol <= 0.9:
                vol += round1(0.1, 2)
            pygame.mixer.music.set_volume(round1(vol, 2))


def mute():
    global ply
    global parametro
    global vol
    global mudo
    if ply:
        if parametro:
            pygame.mixer.music.set_volume(mudo)
            parametro = False
            vol_btn_mute.configure(bg=bhj)
        else:
            pygame.mixer.music.set_volume(vol)
            parametro = True
            vol_btn_mute.configure(bg=bnm)


def pause(is_paused):
    global ply
    global paused
    if ply:
        paused = is_paused
        if paused:
            pygame.mixer.music.unpause()
            paused = False
            pause_btn.configure(bg=bnm)
        else:
            pygame.mixer.music.pause()
            paused = True
            pause_btn.configure(bg=bhj)


# Create playlist box


song_box = Listbox(root, bg='#000000', fg='#00FA9A', width=85,
                   selectbackground='#F0E68C', selectforeground='#000000', )
song_box.pack(pady=10)

# "define player control button images

back_btn_img = PhotoImage(file='C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/de-volta.png')
forward_btn_img = PhotoImage(file='C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/proximo.png')
play_btn_img = PhotoImage(file='C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/toque.png')
pause_btn_img = PhotoImage(file='C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/pausa.png')
stop_btn_img = PhotoImage(file='C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/pare.png')
vol_btn_img_menos = PhotoImage(file='C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/diminuir-volume.png')
vol_btn_img_mais = PhotoImage(file='C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/aumentar-volume.png')
vol_btn_mute_img = PhotoImage(file='C:/Users/alexa/PycharmProjects/Curso_Python3/rp_nov_1/images/mudo.png')

# Create player control button images

controls_frame = Frame(root)
controls_frame.configure(background=bnm)
controls_frame.pack()

# Create player controls buttons

back_btn = Button(controls_frame, image=back_btn_img, borderwidth=bdwd, relief=relif)
back_btn.configure(bg=bnm, activebackground=bhj)
forward_btn = Button(controls_frame, image=forward_btn_img, relief=relif, borderwidth=bdwd)
forward_btn.configure(bg=bnm, activebackground=bhj)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=bdwd, relief=relif, command=play)
play_btn.configure(bg=bnm, activebackground=bhj)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=bdwd, relief=relif, command=lambda: pause(paused))
pause_btn.configure(bg=bnm, activebackground=bhj)
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=bdwd, relief=relif, command=stop)
stop_btn.configure(bg=bnm, activebackground=bhj)
vol_btn_menos = Button(controls_frame, image=vol_btn_img_menos, borderwidth=bdwd, relief=relif, command=volume_me)
vol_btn_menos.configure(bg=bnm, activebackground=bhj)
vol_btn_mais = Button(controls_frame, image=vol_btn_img_mais, borderwidth=bdwd, relief=relif, command=volume_ma)
vol_btn_mais.configure(bg=bnm, activebackground=bhj)
vol_btn_mute = Button(controls_frame, image=vol_btn_mute_img, borderwidth=bdwd, relief=relif, command=mute)
vol_btn_mute.configure(bg=bnm, activebackground=bhj)

back_btn.grid(row=0, column=0, padx=15)
forward_btn.grid(row=0, column=4, padx=15)
play_btn.grid(row=0, column=2, padx=15)
pause_btn.grid(row=0, column=3, padx=15)
stop_btn.grid(row=0, column=1, padx=15)
vol_btn_menos.grid(row=0, column=5, padx=1)
vol_btn_mais.grid(row=0, column=6, padx=1)
vol_btn_mute.grid(row=0, column=7, padx=1)

# Create menu

my_menu = Menu(root)
root.config(menu=my_menu)

# "Add add song menu

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add song to playlist", command=add_song)

root.mainloop()
