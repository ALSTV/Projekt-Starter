import os
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

# DEV Hauptordner Bei bedarf Ändern
DEV_PATH = Path("C:/DEV")


def get_project_path(name):
    if save_location.get() == "dev":
        return DEV_PATH / name
    return Path(name)


def html():
    name = entry.get().strip()

    if not name:
        messagebox.showerror("Fehler", "Bitte gib einen Projektnamen ein.")
        return

    root = get_project_path(name)

    try:
        (root / "css").mkdir(parents=True, exist_ok=True)
        (root / "js").mkdir(exist_ok=True)
        (root / "assets").mkdir(exist_ok=True)

        with open(root / "index.html", "w", encoding="utf-8") as f:
            f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>{name}</title>
    <link rel="stylesheet" href="./css/style.css">
</head>

<body>
    <h1>Hallo Welt!</h1>

    <script src="./js/script.js"></script>
</body>

</html>""")

        open(root / "css/style.css", "w").close()
        open(root / "js/script.js", "w").close()

        messagebox.showinfo(
            "Erfolg",
            f"Projekt wurde erstellt:\n{root}"
        )

    except Exception as e:
        messagebox.showerror("Fehler wir wissen selbst nicht woran es liegt", str(e))


def PY():
    name = entry.get().strip()

    if not name:
        messagebox.showerror("Fehler", "Bitte gib einen Projektnamen ein.")
        return

    root = get_project_path(name)

    try:
        root.mkdir(parents=True, exist_ok=True)

        with open(root / "main.py", "w", encoding="utf-8") as f:
            f.write("print('Hallo Welt')\n")

        with open(root / "gui.py", "w", encoding="utf-8") as f:
            f.write(f"""
import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("{name}")
root.geometry("1000x600")

bg = "#1e1e1e"
fg = "#ffffff"

root.config(bg=bg)

tk.Label(
    root,
    text="{name}",
    bg=bg,
    fg=fg,
    font=("Arial", 20)
).pack(pady=10)

root.mainloop()
""")

        messagebox.showinfo(
            "Erfolg",
            f"Projekt wurde erstellt:\n{root}"
        )

    except Exception as e:
        messagebox.showerror("Fehler", str(e))


# GUI
window = tk.Tk()
window.title("ALS_TV's Projekt Starter")
window.geometry("500x350")

bg = "#1e1e1e"
fg = "#ffffff"

window.config(bg=bg)

tk.Label(
    window,
    text="ALS_TV's Projektstarter",
    bg=bg,
    fg=fg,
    font=("Arial", 20)
).pack(pady=10)

tk.Label(
    window,
    text="Projektname:",
    bg=bg,
    fg=fg
).pack()

entry = tk.Entry(
    window,
    bg="#2a2a2a",
    fg=fg,
    width=24
)
entry.pack(pady=10)

btn = tk.Button(
    window,
    text="HTML Projekt erstellen",
    command=html,

    bg="#3b82f6",         
    fg="white",            

    activebackground="#2563eb",
    activeforeground="white",

    font=("Segoe UI", 9, "bold"),

    width=20,
    height=2,

    bd=0,             
    relief="flat",

    cursor="hand2"
)

btn.pack(pady=10)

btn = tk.Button(
    window,
    text="Python Projekt erstellen",
    command=PY,

    bg="#ff1919",       
    fg="white",           

    activebackground="#eb2525",
    activeforeground="white",

    font=("Segoe UI", 9, "bold"),

    width=20,
    height=2,

    bd=0,                
    relief="flat",

    cursor="hand2"
)

btn.pack(pady=10)

tk.Label(
    window,
    text="Speicherort:",
    bg=bg,
    fg=fg
).pack()

save_location = tk.StringVar(value="dev")

tk.Radiobutton(
    window,
    text="Im aktuellen Ordner",
    variable=save_location,
    value="current",
    bg=bg,
    fg=fg,
    selectcolor=bg
).pack()

tk.Radiobutton(
    window,
    text="DEV Ordner verwenden",
    variable=save_location,
    value="dev",
    bg=bg,
    fg=fg,
    selectcolor=bg
).pack()

window.mainloop()

