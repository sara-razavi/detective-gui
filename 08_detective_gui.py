# Name: Sara Razavi
# Student ID: 970050118
# Focus: functions, variables, lists/dictionaries, if statements and Tkinter
# global variables, functions, dictionaries, lists, if statements and buttons.
# I made it as a small text-style detective game inside a window.
# course: Fundamentals of Computer Science and Programming

import tkinter as tk
from tkinter import messagebox

score = 0
inventory = []

clues = {
    "library": False,
    "garden": False,
    "office": False
}

def add_item(item):
    if item not in inventory:
        inventory.append(item)
        update_inventory()

def update_inventory():
    inventory_box.delete(0, tk.END)

    if len(inventory) == 0:
        inventory_box.insert(tk.END, "Nothing yet...")
    else:
        for item in inventory:
            inventory_box.insert(tk.END, item)

def show_message(text):
    story_label.config(text=text)

def library():
    global score

    if clues["library"]:
        show_message("You already searched the library.")
        return

    clues["library"] = True
    score += 1
    add_item("Old key")
    show_message(
        "You search the library. Behind an old book you find a key.\n"
        "There is a small symbol on it."
    )

def garden():
    global score

    if clues["garden"]:
        show_message("You already searched the garden.")
        return

    clues["garden"] = True
    score += 1
    add_item("Red thread")
    show_message(
        "Near the garden door you find a piece of red thread.\n"
        "It looks like it came from someone's coat."
    )

def office():
    global score

    if clues["office"]:
        show_message("You already searched the office.")
        return

    clues["office"] = True
    score += 1
    add_item("Note")
    show_message(
        "Inside the desk there is a note:\n"
        "\"The person with the key knows the truth.\""
    )

def inspect_key():
    if "Old key" in inventory:
        show_message(
            "The symbol on the key matches the symbol on the office drawer."
        )
    else:
        show_message("You don't have a key yet.")

def inspect_thread():
    if "Red thread" in inventory:
        show_message(
            "The thread looks like it came from a dark red jacket."
        )
    else:
        show_message("You don't have the thread yet.")

def open_drawer():
    if "Old key" in inventory:
        add_item("Final clue")
        show_message(
            "The key opens the drawer. Inside you find a final clue."
        )
    else:
        show_message("The drawer is locked.")

def final_guess():
    global score

    if "Final clue" not in inventory:
        show_message("You don't have enough clues to make a final guess.")
        return

    choice = suspect_entry.get().strip().lower()

    if choice == "butler":
        score += 3
        messagebox.showinfo(
            "Case Solved",
            "You solved the case!\nScore: " + str(score)
        )
        show_message("CASE SOLVED. The butler had the missing item.")
    elif choice == "":
        show_message("Write a suspect name first.")
    else:
        score -= 1
        messagebox.showinfo(
            "Wrong Guess",
            "That suspect does not fit the clues.\nScore: " + str(score)
        )

def reset_game():
    global score

    score = 0
    inventory.clear()

    for key in clues:
        clues[key] = False

    suspect_entry.delete(0, tk.END)
    update_inventory()
    show_message("The case has been reset. Start investigating.")

window = tk.Tk()
window.title("The Missing Diamond")
window.geometry("650x600")

title = tk.Label(
    window,
    text="THE MISSING DIAMOND",
    font=("Arial", 18)
)
title.pack(pady=10)

story_label = tk.Label(
    window,
    text="A diamond disappeared from the mansion.\nStart investigating.",
    wraplength=570,
    justify="center"
)
story_label.pack(pady=15)

location_frame = tk.Frame(window)
location_frame.pack()

tk.Button(
    location_frame,
    text="Search Library",
    width=16,
    command=library
).grid(row=0, column=0, padx=5)

tk.Button(
    location_frame,
    text="Search Garden",
    width=16,
    command=garden
).grid(row=0, column=1, padx=5)

tk.Button(
    location_frame,
    text="Search Office",
    width=16,
    command=office
).grid(row=0, column=2, padx=5)

action_frame = tk.Frame(window)
action_frame.pack(pady=12)

tk.Button(
    action_frame,
    text="Inspect Key",
    command=inspect_key
).grid(row=0, column=0, padx=5)

tk.Button(
    action_frame,
    text="Inspect Thread",
    command=inspect_thread
).grid(row=0, column=1, padx=5)

tk.Button(
    action_frame,
    text="Open Drawer",
    command=open_drawer
).grid(row=0, column=2, padx=5)

tk.Label(window, text="Inventory").pack()

inventory_box = tk.Listbox(window, width=40, height=6)
inventory_box.pack(pady=5)

update_inventory()

tk.Label(window, text="Who do you accuse?").pack(pady=(12, 2))

suspect_entry = tk.Entry(window, width=30)
suspect_entry.pack()

tk.Button(
    window,
    text="Make Final Guess",
    command=final_guess
).pack(pady=8)

tk.Button(
    window,
    text="Reset Game",
    command=reset_game
).pack()

window.mainloop()
