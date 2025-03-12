#Author - Arnav Arora
#Date - 26/08/24
#All versions of the code are uploaded on GitHub.

import tkinter as tk
from tkinter import ttk, messagebox
import random
import string


# List to store the user entries
user_entries = []

# Define a custom font
custom_font = ("Helvetica", "13")

# Define colors
dark_blue = '#0c67c2'
light_blue = '#9bbdde'
white = '#FFFFFF'

label_width = 20

# This is the home page of the program
def main_window():
    global main_window
    load_receipts()
    main_window = tk.Tk()
    main_window.title("Julie's Party Hire")
    main_window.configure(bg=dark_blue)

    main_frame = tk.Frame(main_window, bg=dark_blue)
    main_frame.pack(padx=20, pady=20)

    #Hire button
    hire_button = tk.Button(main_frame, text="Hire Item", command=hire_window, font=custom_font, bg=light_blue, fg=white, width=label_width)
    hire_button.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    #Return Button
    return_button = tk.Button(main_frame, text="Refund", command=refund_window, font=custom_font, bg=light_blue, fg=white, width=label_width)
    return_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

    #View Receipts Button
    view_receipts_button = tk.Button(main_frame, text="View Receipts", command=view_receipts_window, font=custom_font, bg=light_blue, fg=white, width=label_width)
    view_receipts_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

    #Quit Button
    quit_button = tk.Button(main_frame, text="Quit", command=confirm_quit, font=custom_font, bg=light_blue, fg=white, width=label_width)
    quit_button.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

    #Images 
    gif = tk.PhotoImage(file="parties.png")
    gif_resized = gif.subsample(2, 2)  
    label = tk.Label(main_frame, image=gif_resized, bg=dark_blue)
    label.image = gif_resized
    label.grid(row=0, column=0, columnspan=2, pady=10)

    main_window.mainloop()

# This is the Hire Window 
def hire_window():
    global receipt_label, first_name_entry, last_name_entry, item_combobox, quantity_spinbox

    # Hire Window Itself
    hire_window= tk.Toplevel()
    hire_window.title("Hire Window")
    hire_window.configure(bg=dark_blue)  

    # Hire Window Frame
    hire_frame = tk.LabelFrame(hire_window, text="Hire Item Details", bg=light_blue, font=custom_font)
    hire_frame.grid(row=0, column=0)

    # First & Last Name Input
    first_name_label = tk.Label(hire_frame, text="First Name", bg=light_blue, font=custom_font)
    first_name_label.grid(row=1, column=0, padx=20, pady=10)              
    first_name_entry = tk.Entry(hire_frame, font=custom_font, bg=white) 
    first_name_entry.grid(row=1, column=1, padx=20, pady=10)

    last_name_label = tk.Label(hire_frame, text="Last Name", bg=light_blue, font=custom_font)
    last_name_label.grid(row=2, column=0, padx=20, pady=10)
    last_name_entry = tk.Entry(hire_frame, font=custom_font, bg=white) 
    last_name_entry.grid(row=2, column=1)

    # Item Input
    item_label = tk.Label(hire_frame, text="Item", bg=light_blue, font=custom_font)
    item_combobox = ttk.Combobox(hire_frame, values=["Chairs", "Tables", "Candles", "Confetti"], font=custom_font)
    item_label.grid(row=3, column=0, padx=20, pady=10)
    item_combobox.grid(row=3, column=1, padx=20, pady=10)

    # Quantity Input
    quantity_label = tk.Label(hire_frame, text="Quantity", bg=light_blue, font=custom_font)
    quantity_spinbox = tk.Spinbox(hire_frame, from_=1, to=500, font=custom_font)
    quantity_label.grid(row=4, column=0, padx=20, pady=10)
    quantity_spinbox.grid(row=4, column=1, padx=20, pady=10)

    # Submit & Back Button
    validate_button = tk.Button(hire_frame, text="Submit", command=validate_input, bg=light_blue, font=custom_font, fg=white)
    validate_button.grid(row=5, column=1)

    back_button = tk.Button(hire_frame, text="Back to Main", command=hire_window.destroy, font=custom_font, bg=light_blue, fg=white)
    back_button.grid(row=5, column=0, padx=10, pady=5)

# Function to generate a random receipt number
def generate_receipt_number():
    #combines uppercase letters and numbers to form a 5 character receipt number
    receipt_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) 
    existing_receipt_numbers = [entry["receipt_number"] for entry in user_entries]
    while receipt_number in existing_receipt_numbers:
        receipt_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return receipt_number

# Function to check the length
def check_length(name):
    return len(name) <= 20

# Function to check the presence
def check_presence(name):
    return name != ""

# Function to check if the input contains only alphabets
def check_text(name):
    return name.isalpha()

# Function to check if quantity is between 1 and 500
def check_quantity(quantity):
    try:
        qty = int(quantity)
        return 1 <= qty <= 500
    except ValueError:
        return False

#Function to check special characters in refund receipt number field 
def is_alphanumeric(text):
        for char in text:
            if not (char.isalpha() or char.isdigit()):
                return False
        return True



