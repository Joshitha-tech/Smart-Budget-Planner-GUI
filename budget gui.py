import tkinter as tk
from tkinter import messagebox, ttk

def calculate_budget():
    try:
        income = float(income_entry.get())
        expenses = float(expense_entry.get())
        savings = income - expenses
        
        # Calculate percentages
        if income > 0:
            expense_pct = (expenses / income) * 100
            savings_pct = (savings / income) * 100
        else:
            expense_pct = savings_pct = 0

        # Update output labels
        savings_val.config(text=f"₹{savings:,.2f}", fg="#2ecc71" if savings >= 0 else "#e74c3c")
        pct_val.config(text=f"Spent: {expense_pct:.1f}% | Saved: {savings_pct:.1f}%")
        
        # Financial Health Warning
        if expenses > income:
            messagebox.showwarning("Budget Alert", "Warning: Your expenses exceed your income!")
        elif savings_pct >= 30:
            messagebox.showinfo("Great Job!", "Excellent financial health! You are saving over 30% of your income.")
            
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Income and Expenses.")

# Main window setup
root = tk.Tk()
root.title("Smart Budget Planner")
root.geometry("450x400")
root.configure(bg="#2c3e50") # Dark elegant background

# Title Banner
title_label = tk.Label(root, text="PERSONAL BUDGET ANALYTICS", font=("Helvetica", 16, "bold"), bg="#34495e", fg="#ecf0f1", pady=10)
title_label.pack(fill=tk.X)

# Main Form Frame
frame = tk.Frame(root, bg="#2c3e50", padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# Input Fields
tk.Label(frame, text="Monthly Income (₹):", font=("Helvetica", 11), bg="#2c3e50", fg="#ecf0f1").grid(row=0, column=0, sticky="w", pady=10)
income_entry = tk.Entry(frame, font=("Helvetica", 11), width=20, bg="#ecf0f1")
income_entry.grid(row=0, column=1, pady=10, padx=10)

tk.Label(frame, text="Monthly Expenses (₹):", font=("Helvetica", 11), bg="#2c3e50", fg="#ecf0f1").grid(row=1, column=0, sticky="w", pady=10)
expense_entry = tk.Entry(frame, font=("Helvetica", 11), width=20, bg="#ecf0f1")
expense_entry.grid(row=1, column=1, pady=10, padx=10)

# Beautiful Calculate Button
calc_btn = tk.Button(frame, text="Analyze Budget", command=calculate_budget, font=("Helvetica", 11, "bold"), bg="#e67e22", fg="white", bd=0, padx=15, pady=5, activebackground="#d35400", activeforeground="white")
calc_btn.grid(row=2, column=0, columnspan=2, pady=20)

# Divider line
ttk.Separator(frame, orient='horizontal').grid(row=3, column=0, columnspan=2, sticky="ew", pady=10)

# Results Display
tk.Label(frame, text="Net Monthly Savings:", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1").grid(row=4, column=0, sticky="w", pady=5)
savings_val = tk.Label(frame, text="₹0.00", font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="#2ecc71")
savings_val.grid(row=4, column=1, sticky="w", pady=5, padx=10)

pct_val = tk.Label(frame, text="Spent: 0% | Saved: 0%", font=("Helvetica", 10, "italic"), bg="#2c3e50", fg="#bdc3c7")
pct_val.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop() 