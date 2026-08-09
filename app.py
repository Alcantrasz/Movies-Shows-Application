import tkinter as tk
from tkinter import ttk, messagebox

from media import Media
import database



# Create database if it doesn't already exist
database.create_database()



# Window
root = tk.Tk()
root.title("Movie & Show Tracker")
root.geometry("900x600")
root.resizable(False, False)



# Variables
selected_id = None

type_var = tk.StringVar(value="Movie")
genre_var = tk.StringVar(value="Action")
rating_var = tk.IntVar(value=5)
search_var = tk.StringVar()



# Functions
def clear_fields():
    """Reset all input fields."""
    global selected_id

    selected_id = None

    type_var.set("Movie")
    genre_var.set("Action")
    rating_var.set(5)

    name_entry.delete(0, tk.END)


def load_tree(records=None):
    """Load records into the Treeview."""

    for item in tree.get_children():
        tree.delete(item)

    if records is None:
        records = database.get_all_media()

    for record in records:
        tree.insert("", tk.END, values=record)


def add_media():
    """Add a new Movie or Show."""

    try:
        media = Media(
            type_var.get(),
            name_entry.get(),
            genre_var.get(),
            rating_var.get()
        )

        database.add_media(media)

        load_tree()

        clear_fields()

        messagebox.showinfo("Success", "Entry added!")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def delete_media():
    """Delete the selected entry."""

    global selected_id

    if selected_id is None:
        messagebox.showwarning(
            "Nothing Selected",
            "Please select a record."
        )
        return

    database.delete_media(selected_id)

    load_tree()

    clear_fields()


def update_media():
    """Update the selected entry."""

    global selected_id

    if selected_id is None:
        messagebox.showwarning(
            "Nothing Selected",
            "Select a record first."
        )
        return

    try:

        media = Media(
            type_var.get(),
            name_entry.get(),
            genre_var.get(),
            rating_var.get()
        )

        database.update_media(selected_id, media)

        load_tree()

        clear_fields()

        messagebox.showinfo(
            "Updated",
            "Entry updated successfully."
        )

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def search_media(*args):
    """Search while typing."""

    text = search_var.get().strip()

    if text == "":
        load_tree()
    else:
        load_tree(database.search_media(text))


def on_select(event):
    """Load selected row into the form."""

    global selected_id

    selected = tree.focus()

    if not selected:
        return

    values = tree.item(selected)["values"]

    selected_id = values[0]

    type_var.set(values[1])

    name_entry.delete(0, tk.END)
    name_entry.insert(0, values[2])

    genre_var.set(values[3])

    rating_var.set(values[4])


search_var.trace_add("write", search_media)



# Form Frame
form = tk.Frame(root, padx=10, pady=10)
form.pack(fill="x")


tk.Label(
    form,
    text="Type"
).grid(row=0, column=0, sticky="w")

type_box = ttk.Combobox(
    form,
    textvariable=type_var,
    values=["Movie", "Show"],
    state="readonly",
    width=18
)

type_box.grid(row=1, column=0, padx=5)


tk.Label(
    form,
    text="Name"
).grid(row=0, column=1, sticky="w")

name_entry = tk.Entry(
    form,
    width=35
)

name_entry.grid(row=1, column=1, padx=5)


tk.Label(
    form,
    text="Genre"
).grid(row=0, column=2, sticky="w")

genre_box = ttk.Combobox(
    form,
    textvariable=genre_var,
    values=Media.ALLOWED_GENRES,
    state="readonly",
    width=18
)

genre_box.grid(row=1, column=2, padx=5)


tk.Label(
    form,
    text="Rating"
).grid(row=0, column=3, sticky="w")

rating_box = ttk.Combobox(
    form,
    textvariable=rating_var,
    values=[1, 2, 3, 4, 5],
    state="readonly",
    width=5
)

rating_box.grid(row=1, column=3, padx=5)



# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add",
    width=12,
    command=add_media
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update",
    width=12,
    command=update_media
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    width=12,
    command=delete_media
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_fields
).grid(row=0, column=3, padx=5)



# Search
search_frame = tk.Frame(root)
search_frame.pack(fill="x", padx=10)

tk.Label(
    search_frame,
    text="Search:"
).pack(side="left")

search_entry = tk.Entry(
    search_frame,
    textvariable=search_var,
    width=40
)

search_entry.pack(side="left", padx=10)


# Treeview
tree_frame = tk.Frame(root)
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(tree_frame)
scrollbar.pack(side="right", fill="y")

tree = ttk.Treeview(
    tree_frame,
    columns=("ID", "Type", "Name", "Genre", "Rating"),
    show="headings",
    yscrollcommand=scrollbar.set,
    selectmode="browse"
)

scrollbar.config(command=tree.yview)

tree.heading("ID", text="ID")
tree.heading("Type", text="Type")
tree.heading("Name", text="Name")
tree.heading("Genre", text="Genre")
tree.heading("Rating", text="Rating")

tree.column("ID", width=50, anchor="center")
tree.column("Type", width=100, anchor="center")
tree.column("Name", width=320)
tree.column("Genre", width=150, anchor="center")
tree.column("Rating", width=80, anchor="center")

tree.pack(fill="both", expand=True)

# Double-click a row to load it into the form
tree.bind("<Double-1>", on_select)


# Right-click menu (optional but nice)
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Delete", command=delete_media)
menu.add_command(label="Clear Form", command=clear_fields)


def show_menu(event):
    row = tree.identify_row(event.y)

    if row:
        tree.selection_set(row)
        tree.focus(row)
        on_select(None)

        menu.tk_popup(event.x_root, event.y_root)


tree.bind("<Button-3>", show_menu)


# Keyboard shortcuts
root.bind("<Delete>", lambda event: delete_media())
root.bind("<Escape>", lambda event: clear_fields())


def save_with_enter(event):
    if selected_id is None:
        add_media()
    else:
        update_media()


root.bind("<Return>", save_with_enter)


# Status Bar
status = tk.StringVar()


def update_status():
    count = len(database.get_all_media())
    status.set(f"{count} item(s) in database")


status_bar = tk.Label(
    root,
    textvariable=status,
    bd=1,
    relief=tk.SUNKEN,
    anchor="w"
)

status_bar.pack(fill="x", side="bottom")


# Override load_tree so it updates the status bar too
_old_load_tree = load_tree


def load_tree(records=None):
    _old_load_tree(records)
    update_status()



# Initial Load
load_tree()
clear_fields()


# Run Application
root.mainloop()