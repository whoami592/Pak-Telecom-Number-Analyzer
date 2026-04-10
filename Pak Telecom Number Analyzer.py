# ========================================================
# Pak Telecom Number Analyzer
# Fully Functional GUI Application
# Coded by Mr. Sabaz Ali Khan
# ========================================================

import tkinter as tk
from tkinter import messagebox, ttk

# Complete and updated operator prefixes (as of 2026)
# These are the original allocation prefixes used by PTA.
# Note: Due to Mobile Number Portability (MNP), the actual current operator
# may differ, but this tool shows the original allocated operator.
OPERATORS = {
    # Jazz (including former Warid numbers)
    "0300": "Jazz", "0301": "Jazz", "0302": "Jazz", "0303": "Jazz", "0304": "Jazz",
    "0305": "Jazz", "0306": "Jazz", "0307": "Jazz", "0308": "Jazz", "0309": "Jazz",
    "0320": "Jazz", "0321": "Jazz", "0322": "Jazz", "0323": "Jazz", "0324": "Jazz",
    "0325": "Jazz", "0326": "Jazz", "0327": "Jazz", "0328": "Jazz", "0329": "Jazz",

    # Zong
    "0310": "Zong", "0311": "Zong", "0312": "Zong", "0313": "Zong", "0314": "Zong",
    "0315": "Zong", "0316": "Zong", "0317": "Zong", "0318": "Zong", "0319": "Zong",

    # Ufone
    "0330": "Ufone", "0331": "Ufone", "0332": "Ufone", "0333": "Ufone", "0334": "Ufone",
    "0335": "Ufone", "0336": "Ufone", "0337": "Ufone", "0338": "Ufone", "0339": "Ufone",

    # Telenor
    "0340": "Telenor", "0341": "Telenor", "0342": "Telenor", "0343": "Telenor", "0344": "Telenor",
    "0345": "Telenor", "0346": "Telenor", "0347": "Telenor", "0348": "Telenor", "0349": "Telenor",
}

def clean_number(raw_number):
    """Clean the input number and convert to standard 11-digit format"""
    # Remove everything except digits
    digits = ''.join(filter(str.isdigit, raw_number))
    
    # Handle different formats:
    # +923001234567  → 03001234567
    # 923001234567   → 03001234567
    # 03001234567    → remains same
    if len(digits) == 12 and digits.startswith("92"):
        cleaned = "0" + digits[2:]
    elif len(digits) == 13 and digits.startswith("092"):
        cleaned = digits[1:]
    elif len(digits) == 11 and digits.startswith("03"):
        cleaned = digits
    else:
        return None
    
    return cleaned if len(cleaned) == 11 and cleaned.startswith("03") else None

def analyze_number():
    """Main analysis function"""
    input_text = entry.get().strip()
    
    if not input_text:
        messagebox.showwarning("Empty Input", "Please enter a phone number!")
        return
    
    cleaned = clean_number(input_text)
    
    if not cleaned:
        messagebox.showerror("Invalid Number", 
            "Invalid Pakistani number!\n\n"
            "Valid formats:\n"
            "• 03001234567\n"
            "• +923001234567\n"
            "• 923001234567")
        return
    
    prefix = cleaned[:4]
    operator = OPERATORS.get(prefix, "Unknown / Other Operator")
    
    # Nice formatted display
    formatted = f"{cleaned[:4]}-{cleaned[4:7]}-{cleaned[7:]}"
    
    result = f"✅ Analysis Complete\n\n"
    result += f"Number     : {formatted}\n"
    result += f"Operator   : {operator}\n"
    result += f"Prefix     : {prefix}\n"
    result += f"Status     : Valid Pakistani Mobile Number\n"
    result += f"Length     : 11 digits\n"
    result += f"Note       : Original allocation by PTA\n"
    result += f"Portability: Actual current operator may differ due to MNP"
    
    # Update result box
    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state="disabled")

def clear_all():
    """Clear input and result"""
    entry.delete(0, tk.END)
    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.config(state="disabled")
    entry.focus()

# ====================== GUI SETUP ======================
root = tk.Tk()
root.title("Pak Telecom Number Analyzer")
root.geometry("720x620")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# Header
header_frame = tk.Frame(root, bg="#003087", height=80)
header_frame.pack(fill="x")
header_frame.pack_propagate(False)

tk.Label(header_frame, 
         text="🇵🇰 Pak Telecom Number Analyzer",
         font=("Arial", 22, "bold"),
         fg="white",
         bg="#003087").pack(pady=15)

tk.Label(header_frame, 
         text="Coded by Mr. Sabaz Ali Khan",
         font=("Arial", 11),
         fg="#ffcc00",
         bg="#003087").pack()

# Input Section
input_frame = tk.LabelFrame(root, text=" Enter Number ", font=("Arial", 12, "bold"), padx=15, pady=15, bg="#f0f4f8")
input_frame.pack(pady=20, padx=30, fill="x")

tk.Label(input_frame, text="Mobile Number:", font=("Arial", 11), bg="#f0f4f8").grid(row=0, column=0, sticky="w", pady=5)
entry = tk.Entry(input_frame, width=35, font=("Consolas", 14), justify="center", relief="solid", bd=2)
entry.grid(row=0, column=1, padx=10, pady=5)
entry.focus()

# Buttons
btn_frame = tk.Frame(input_frame, bg="#f0f4f8")
btn_frame.grid(row=1, column=0, columnspan=2, pady=15)

analyze_btn = tk.Button(btn_frame, text="🔍 Analyze Number", font=("Arial", 12, "bold"),
                        bg="#00aa00", fg="white", width=18, height=2, command=analyze_number)
analyze_btn.pack(side="left", padx=8)

clear_btn = tk.Button(btn_frame, text="🗑 Clear", font=("Arial", 12, "bold"),
                      bg="#cc0000", fg="white", width=12, height=2, command=clear_all)
clear_btn.pack(side="left", padx=8)

# Result Section
result_frame = tk.LabelFrame(root, text=" Analysis Result ", font=("Arial", 12, "bold"), padx=15, pady=10, bg="#f0f4f8")
result_frame.pack(pady=10, padx=30, fill="both", expand=True)

result_text = tk.Text(result_frame, height=14, font=("Consolas", 11), bg="#ffffff", fg="#003087",
                      relief="solid", bd=1, wrap="word")
result_text.pack(fill="both", expand=True, padx=5, pady=5)
result_text.config(state="disabled")

# Footer Information
footer_text = """Supported Operators:
Jazz (0300-0309, 0320-0329)  |  Zong (0310-0319)  |  Ufone (0330-0339)  |  Telenor (0340-0349)

This tool uses official PTA prefix allocation.
Due to Mobile Number Portability (MNP), the actual service provider may be different."""

footer = tk.Label(root, text=footer_text, font=("Arial", 9), fg="#555555", bg="#f0f4f8", justify="left")
footer.pack(pady=15, padx=30, anchor="w")

# Run the application
root.mainloop()