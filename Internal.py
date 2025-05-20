import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import math
import json
import matplotlib.pyplot as plt

# ------------------ Utility Functions ------------------
def convert_to_scale(mark, out_of, scale):
    return (mark / out_of) * scale

def get_attendance_marks(attendance_percent):
    if attendance_percent >= 90:
        return 10.0
    elif attendance_percent >= 0:
        return round(attendance_percent / 10, 1)
    else:
        return 0

def reset_fields():
    for entry in entries:
        entry.delete(0, tk.END)
    attendance_slider.set(75)
    result_label.config(text="")

def update_attendance_label(value):
    attendance_value_label.config(text=f"{float(value):.0f}%")

def save_data():
    data = {
        "name": name_entry.get(),
        "test1": test1_entry.get(),
        "test1_total": test1_total_entry.get(),
        "test2": test2_entry.get(),
        "test2_total": test2_total_entry.get(),
        "assignment1": assign1_entry.get(),
        "assignment1_total": assign1_total_entry.get(),
        "assignment2": assign2_entry.get(),
        "assignment2_total": assign2_total_entry.get(),
        "attendance": attendance_slider.get()
    }
    filename = filedialog.asksaveasfilename(defaultextension=".json")
    if filename:
        with open(filename, "w") as f:
            json.dump(data, f)

def load_data():
    filename = filedialog.askopenfilename(filetypes=[["JSON files", "*.json"]])
    if filename:
        with open(filename, "r") as f:
            data = json.load(f)
        name_entry.delete(0, tk.END)
        name_entry.insert(0, data["name"])
        test1_entry.delete(0, tk.END)
        test1_entry.insert(0, data["test1"])
        test1_total_entry.delete(0, tk.END)
        test1_total_entry.insert(0, data["test1_total"])
        test2_entry.delete(0, tk.END)
        test2_entry.insert(0, data["test2"])
        test2_total_entry.delete(0, tk.END)
        test2_total_entry.insert(0, data["test2_total"])
        assign1_entry.delete(0, tk.END)
        assign1_entry.insert(0, data["assignment1"])
        assign1_total_entry.delete(0, tk.END)
        assign1_total_entry.insert(0, data["assignment1_total"])
        assign2_entry.delete(0, tk.END)
        assign2_entry.insert(0, data["assignment2"])
        assign2_total_entry.delete(0, tk.END)
        assign2_total_entry.insert(0, data["assignment2_total"])
        attendance_slider.set(data["attendance"])
        calculate_internal()

students_data = []

def export_graph():
    if not students_data:
        messagebox.showwarning("No Data", "No student records to plot.")
        return
    names = [s['name'] for s in students_data]
    marks = [s['mark'] for s in students_data]
    plt.figure(figsize=(8, 4))
    plt.bar(names, marks, color='cyan')
    plt.xlabel("Student Name")
    plt.ylabel("Internal Mark (/50)")
    plt.title("KTU Internal Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ------------------ Main Calculation Function ------------------
def calculate_internal(event=None):
    name = name_entry.get()
    try:
        t1 = float(test1_entry.get())
        t1_total = float(test1_total_entry.get())
        t2 = float(test2_entry.get())
        t2_total = float(test2_total_entry.get())
        assign1 = float(assign1_entry.get())
        assign1_total = float(assign1_total_entry.get())
        assign2 = float(assign2_entry.get())
        assign2_total = float(assign2_total_entry.get())
        attendance = float(attendance_slider.get())

        t1_scaled = convert_to_scale(t1, t1_total, 25)
        t2_scaled = convert_to_scale(t2, t2_total, 25)
        test_avg = (t1_scaled + t2_scaled) / 2
        assign1_scaled = convert_to_scale(assign1, assign1_total, 7.5)
        assign2_scaled = convert_to_scale(assign2, assign2_total, 7.5)
        assignment_total_scaled = assign1_scaled + assign2_scaled  # 15 marks total
        attendance_mark = get_attendance_marks(attendance)

        internal_total_real = test_avg + assignment_total_scaled + attendance_mark
        internal_total_rounded = round(internal_total_real)

        result_label.config(
            text=f"{name}'s Internal Mark: {internal_total_rounded}/50",
            fg="lightgreen"
        )

        students_data.append({"name": name, "mark": internal_total_rounded})

    except ValueError:
        result_label.config(text="❌ Please enter valid numbers.", fg="red")

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("KTU Internal Mark Calculator")
root.configure(bg="#121212")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#121212", foreground="white")
style.configure("TButton", background="#1f1f1f", foreground="white", relief="flat")
style.configure("TEntry", fieldbackground="#1f1f1f", foreground="white")

def label(text, r, c):
    ttk.Label(root, text=text).grid(row=r, column=c, padx=5, pady=5, sticky="w")

def entry(r, c):
    e = ttk.Entry(root)
    e.grid(row=r, column=c, padx=5, pady=5)
    entries.append(e)
    return e

entries = []

label("Student Name", 0, 0)
name_entry = entry(0, 1)

label("Test 1 Marks", 1, 0)
test1_entry = entry(1, 1)
label("Out of", 1, 2)
test1_total_entry = entry(1, 3)

label("Test 2 Marks", 2, 0)
test2_entry = entry(2, 1)
label("Out of", 2, 2)
test2_total_entry = entry(2, 3)

label("Assignment 1 Marks", 3, 0)
assign1_entry = entry(3, 1)
label("Out of", 3, 2)
assign1_total_entry = entry(3, 3)

label("Assignment 2 Marks", 4, 0)
assign2_entry = entry(4, 1)
label("Out of", 4, 2)
assign2_total_entry = entry(4, 3)

label("Attendance (%)", 5, 0)
attendance_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", bg="#121212", fg="white", highlightthickness=0, command=update_attendance_label)
attendance_slider.set(75)
attendance_slider.grid(row=5, column=1, columnspan=2, sticky="we")
attendance_value_label = ttk.Label(root, text="75%")
attendance_value_label.grid(row=5, column=3)

# Buttons
btn_frame = tk.Frame(root, bg="#121212")
btn_frame.grid(row=6, column=0, columnspan=4, pady=10)
tk.Button(btn_frame, text="Calculate", command=calculate_internal, bg="#2196F3", fg="white", padx=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Reset", command=reset_fields, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Save", command=save_data, bg="#4CAF50", fg="white").grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Load", command=load_data, bg="#9C27B0", fg="white").grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Graph", command=export_graph, bg="#FF9800", fg="white").grid(row=0, column=4, padx=5)

# Result Display
result_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="#121212", fg="lightgreen")
result_label.grid(row=7, column=0, columnspan=4, pady=10)

# Bind Enter Key
root.bind('<Return>', calculate_internal)

# Run
root.mainloop()
