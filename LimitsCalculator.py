import tkinter as tk
from tkinter import messagebox
import math

entry_x = entry_a = entry_mean = entry_std_dev = entry_k = entry_n = entry_p = entry_n_berry = entry_mean_berry = entry_std_dev_berry = entry_z_berry = entry_n_martingale = entry_m_martingale = entry_x_n_martingale = entry_m_value = None

def markov_inequality():
    try:
        x = float(entry_x.get())
        a = float(entry_a.get())
        if a > 0:
            probability = x / a
            result_label.config(text=f'P(X >= {a}) <= {probability:.4f}')
        else:
            messagebox.showerror('Error', 'A must be greater than 0.')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers.')

def chebyshev_inequality():
    try:
        mean = float(entry_mean.get())
        std_dev = float(entry_std_dev.get())
        k = float(entry_k.get())
        if std_dev > 0 and k > 0:
            probability = 1 - 1 / (k**2)
            result_label.config(text=f'P(|X - μ| >= {k}σ) <= {probability:.4f}')
        else:
            messagebox.showerror('Error', 'Standard Deviation and k must be greater than 0.')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers.')

def poisson_limit():
    try:
        n = int(entry_n.get())
        p = float(entry_p.get())
        lambda_val = n * p
        if n > 0 and 0 <= p <= 1:
            probability = math.exp(-lambda_val)
            result_label.config(text=f'P(X = 0) ≈ {probability:.4f}')
        else:
            messagebox.showerror('Error', 'n must be greater than 0 and p must be between 0 and 1.')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers.')

def berry_esseen_limit():
    try:
        n = int(entry_n_berry.get())
        mean = float(entry_mean_berry.get())
        std_dev = float(entry_std_dev_berry.get())
        z = float(entry_z_berry.get())
        
        if n > 0 and std_dev > 0:
            sqrt_n = math.sqrt(n)
            cdf_z = 0.5 * (1 + math.erf((z - mean) / (std_dev * sqrt_n)))
            abs_diff = abs(cdf_z - 0.5)
            probability = abs_diff * sqrt_n / std_dev
            result_label.config(text=f'|F_n(z) - Φ(z)| ≈ {probability:.4f}')
        else:
            messagebox.showerror('Error', 'n and Standard Deviation must be greater than 0.')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers.')

def martingale_central_limit_theorem():
    try:
        n = int(entry_n_martingale.get())
        m = int(entry_m_martingale.get())
        x_n = float(entry_x_n_martingale.get())
        m_value = float(entry_m_value.get())
        
        if n > 0 and m > 0:
            sqrt_n = math.sqrt(n)
            probability = math.erf((x_n - n * m_value) / (sqrt_n * math.sqrt(m_value * (1 - m_value))))
            result_label.config(text=f'P(S_n <= x_n) ≈ {probability:.4f}')
        else:
            messagebox.showerror('Error', 'n and m must be greater than 0.')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers.')

def open_markov_window():
    global entry_x, entry_a
    markov_window = tk.Toplevel(root)
    markov_window.title("Markov Inequality Calculator")
    
    label_x = tk.Label(markov_window, text="Enter X:", font=("Arial", 16))
    label_x.pack()
    
    entry_x = tk.Entry(markov_window, font=("Arial", 16))
    entry_x.pack()
    
    label_a = tk.Label(markov_window, text="Enter A:", font=("Arial", 16))
    label_a.pack()
    
    entry_a = tk.Entry(markov_window, font=("Arial", 16))
    entry_a.pack()
    
    calculate_markov_button = tk.Button(markov_window, text="Calculate Markov Inequality", command=markov_inequality, font=("Arial", 16), bg="green", fg="white")
    calculate_markov_button.pack()
    
    result_label = tk.Label(markov_window, text="", font=("Arial", 16))
    result_label.pack()

def open_chebyshev_window():
    global entry_mean, entry_std_dev, entry_k
    chebyshev_window = tk.Toplevel(root)
    chebyshev_window.title("Chebyshev Inequality Calculator")
    
    label_mean = tk.Label(chebyshev_window, text="Enter Mean (μ):", font=("Arial", 16))
    label_mean.pack()
    
    entry_mean = tk.Entry(chebyshev_window, font=("Arial", 16))
    entry_mean.pack()
    
    label_std_dev = tk.Label(chebyshev_window, text="Enter Standard Deviation (σ):", font=("Arial", 16))
    label_std_dev.pack()
    
    entry_std_dev = tk.Entry(chebyshev_window, font=("Arial", 16))
    entry_std_dev.pack()
    
    label_k = tk.Label(chebyshev_window, text="Enter k:", font=("Arial", 16))
    label_k.pack()
    
    entry_k = tk.Entry(chebyshev_window, font=("Arial", 16))
    entry_k.pack()
    
    calculate_chebyshev_button = tk.Button(chebyshev_window, text="Calculate Chebyshev Inequality", command=chebyshev_inequality, font=("Arial", 16), bg="blue", fg="white")
    calculate_chebyshev_button.pack()
    
    result_label = tk.Label(chebyshev_window, text="", font=("Arial", 16))
    result_label.pack()

