import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_booking_page():
    booking_window = tk.Toplevel()
    booking_window.title("Book a Flight")
    booking_window.geometry("400x400")

    # Form Labels and Entries
    tk.Label(booking_window, text="Name").pack()
    name_entry = tk.Entry(booking_window)
    name_entry.pack()

    tk.Label(booking_window, text="Flight Number").pack()
    flight_entry = tk.Entry(booking_window)
    flight_entry.pack()

    tk.Label(booking_window, text="Departure").pack()
    departure_entry = tk.Entry(booking_window)
    departure_entry.pack()

    tk.Label(booking_window, text="Destination").pack()
    destination_entry = tk.Entry(booking_window)
    destination_entry.pack()

    tk.Label(booking_window, text="Date").pack()
    date_entry = tk.Entry(booking_window)
    date_entry.pack()

    tk.Label(booking_window, text="Seat Number").pack()
    seat_entry = tk.Entry(booking_window)
    seat_entry.pack()

    # Save data to DB
    def book_flight():
        name = name_entry.get()
        flight = flight_entry.get()
        departure = departure_entry.get()
        destination = destination_entry.get()
        date = date_entry.get()
        seat = seat_entry.get()

        if name and flight and departure and destination and date and seat:
            conn = sqlite3.connect('flights.db')
            c = conn.cursor()
            c.execute("INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number) VALUES (?, ?, ?, ?, ?, ?)",
                      (name, flight, departure, destination, date, seat))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Flight booked successfully!")
            booking_window.destroy()
        else:
            messagebox.showwarning("Missing Info", "Please fill in all fields.")

    tk.Button(booking_window, text="Book Flight", command=book_flight).pack(pady=10)