# Function to validate the input
def validate_input():
    def print_receipt(receipt_number, first_name, last_name, item, quantity):
        view_receipt = tk.Toplevel()
        view_receipt.title("Receipt")
        view_receipt.configure(bg=dark_blue)

        receipt_frame = tk.LabelFrame(view_receipt, text="Receipt", bg=light_blue, fg=white, font=('Helvetica', 14, 'bold'))
        receipt_frame.grid(row=0, column=0, padx=20, pady=10)

        tk.Label(receipt_frame, text=f"Receipt Number: {receipt_number}", bg=light_blue, fg=white).pack(pady=5)
        tk.Label(receipt_frame, text=f"First Name: {first_name}", bg=light_blue, fg=white).pack(pady=5)
        tk.Label(receipt_frame, text=f"Last Name: {last_name}", bg=light_blue, fg=white).pack(pady=5)
        tk.Label(receipt_frame, text=f"Item: {item}", bg=light_blue, fg=white).pack(pady=5)
        tk.Label(receipt_frame, text=f"Quantity: {quantity}", bg=light_blue, fg=white).pack(pady=5)

    # Get the input values
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    item = item_combobox.get().strip()
    quantity = quantity_spinbox.get().strip()
    receipt_number = generate_receipt_number()

    # Debugging 
    print(f"Debug: First Name: '{first_name}'")
    print(f"Debug: Last Name: '{last_name}'")
    print(f"Debug: Item: '{item}'")
    print(f"Debug: Quantity: '{quantity}'")

    # Validation
    errors = []
    if not check_presence(first_name):
        errors.append("First name cannot be blank.")
    elif not check_length(first_name):
        errors.append("First name must be shorter than 20 characters.")
    elif not check_text(first_name):
        errors.append("First name cannot contain numbers or special characters and must contain only alphabets.")
    if not check_presence(last_name):
        errors.append("Last name cannot be blank.")
    elif not check_length(last_name):
        errors.append("Last name must be shorter than 20 characters.")
    elif not check_text(last_name):
        errors.append("Last name cannot contain numbers or special characters and must contain only alphabets.")
    if not check_presence(item):
        errors.append("Item cannot be blank.")
    elif item not in ["Chairs", "Tables", "Candles", "Confetti"]:
        errors.append("Item must be from the list provided.")
    if not check_quantity(quantity):
        errors.append("Quantity must be a number between 1 and 500.")

    if errors:
        messagebox.showerror("Error in Input", "\n".join(errors))
    else:
        # Append the entry to user_entries and write to file
        entry = {
            "first_name": first_name,
            "last_name": last_name,
            "item": item,
            "receipt_number": receipt_number,
            "quantity": quantity
        }
        user_entries.append(entry)
        with open("user_entries.txt", "a") as file:
            file.write(f"{first_name},{last_name},{item},{receipt_number},{quantity}\n")

        response = messagebox.askyesno("Entry Complete", f"Entry is stored with Receipt Number: {receipt_number}. Do you want to return to the main window?")
        if response:
            print_receipt(receipt_number, first_name, last_name, item, quantity)
        else:
            exit()



# This is the Refund Window
def refund_window():
    global refund_first_name_entry, refund_last_name_entry, refund_receipt_entry, refund_quantity_label, refund_quantity_spinbox, view_receipt_listbox

    refund = tk.Toplevel()
    refund.title("Refund Window")
    refund.configure(bg=dark_blue) 

    refund_frame = tk.LabelFrame(refund, text="Refund Details", bg=light_blue, font=custom_font)
    refund_frame.grid(row=0, column=0)

    refund_first_name_label = tk.Label(refund_frame, text="First Name", bg=light_blue, font=custom_font)
    refund_first_name_label.grid(row=1, column=0, padx=20, pady=10)
    refund_first_name_entry = tk.Entry(refund_frame, font=custom_font, bg=white)
    refund_first_name_entry.grid(row=1, column=1, padx=20, pady=10)

    refund_last_name_label = tk.Label(refund_frame, text="Last Name", bg=light_blue, font=custom_font)
    refund_last_name_label.grid(row=2, column=0, padx=20, pady=10)
    refund_last_name_entry = tk.Entry(refund_frame, font=custom_font, bg=white)
    refund_last_name_entry.grid(row=2, column=1, padx=20, pady=10)

    refund_quantity_label = tk.Label(refund_frame, text="Quantity", bg=light_blue, font=custom_font)
    refund_quantity_spinbox = tk.Spinbox(refund_frame, from_=1, to=500, font=custom_font)
    refund_quantity_label.grid(row=3, column=0, padx=20, pady=10)
    refund_quantity_spinbox.grid(row=3, column=1, padx=20, pady=10)

    refund_receipt_label = tk.Label(refund_frame, text="Receipt Number", bg=light_blue, font=custom_font)
    refund_receipt_label.grid(row=4, column=0, padx=20, pady=10)
    refund_receipt_entry = tk.Entry(refund_frame, font=custom_font, bg=white)
    refund_receipt_entry.grid(row=4, column=1, padx=20, pady=10)

    refund_button = tk.Button(refund_frame, text="Submit", command=process_refund, font=custom_font, bg=light_blue, fg=white)
    refund_button.grid(row=5, column=1)

    back_button = tk.Button(refund_frame, text="Back to Main", command=refund.destroy, font=custom_font, bg=light_blue, fg=white)
    back_button.grid(row=5, column=0, padx=10, pady=5)

    