def open_poisson_window():
    global entry_n, entry_p
    poisson_window = tk.Toplevel(root)
    poisson_window.title("Poisson Limit Calculator")
    
    label_n = tk.Label(poisson_window, text="Enter n:", font=("Arial", 16))
    label_n.pack()
    
    entry_n = tk.Entry(poisson_window, font=("Arial", 16))
    entry_n.pack()
    
    label_p = tk.Label(poisson_window, text="Enter p (0 <= p <= 1):", font=("Arial", 16))
    label_p.pack()
    
    entry_p = tk.Entry(poisson_window, font=("Arial", 16))
    entry_p.pack()
    
    calculate_poisson_button = tk.Button(poisson_window, text="Calculate Poisson Limit", command=poisson_limit, font=("Arial", 16), bg="orange", fg="black")
    calculate_poisson_button.pack()
    
    result_label = tk.Label(poisson_window, text="", font=("Arial", 16))
    result_label.pack()

def open_berry_window():
    global entry_n_berry, entry_mean_berry, entry_std_dev_berry, entry_z_berry
    berry_window = tk.Toplevel(root)
    berry_window.title("Berry-Esseen Limit Calculator")
    
    label_n_berry = tk.Label(berry_window, text="Enter n:", font=("Arial", 16))
    label_n_berry.pack()
    
    entry_n_berry = tk.Entry(berry_window, font=("Arial", 16))
    entry_n_berry.pack()
    
    label_mean_berry = tk.Label(berry_window, text="Enter Mean (μ):", font=("Arial", 16))
    label_mean_berry.pack()
    
    entry_mean_berry = tk.Entry(berry_window, font=("Arial", 16))
    entry_mean_berry.pack()
    
    label_std_dev_berry = tk.Label(berry_window, text="Enter Standard Deviation (σ):", font=("Arial", 16))
    label_std_dev_berry.pack()
    
    entry_std_dev_berry = tk.Entry(berry_window, font=("Arial", 16))
    entry_std_dev_berry.pack()
    
    label_z_berry = tk.Label(berry_window, text="Enter z:", font=("Arial", 16))
    label_z_berry.pack()
    
    entry_z_berry = tk.Entry(berry_window, font=("Arial", 16))
    entry_z_berry.pack()
    
    calculate_berry_button = tk.Button(berry_window, text="Calculate Berry-Esseen Limit", command=berry_esseen_limit, font=("Arial", 16), bg="purple", fg="white")
    calculate_berry_button.pack()
    
    result_label = tk.Label(berry_window, text="", font=("Arial", 16))
    result_label.pack()

def open_martingale_window():
    global entry_n_martingale, entry_m_martingale, entry_x_n_martingale, entry_m_value
    martingale_window = tk.Toplevel(root)
    martingale_window.title("Martingale Central Limit Theorem Calculator")
    
    label_n_martingale = tk.Label(martingale_window, text="Enter n:", font=("Arial", 16))
    label_n_martingale.pack()
    
    entry_n_martingale = tk.Entry(martingale_window, font=("Arial", 16))
    entry_n_martingale.pack()
    
    label_m_martingale = tk.Label(martingale_window, text="Enter m:", font=("Arial", 16))
    label_m_martingale.pack()
    
    entry_m_martingale = tk.Entry(martingale_window, font=("Arial", 16))
    entry_m_martingale.pack()
    
    label_x_n_martingale = tk.Label(martingale_window, text="Enter x_n:", font=("Arial", 16))
    label_x_n_martingale.pack()
    
    entry_x_n_martingale = tk.Entry(martingale_window, font=("Arial", 16))
    entry_x_n_martingale.pack()
    
    label_m_value = tk.Label(martingale_window, text="Enter M-value:", font=("Arial", 16))
    label_m_value.pack()
    
    entry_m_value = tk.Entry(martingale_window, font=("Arial", 16))
    entry_m_value.pack()
    
    calculate_martingale_button = tk.Button(martingale_window, text="Calculate Martingale CLT", command=martingale_central_limit_theorem, font=("Arial", 16), bg="red", fg="white")
    calculate_martingale_button.pack()
    
    result_label = tk.Label(martingale_window, text="", font=("Arial", 16))
    result_label.pack()

root = tk.Tk()
root.title("Probability Theorems Calculator")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

markov_button = tk.Button(frame, text="Calculate Markov Inequality", command=open_markov_window, font=("Arial", 16), bg="green", fg="white")
markov_button.pack(pady=10)

chebyshev_button = tk.Button(frame, text="Calculate Chebyshev Inequality", command=open_chebyshev_window, font=("Arial", 16), bg="blue", fg="white")
chebyshev_button.pack(pady=10)

poisson_button = tk.Button(frame, text="Calculate Poisson Limit", command=open_poisson_window, font=("Arial", 16), bg="orange", fg="black")
poisson_button.pack(pady=10)

berry_button = tk.Button(frame, text="Calculate Berry-Esseen Limit", command=open_berry_window, font=("Arial", 16), bg="purple", fg="white")
berry_button.pack(pady=10)

martingale_button = tk.Button(frame, text="Calculate Martingale CLT", command=open_martingale_window, font=("Arial", 16), bg="red", fg="white")
martingale_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 16))
result_label.pack()

root.mainloop()
