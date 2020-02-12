from twisted_fate import Deck
import tkinter as tk
# test decks:
# CEBACAIADADQCAQGC4NCQKJRHEBAEAICAIGAGAIAAYNCUAQDAEAAOHRJAMAQEAIYDY
# CEAAEBABAINCSNJWBAAQACIOCQNB2JZKFQBAMAICBQSCQLJRHEFACAADAYFAWHRSGM2DKNQ

def clicked():
    deck1 = Deck.decode(txt1.get())
    deck2 = Deck.decode(txt2.get())
    diff = var.get()
    text_left.config(state=tk.NORMAL)
    text_right.config(state=tk.NORMAL)
    text_left.delete(1.0, tk.END)
    text_right.delete(1.0, tk.END)
    champions = deck1.champions() + deck2.champions()
    champions = set(champions)
    if diff == 0:
        for card in deck1.cards:
            if card.name not in champions:
                if card not in deck2.cards:
                    text_left.insert(tk.END, f'+ {card.count} {card.name}\n')
                else:
                    diff_card = card.count - deck2.cards[deck2.index(card)]
                    if diff_card > 0:
                        text_left.insert(tk.END, f'+ {diff_card} {card.name}\n')
            else:
                diff = card.count
                for i in range(len(deck2.cards)):
                    if deck2.cards[i].name == card.name:
                        diff -= deck2.cards[i].count
                if diff > 0:
                    text_left.insert(1.0, f'+ {diff} {card.name}\n')

        for card in deck2.cards:
            if card.name not in champions:
                if card not in deck1.cards:
                    text_right.insert(tk.END, f'+ {card.count} {card.name}\n')
                else:
                    diff_card = card.count - deck1.cards[deck1.index(card)]
                    if diff_card > 0:
                        text_right.insert(tk.END, f'+ {diff_card} {card.name}\n')
            else:
                diff = card.count
                for i in range(len(deck1.cards)):
                    if deck1.cards[i].name == card.name:
                        diff -= deck1.cards[i].count
                if diff > 0:
                    text_right.insert(1.0, f'+ {diff} {card.name}\n')
    # for card in deck1.cards:
    #     text_left.insert(tk.END, f'{card.name} x {card.count}\n')
    #
    # for card in deck2.cards:
    #     text_right.insert(tk.END, f'{card.name} x {card.count}\n')

    text_left.config(state=tk.DISABLED)
    text_right.config(state=tk.DISABLED)


window = tk.Tk()
window.title("Deck Comparer")
frame = tk.Frame()
pad = 5
# window.geometry('350x800')

lbl = tk.Label(window, text="First Deck Code")
txt1 = tk.Entry(window, width=40)
lbl2 = tk.Label(window, text="Second Deck Code")
txt2 = tk.Entry(window, width=40)
btn = tk.Button(window, text="Compare", command=clicked)
var = tk.IntVar()
r_btn_diff = tk.Radiobutton(window, text='Difference', variable=var, value=0)
r_btn_diff.select()
r_btn_same = tk.Radiobutton(window, text='Same', variable=var, value=1)

left_lbl = tk.Label(frame, text='Deck 1')
right_lbl = tk.Label(frame, text='Deck 2')
text_left = tk.Text(frame, height=40, width=30, state=tk.DISABLED)
text_right = tk.Text(frame, height=40, width=30, state=tk.DISABLED)

# GRID LAYOUT
lbl.grid(column=0, row=0, padx=pad, pady=pad, sticky=tk.W)
txt1.grid(column=1, row=0, padx=pad, pady=pad)
lbl2.grid(column=0, row=1, padx=pad, pady=pad, sticky=tk.W)
txt2.grid(column=1, row=1, padx=pad, pady=pad)
r_btn_diff.grid(column=2, row=0, sticky=tk.W)
r_btn_same.grid(column=2, row=1, sticky=tk.W)
btn.grid(columnspan=3, column=0, row=2, pady=pad)

frame.grid(columnspan=3, column=0, row=3, pady=pad, padx=pad)
left_lbl.grid(column=0, row=0)
right_lbl.grid(column=1, row=0)
text_left.grid(column=0, row=1, pady=pad, sticky=tk.E)
text_right.grid(column=1, row=1, pady=pad)


window.mainloop()