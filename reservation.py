import tkinter as tk
from tkinter import messagebox
import sqlite3
from edit_reservation import open_edit_page  # We'll create this next

def open_reservations_page():
    reservations_window = tk.Toplevel()
    reservations_window.title("All Reservations")
    reservations_window.geometry("1000x500")

    # Table headers
    headers = ["ID", "Name", "Flight", "From", "To", "Date", "Seat", "Actions"]
    for i, header in enumerate(headers):
        tk.Label(reservations_window, text=header, font=('Arial', 10, 'bold')).grid(row=0, column=i, padx=5, pady=5)

    # Get data from DB
    conn = sqlite3.connect("flights.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reservations")
    rows = c.fetchall()
    conn.close()

    # Display data and action buttons
    for row_index, row in enumerate(rows, start=1):
        for col_index, item in enumerate(row):
            tk.Label(reservations_window, text=item).grid(row=row_index, column=col_index, padx=5, pady=5)

        # Edit button
        edit_btn = tk.Button(reservations_window, text="Edit", command=lambda r=row: open_edit_page(r))
        edit_btn.grid(row=row_index, column=7, padx=5)

        # Delete button
        delete_btn = tk.Button(reservations_window, text="Delete", command=lambda r=row: delete_reservation(r[0], reservations_window))
        delete_btn.grid(row=row_index, column=8, padx=5)

def delete_reservation(reservation_id, window):
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?")
    if confirm:
        conn = sqlite3.connect("flights.db")
        c = conn.cursor()
        c.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Reservation deleted successfully.")
        window.destroy()
        open_reservations_page()  # Reload updated table