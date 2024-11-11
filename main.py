import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("1000x450")
root.title("Money Map by Amokh")
root.iconbitmap(r"C:\Users\Dell\Desktop\MONEY MAP\icon-moneymap.ico")
root.configure(background="#2c3e50")
item_list=[]

# Add item function
def add_item():
    item = item_txt.get()
    qty = qty_txt.get()
    cost = cost_txt.get()
    total = int(qty) * int(cost)
    single_item_label = tk.Label(frame2, text=f"{item}\t\t{qty}\t\t{cost}\t\t{total}", bg="#2c3e50", fg="#ffffff", font="Helvetica 15 ")
    single_item_label.pack(pady=5)
    single_item = {"Item": item, "Quantity": qty, "Cost": cost, "Total Amount": total}
    item_list.append(single_item)

# Clear item function
def clear_item():
    item_txt.delete(0, "end")
    qty_txt.delete(0, "end")
    cost_txt.delete(0, "end")

# Analyse function
def analyse():
    df = pd.DataFrame(item_list)
    items = df['Item']
    total = df['Total Amount']
    fig = plt.figure(figsize=(10, 5))
    plt.bar(items, total, color='red', width=0.4)
    plt.ylabel("Cost of items")
    plt.xlabel("Items purchased")
    plt.title("Expenditure Tracker Analysis")

    plt.show()

title_label = tk.Label(root, text="Money Map", bg="#2c3e50", fg="#ffffff", font="Helvetica 20 bold")
title_label.pack(pady=30)

# For making "item"
item_label = tk.Label(root, text="Item", bg="#2c3e50", fg="#ffffff", font="Helvetica 15 bold")
item_label.pack(pady=(20, 5))

# For the content inside the first box
item_txt = tk.Entry(root, font="Helvetica 15 ")
item_txt.pack()

# For making "quantity"
qty_label = tk.Label(root, text="Quantity", bg="#2c3e50", fg="#ffffff", font="Helvetica 15 bold")
qty_label.pack(pady=(20, 5))

# For the content inside the second box
qty_txt = tk.Entry(root, font="Helvetica 15 ")
qty_txt.pack()

# For making "cost per unit"
cost_label = tk.Label(root, text="Cost per unit", bg="#2c3e50", fg="#ffffff", font="Helvetica 15 bold")
cost_label.pack(pady=(20, 5))

# For the content inside the third box
cost_txt = tk.Entry(root, font="Helvetica 15 ")
cost_txt.pack()

frame1 = tk.Frame(root, bg="#2c3e50")

# Add item button
add_button = tk.Button(frame1, text="Add item", bg="#2c3e50", fg="#ffffff", font="Helvetica 15 ", command=add_item)
add_button.pack(padx=10, pady=20, side=tk.LEFT)

# Clear button
clear_button = tk.Button(frame1, text="Clear", bg="#2c3e50", fg="#ffffff", font="Helvetica 15 ", command=clear_item)
clear_button.pack(padx=10, pady=20, side=tk.RIGHT)
frame1.pack()

# For making "Expense"
exp_label = tk.Label(root, text="Expense", bg="#2c3e50", fg="#ffffff", font="Helvetica 15 ")
exp_label.pack(pady=(30, 5))

# For making frame 2
frame2 = tk.Frame(root, bg="#2c3e50")

# For making "Item Quantity Unit Cost Total" which is in frame 2
heading_label = tk.Label(frame2, text="Item\t\tQuantity\t\tUnit Cost\t\tTotal", bg="#2c3e50", fg="#ffffff", font="Helvetica 15 ")
heading_label.pack(pady=(5))
frame2.pack()

# Analyse button
analyse_button = tk.Button(root, text="Analyse", bg="#E74C3C", fg="#000000", font="Helvetica 15 bold", command=analyse)
analyse_button.pack(pady=30)

root.mainloop()