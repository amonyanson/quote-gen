import requests

import tkinter as ttk
import ttkbootstrap as tkk

url = "insert api server link here"

root = ttk.Window(themename="pulse")
root.title("Quotes Generator")
root.geometry("700x250")

frame = ttk.Frame(root)
frame.pack(padx=30,pady=40)

quote_label = ttk.Label(frame, text="",font=("Helvetica",16),wraplength=650)
quote_label.pack()

author_label = ttk.Label(frame,text="",font=("Helvetica",12)
author_label.pack(pady)