# Function to validate refund input
def validate_refund_input(first_name, last_name, receipt_number, refund_quantity):
    errors = []

    if not check_presence(first_name):
        errors.append("First name cannot be blank.")
    elif not check_length(first_name):
        errors.append("First name must be shorter than 20 characters.")
    elif not check_text(first_name):
        errors.append("First name cannot contain numbers or special characters and must contain only alphabets.")

    if not check_presence(last_name):
        errors.append("Last name cannot be blank.")
    elif not check_length(last_name):
        errors.append("Last name must be shorter than 20 characters.")
    elif not check_text(last_name):
        errors.append("Last name cannot contain numbers or special characters and must contain only alphabets.")

    if not check_presence(receipt_number):
        errors.append("Receipt number cannot be blank.")
    elif not is_alphanumeric(receipt_number):
        errors.append("Receipt number cannot contain special characters. It can only have letters and digits between 1-9.")
    
    if not check_quantity(refund_quantity):
        errors.append("Quantity must be a number between 1 and 500.")

    return errors


# Function to process the refund
def process_refund():
    first_name = refund_first_name_entry.get().strip()
    last_name = refund_last_name_entry.get().strip()
    receipt_number = refund_receipt_entry.get().strip()
    refund_quantity = refund_quantity_spinbox.get().strip()

    errors = validate_refund_input(first_name, last_name, receipt_number, refund_quantity)
    if errors:
        messagebox.showerror("Error in Input", "\n".join(errors))
        return

    refund_quantity = int(refund_quantity)  # Convert to integer only after validation

    for entry in user_entries:
        if entry["receipt_number"] == receipt_number and entry["first_name"] == first_name and entry["last_name"] == last_name:
            current_quantity = int(entry["quantity"])
            if refund_quantity >= current_quantity:
                user_entries.remove(entry)
            else:
                entry["quantity"] = str(current_quantity - refund_quantity)
            with open("user_entries.txt", "w") as file:
                for entry in user_entries:
                    file.write(f"{entry['first_name']},{entry['last_name']},{entry['item']},{entry['receipt_number']},{entry['quantity']}\n")
            messagebox.showinfo("Refund Processed", f"Refund processed for Receipt Number: {receipt_number}")
            return

    messagebox.showerror("Refund Error", "No matching receipt found for the provided details you provided.")



def load_receipts():
    global user_entries
    try:
        with open("user_entries.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                parts = line.split(",")
                if len(parts) != 5:  # Check if there are exactly 5 parts
                    print(f"Skipping malformed line: {line}")
                    continue
                
                first_name, last_name, item, receipt_number, quantity = parts
                user_entries.append({
                    "first_name": first_name,
                    "last_name": last_name,
                    "item": item,
                    "receipt_number": receipt_number,
                    "quantity": quantity
                })
    except FileNotFoundError:
        print("File not found. No receipts to load.")


#This is the view receipts window
def view_receipts_window():
    view_receipts = tk.Toplevel()
    view_receipts.title("View Receipts")
    view_receipts.configure(bg=dark_blue) 

    view_frame = tk.Frame(view_receipts, bg=dark_blue)
    view_frame.pack(padx=20, pady=20)

    listbox_frame = tk.Frame(view_frame, bg=light_blue)
    listbox_frame.pack()

    if user_entries:
        for entry in user_entries:
            receipt_info = (f"Receipt Number: {entry['receipt_number']} - Name: {entry['first_name']} {entry['last_name']} "
                            f"- Item: {entry['item']} - Quantity: {entry['quantity']}")
            tk.Label(view_frame, text=receipt_info, bg=dark_blue, fg=white, font=custom_font).pack(pady=5)
    else:
        tk.Label(view_frame, text="No receipts available", bg=dark_blue, fg=white, font=custom_font).pack(pady=5)

    back_button = tk.Button(view_frame, text="Back to Main", command=view_receipts.destroy, font=custom_font, bg=light_blue, fg=white)
    back_button.pack(pady=10)

    try:
        with open("user_entries.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                return
            for line in lines:
                line = line.strip()
                if line:  # Check if line is not empty
                    parts = line.split(",")
                    if len(parts) == 5:  # Ensure there are exactly 5 parts
                        first_name, last_name, item, receipt_number, quantity = parts
                        receipt_display = (f"Receipt Number: {receipt_number} | Name: {first_name} {last_name} "
                                           f"| Item: {item} | Quantity: {quantity}")
                    else:
                        view_receipts_listbox.insert(tk.END, f"Incorrect line: {line}")
    except FileNotFoundError:
        view_receipts_listbox.insert(tk.END, "Receipts file not found.")

# Function to confirm quit
def confirm_quit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        main_window.destroy()

# Start the main window
if __name__ == "__main__":
    main_window()



