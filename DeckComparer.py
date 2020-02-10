from twisted_fate import Deck
import tkinter as tk


def clicked():
    deck1 = Deck.decode(txt1.get())
    deck2 = Deck.decode(txt2.get())


window = tk.Tk()
window.title("Deck Comparer")
pad = 5
# window.geometry('350x800')

lbl = tk.Label(window, text="First Deck")
txt1 = tk.Entry(window, width=40)
lbl2 = tk.Label(window, text="Second Deck")
txt2 = tk.Entry(window, width=40)

deck = Deck.decode("CEBACAIADADQCAQGC4NCQKJRHEBAEAICAIGAGAIAAYNCUAQDAEAAOHRJAMAQEAIYDY")
text_box = tk.Text(window, height=2, width=40)


# GRID LAYOUT
lbl.grid(column=0, row=0, padx=pad, pady=pad)
txt1.grid(column=1, row=0, padx=pad, pady=pad)
lbl2.grid(column=0, row=1, padx=pad, pady=pad)
txt2.grid(column=1, row=1, padx=pad, pady=pad)
text_box.grid(columnspan=2, column=0, row=2, pady=pad)
# btn.grid(column=1, row=3)


window.mainloop()