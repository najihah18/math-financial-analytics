import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import date, timedelta
from statistics import mean, stdev
from math import sqrt


# -------------------------
# API FUNCTIONS
# -------------------------

def get_latest_rate(from_currency, to_currency):
    url = (
        f"https://api.frankfurter.dev/v2/rate/"
        f"{from_currency}/{to_currency}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    return data["rate"]


def get_historical_rates(from_currency, to_currency, days=45):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    url = "https://api.frankfurter.dev/v2/rates"

    params = {
        "from": start_date.isoformat(),
        "to": end_date.isoformat(),
        "base": from_currency,
        "quotes": to_currency
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    rates = []

    for item in data:
        if item["quote"] == to_currency:
            rates.append({
                "date": item["date"],
                "rate": float(item["rate"])
            })

    rates.sort(key=lambda x: x["date"])

    return rates


# -------------------------
# CURRENCY CONVERSION
# -------------------------

def convert_currency():
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

    # Same currency
    if from_currency == to_currency:
        label_result.config(
            text=f"{amount:.2f} {from_currency} = "
                 f"{amount:.2f} {to_currency}"
        )
        return

    try:
        exchange_rate = get_latest_rate(
            from_currency,
            to_currency
        )

        result = amount * exchange_rate

        label_result.config(
            text=f"{amount:.2f} {from_currency} = "
                 f"{result:.2f} {to_currency}"
        )

    except requests.RequestException:
        messagebox.showerror(
            "Connection Problem",
            "Unable to connect to the exchange-rate service."
        )

    except (KeyError, ValueError):
        messagebox.showerror(
            "API Problem",
            "The exchange-rate data could not be read."
        )


# -------------------------
# MOVING AVERAGE
# -------------------------

def calculate_moving_average(rates, window=7):
    recent_rates = [
        item["rate"]
        for item in rates[-window:]
    ]

    return mean(recent_rates)


# -------------------------
# VOLATILITY
# -------------------------

def calculate_volatility(rates):
    values = [
        item["rate"]
        for item in rates
    ]

    daily_returns = []

    for i in range(1, len(values)):
        previous_rate = values[i - 1]
        current_rate = values[i]

        daily_return = (
            current_rate / previous_rate
        ) - 1

        daily_returns.append(daily_return)

    if len(daily_returns) < 2:
        return 0

    # Annualised volatility
    volatility = stdev(daily_returns) * sqrt(252)

    return volatility


# -------------------------
# SIMPLE LINEAR FORECAST
# -------------------------

def calculate_forecast(rates):
    values = [
        item["rate"]
        for item in rates
    ]

    n = len(values)

    if n < 2:
        return values[-1]

    x_values = list(range(n))

    x_mean = mean(x_values)
    y_mean = mean(values)

    numerator = 0
    denominator = 0

    for x, y in zip(x_values, values):
        numerator += (x - x_mean) * (y - y_mean)
        denominator += (x - x_mean) ** 2

    if denominator == 0:
        return values[-1]

    slope = numerator / denominator

    intercept = y_mean - (slope * x_mean)

    next_x = n

    forecast = intercept + (slope * next_x)

    return forecast


# -------------------------
# ANALYTICS
# -------------------------

def run_analytics():
    from_currency = combo_from.get().strip().upper()
    to_currency = combo_to.get().strip().upper()

    if not from_currency or not to_currency:
        messagebox.showerror(
            "Invalid Currency",
            "Please select both currencies."
        )
        return

    if from_currency == to_currency:
        messagebox.showerror(
            "Invalid Pair",
            "Please choose two different currencies."
        )
        return

    try:
        rates = get_historical_rates(
            from_currency,
            to_currency
        )

        if len(rates) < 2:
            messagebox.showerror(
                "Insufficient Data",
                "Not enough historical data was returned."
            )
            return

        # Moving average
        moving_average = calculate_moving_average(
            rates,
            window=7
        )

        # Volatility
        volatility = calculate_volatility(rates)

        # Forecast
        forecast = calculate_forecast(rates)

        latest_rate = rates[-1]["rate"]

        first_date = rates[0]["date"]
        last_date = rates[-1]["date"]

        analytics_text = (
            f"Pair: {from_currency}/{to_currency}\n"
            f"Data period: {first_date} → {last_date}\n"
            f"Observations: {len(rates)}\n\n"
            f"Latest Rate: {latest_rate:.6f}\n"
            f"7-Day Moving Average: {moving_average:.6f}\n"
            f"Annualised Volatility: {volatility * 100:.2f}%\n"
            f"Next-Rate Forecast: {forecast:.6f}"
        )

        label_analytics.config(
            text=analytics_text
        )

    except requests.RequestException:
        messagebox.showerror(
            "Connection Problem",
            "Unable to retrieve historical exchange-rate data."
        )

    except (KeyError, ValueError, TypeError):
        messagebox.showerror(
            "Data Problem",
            "The historical exchange-rate data could not be processed."
        )


# -------------------------
# GUI SETUP
# -------------------------

root = tk.Tk()

root.title("Currency Analytics Engine")
root.geometry("500x600")


# -------------------------
# TITLE
# -------------------------

label_title = tk.Label(
    root,
    text="Currency Analytics Engine",
    font=("Arial", 16, "bold")
)

label_title.pack(pady=20)


# -------------------------
# AMOUNT
# -------------------------

label_amount = tk.Label(
    root,
    text="Amount"
)

label_amount.pack()

entry_amount = tk.Entry(root)

entry_amount.pack(pady=5)


# -------------------------
# FROM CURRENCY
# -------------------------

label_from = tk.Label(
    root,
    text="From Currency"
)

label_from.pack(pady=(15, 5))

combo_from = ttk.Combobox(
    root,
    values=[
        "USD",
        "EUR",
        "GBP",
        "MYR",
        "JPY",
        "AUD",
        "SGD"
    ],
    state="readonly"
)

combo_from.pack()

combo_from.set("USD")


# -------------------------
# TO CURRENCY
# -------------------------

label_to = tk.Label(
    root,
    text="To Currency"
)

label_to.pack(pady=(15, 5))

combo_to = ttk.Combobox(
    root,
    values=[
        "USD",
        "EUR",
        "GBP",
        "MYR",
        "JPY",
        "AUD",
        "SGD"
    ],
    state="readonly"
)

combo_to.pack()

combo_to.set("MYR")


# -------------------------
# CONVERT BUTTON
# -------------------------

button_convert = tk.Button(
    root,
    text="Convert",
    command=convert_currency
)

button_convert.pack(pady=15)


# -------------------------
# CONVERSION RESULT
# -------------------------

label_result = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 12, "bold")
)

label_result.pack(pady=5)


# -------------------------
# ANALYTICS BUTTON
# -------------------------

button_analytics = tk.Button(
    root,
    text="Run 45-Day Analytics",
    command=run_analytics
)

button_analytics.pack(pady=15)


# -------------------------
# ANALYTICS RESULT
# -------------------------

label_analytics = tk.Label(
    root,
    text="Analytics will appear here",
    font=("Arial", 11),
    justify="left"
)

label_analytics.pack(pady=10)


# -------------------------
# START GUI
# -------------------------

root.mainloop()
