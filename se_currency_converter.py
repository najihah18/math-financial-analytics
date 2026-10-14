import tkinter as tk
from tkinter import ttk, messagebox
import requests


def convert_currency():
    # Get user input
    amount_text = entry_amount.get().strip()
    from_currency = combo_from.get().strip().upper()
    to_currency = combo_to.get().strip().upper()

    # Check amount
    try:
        amount = float(amount_text)

        if amount < 0:
            messagebox.showerror(
                "Invalid Amount",
                "Please enter a positive amount."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Amount",
            "Please enter a valid number."
        )
        return

    # Check currency selection
    if not from_currency or not to_currency:
        messagebox.showerror(
            "Invalid Currency",
            "Please select both currencies."
        )
        return

    # No need to call the API if currencies are the same
    if from_currency == to_currency:
        label_result.config(
            text=f"{amount:.2f} {from_currency} = "
                 f"{amount:.2f} {to_currency}"
        )
        return

    try:
        # Get the latest exchange rates
        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            messagebox.showerror(
                "API Problem",
                "Unable to retrieve exchange rates."
            )
            return

        rates = data.get("rates", {})

        if to_currency not in rates:
            messagebox.showerror(
                "Currency Problem",
                f"Exchange rate for {to_currency} is unavailable."
            )
            return

        exchange_rate = rates[to_currency]

        # Basic currency conversion
        result = amount * exchange_rate

        label_result.config(
            text=f"{amount:.2f} {from_currency} = "
                 f"{result:.2f} {to_currency}"
        )

        # TODO: Add volatility forecasting in the next phase
        # TODO: Add moving average calculation in the next phase

    except requests.RequestException:
        messagebox.showerror(
            "Connection Problem",
            "Unable to connect to the exchange-rate service."
        )


# -------------------------
# GUI Setup
# -------------------------

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")


# Amount
label_amount = tk.Label(root, text="Amount")
label_amount.pack(pady=(20, 5))

entry_amount = tk.Entry(root)
entry_amount.pack()


# From currency
label_from = tk.Label(root, text="From Currency")
label_from.pack(pady=(15, 5))

combo_from = ttk.Combobox(
    root,
    values=["USD", "EUR", "GBP", "MYR", "JPY", "AUD", "SGD"],
    state="readonly"
)
combo_from.pack()
combo_from.set("USD")


# To currency
label_to = tk.Label(root, text="To Currency")
label_to.pack(pady=(15, 5))

combo_to = ttk.Combobox(
    root,
    values=["USD", "EUR", "GBP", "MYR", "JPY", "AUD", "SGD"],
    state="readonly"
)
combo_to.pack()
combo_to.set("MYR")


# Convert button
button_convert = tk.Button(
    root,
    text="Convert",
    command=convert_currency
)
button_convert.pack(pady=20)


# Result
label_result = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 12)
)
label_result.pack()


root.mainloop()
