import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_edit_page(reservation):
    edit_window = tk.Toplevel()
    edit_window.title("Edit Reservation")
    edit_window.geometry("400x400")

    reservation_id, name, flight, departure, destination, date, seat = reservation

    # Fields with existing values
    tk.Label(edit_window, text="Name").pack()
    name_entry = tk.Entry(edit_window)
    name_entry.insert(0, name)
    name_entry.pack()

    tk.Label(edit_window, text="Flight Number").pack()
    flight_entry = tk.Entry(edit_window)
    flight_entry.insert(0, flight)
    flight_entry.pack()

    tk.Label(edit_window, text="Departure").pack()
    departure_entry = tk.Entry(edit_window)
    departure_entry.insert(0, departure)
    departure_entry.pack()

    tk.Label(edit_window, text="Destination").pack()
    destination_entry = tk.Entry(edit_window)
    destination_entry.insert(0, destination)
    destination_entry.pack()

    tk.Label(edit_window, text="Date").pack()
    date_entry = tk.Entry(edit_window)
    date_entry.insert(0, date)
    date_entry.pack()

    tk.Label(edit_window, text="Seat Number").pack()
    seat_entry = tk.Entry(edit_window)
    seat_entry.insert(0, seat)
    seat_entry.pack()

    # Update Button
    def update_reservation():
        updated_data = (
            name_entry.get(),
            flight_entry.get(),
            departure_entry.get(),
            destination_entry.get(),
            date_entry.get(),
            seat_entry.get(),
            reservation_id
        )

        conn = sqlite3.connect("flights.db")
        c = conn.cursor()
        c.execute('''
            UPDATE reservations
            SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
            WHERE id = ?
        ''', updated_data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Updated", "Reservation updated successfully.")
        edit_window.destroy()

    tk.Button(edit_window, text="Update", command=update_reservation).pack(pady=10)