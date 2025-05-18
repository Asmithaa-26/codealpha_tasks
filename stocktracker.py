import tkinter as tk
from tkinter import messagebox, ttk
import requests

API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'  # Replace with your API key
BASE_URL = 'https://www.alphavantage.co/query'

portfolio = {}


def get_stock_price(symbol):
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    try:
        price = float(data['Global Quote']['05. price'])
        return price
    except KeyError:
        return None


def add_stock():
    symbol = symbol_entry.get().upper()
    try:
        shares = int(shares_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shares must be a number.")
        return

    price = get_stock_price(symbol)
    if price:
        portfolio[symbol] = {'shares': shares, 'price': price}
        update_portfolio()
        symbol_entry.delete(0, tk.END)
        shares_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", f"Could not fetch price for {symbol}.")


def remove_stock():
    selected = tree.selection()
    if selected:
        for item in selected:
            symbol = tree.item(item, 'text')
            portfolio.pop(symbol, None)
        update_portfolio()
    else:
        messagebox.showinfo("Select Item", "Please select a stock to remove.")


def update_portfolio():
    for item in tree.get_children():
        tree.delete(item)

    total_value = 0
    for symbol, data in portfolio.items():
        current_price = get_stock_price(symbol)
        if current_price:
            value = current_price * data['shares']
            tree.insert('', 'end', text=symbol,
                        values=(data['shares'], f"${current_price:.2f}", f"${value:.2f}"))
            total_value += value

    total_label.config(text=f"Total Portfolio Value: ${total_value:.2f}")


# GUI Setup
root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Stock Symbol:").grid(row=0, column=0, padx=5)
symbol_entry = tk.Entry(frame)
symbol_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Shares:").grid(row=0, column=2, padx=5)
shares_entry = tk.Entry(frame)
shares_entry.grid(row=0, column=3, padx=5)

tk.Button(frame, text="Add Stock", command=add_stock).grid(row=0, column=4, padx=5)
tk.Button(frame, text="Remove Stock", command=remove_stock).grid(row=0, column=5, padx=5)

tree = ttk.Treeview(root, columns=("Shares", "Current Price", "Total Value"), show='headings')
tree.heading("Shares", text="Shares")
tree.heading("Current Price", text="Current Price")
tree.heading("Total Value", text="Total Value")
tree.pack(pady=10, fill="x")

total_label = tk.Label(root, text="Total Portfolio Value: $0.00", font=("Arial", 14))
total_label.pack(pady=10)

root.mainloop()
