import tkinter as tk
from tkinter import messagebox, ttk

def calculate():
    try:
        # Eingaben aus den Textfeldern erhalten
        revenue = float(entry_revenue.get())
        expenses = float(entry_expenses.get())
        tax_rate = float(entry_tax_rate.get())
        vat_rate = float(vat_rate_combobox.get())  # Umsatzsteuersatz aus Dropdown-Menü
        
        # Berechnungen
        vat_amount = revenue * (vat_rate / 100)  # Umsatzsteuerbetrag
        revenue_ex_vat = revenue - vat_amount  # Einnahmen ohne Umsatzsteuer
        profit_before_tax = revenue_ex_vat - expenses  # Gewinn vor Steuern
        tax = profit_before_tax * (tax_rate / 100)  # Steuerbetrag
        net_profit = profit_before_tax - tax  # Nettogewinn nach Steuern
        
        # Ergebnisse anzeigen
        result_text = (f"Einnahmen (inkl. MwSt.): {revenue:.2f} €\n"
                       f"Umsatzsteuerbetrag: {vat_amount:.2f} €\n"
                       f"Einnahmen (exkl. MwSt.): {revenue_ex_vat:.2f} €\n"
                       f"Ausgaben: {expenses:.2f} €\n"
                       f"Gewinn vor Steuern: {profit_before_tax:.2f} €\n"
                       f"Steuer: {tax:.2f} €\n"
                       f"Nettogewinn: {net_profit:.2f} €")
        label_result.config(text=result_text)
    except ValueError:
        messagebox.showerror("Eingabefehler", "Bitte geben Sie gültige Zahlenwerte ein.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Gewerbe-Rechner")

# Eingabefelder und Labels
tk.Label(root, text="Einnahmen (inkl. MwSt.) (€):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_revenue = tk.Entry(root)
entry_revenue.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Umsatzsteuersatz").grid(row=1, column=0, padx=10, pady=5, sticky="e")
vat_rate_combobox = ttk.Combobox(root, values=[7, 19, 0], state="readonly")  # Dropdown für MwSt. Sätze
vat_rate_combobox.set(19)  # Standardwert
vat_rate_combobox.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Ausgaben (€):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_expenses = tk.Entry(root)
entry_expenses.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Einkommenssteuersatz (%)").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_tax_rate = tk.Entry(root)
entry_tax_rate.grid(row=3, column=1, padx=10, pady=5)

# Berechnungs-Button
button_calculate = tk.Button(root, text="Berechnen", command=calculate)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Ergebnis-Label
label_result = tk.Label(root, text="", justify="left")
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Hauptloop starten
root.mainloop()
