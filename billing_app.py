from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime
from pdf_bill import generate_pdf_bill

def connect_db():
    return sqlite3.connect("bike_billing.db")

def generate_bill():
    try:
        name_en = entry_name_en.get()
        name_kn = entry_name_kn.get()
        phone = entry_phone.get()
        bike_no = entry_bike_no.get()
        bike_model = entry_bike_model.get()
        service_amt = float(entry_service.get())

        subtotal = service_amt
        gst = subtotal * 0.18
        total = subtotal + gst
        date = datetime.now().strftime("%d-%m-%Y")

        conn = connect_db()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO customers (name_en, name_kn, phone, bike_no, bike_model)
        VALUES (?, ?, ?, ?, ?)
        """, (name_en, name_kn, phone, bike_no, bike_model))

        customer_id = cur.lastrowid

        cur.execute("""
        INSERT INTO bills (customer_id, date, subtotal, gst, total)
        VALUES (?, ?, ?, ?, ?)
        """, (customer_id, date, subtotal, gst, total))

        bill_no = cur.lastrowid

        conn.commit()
        conn.close()

        generate_pdf_bill(
            bill_no, name_en, name_kn, phone,
            bike_no, bike_model, subtotal, gst, total
        )

        lbl_total.config(text=f"Total / ಒಟ್ಟು: ₹{total:.2f}")
        messagebox.showinfo("Success", "Bill Generated & PDF Created")

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("Bike Billing Software")
root.geometry("600x550")
root.resizable(False, False)

Label(root, text="Bike Billing Software / ಬೈಕ್ ಬಿಲ್ಲಿಂಗ್",
      font=("Arial", 16, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Customer Name (EN)").grid(row=0, column=0, sticky="w")
entry_name_en = Entry(frame, width=30)
entry_name_en.grid(row=0, column=1)

Label(frame, text="ಗ್ರಾಹಕರ ಹೆಸರು (KN)").grid(row=1, column=0, sticky="w")
entry_name_kn = Entry(frame, width=30)
entry_name_kn.grid(row=1, column=1)

Label(frame, text="Mobile Number").grid(row=2, column=0, sticky="w")
entry_phone = Entry(frame, width=30)
entry_phone.grid(row=2, column=1)

Label(frame, text="Bike Number").grid(row=3, column=0, sticky="w")
entry_bike_no = Entry(frame, width=30)
entry_bike_no.grid(row=3, column=1)

Label(frame, text="Bike Model").grid(row=4, column=0, sticky="w")
entry_bike_model = Entry(frame, width=30)
entry_bike_model.grid(row=4, column=1)

Label(frame, text="Service Amount ₹").grid(row=5, column=0, sticky="w")
entry_service = Entry(frame, width=30)
entry_service.grid(row=5, column=1)

Button(root, text="Generate Bill / ಬಿಲ್ ರಚಿಸಿ",
       font=("Arial", 12, "bold"),
       bg="green", fg="white",
       command=generate_bill).pack(pady=15)

lbl_total = Label(root, text="", font=("Arial", 14, "bold"))
lbl_total.pack()

root.mainloop()

