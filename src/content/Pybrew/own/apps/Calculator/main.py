import tkinter as tk
import math

# Funktion zur Berechnung des Ergebnisses
def berechne():
    try:
        # Berechnung des Ausdrucks
        ergebnis = eval(entry.get(), {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(ergebnis))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Fehler")

# Funktion zum Hinzufügen von Tasten in das Eingabefeld
def taste_drucke(taste):
    if taste == "=":
        berechne()
    elif taste == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, taste)

# Fenster erstellen
root = tk.Tk()
root.title("Fortgeschrittener Taschenrechner")

# Farben definieren
background_color = "#f0f0f0"
button_color = "#d0d0d0"
button_active_color = "#b0b0b0"
entry_color = "#ffffff"

# Eingabefeld
entry = tk.Entry(root, width=30, font=('Arial', 18), borderwidth=2, relief="solid", bg=entry_color, fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Funktion zum Erstellen von Knöpfen
def knopf_funktion():
    knöpfe = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]

    for index, knopf in enumerate(knöpfe):
        row = 1 + index // 4
        column = index % 4

        if knopf in ['=', 'C']:
            color = button_active_color
        else:
            color = button_color

        tk.Button(root, text=knopf, width=6, height=2, font=('Arial', 14),
                  bg=color, fg="black",
                  command=lambda t=knopf: taste_drucke(t)).grid(row=row, column=column, padx=5, pady=5)

# Hintergrundfarbe des Fensters
root.configure(bg=background_color)

# Knöpfe in das Fenster einfügen
knopf_funktion()

# Hauptloop starten
root.mainloop()
