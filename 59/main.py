import tkinter as tk
from tkinter.messagebox import *

window = tk.Tk()

window.title("Program Titid Bau Kencur")
window.configure(background="light blue")

window.geometry("800x600")
window.resizable(False , False)

# frame input
input_frame = tk.Frame(window)
input_frame.pack(pady=10 , padx=10 , fill="x" , expand=True)

nama_depan_label = tk.Label(input_frame , text="Nama Depan" , font=("Arial" , 12))
nama_depan_label.pack(pady=10 , padx=10 , fill="x" , expand=True)

NAMA_DEPAN = tk.StringVar()
nama_depan_entry = tk.Entry(input_frame , textvariable=NAMA_DEPAN)
nama_depan_entry.pack(pady=10 , padx=10 , fill="x" , expand=True)

def tombol_click():
    nama_depan = NAMA_DEPAN.get()
    showinfo("Sapa" , f"Halo {nama_depan}")

tombol_sapa = tk.Button(input_frame , text="Sapa" , font=("Arial" , 12) ,command=tombol_click)
tombol_sapa.pack(pady=10 , padx=10 , fill="x" , expand=True)

window.mainloop()