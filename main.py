import tkinter as tk
from database import create_db
from booking import open_booking_page
from reservation import open_reservations_page

# Initialize the database
create_db()

# Create main window
window = tk.Tk()
window.title("Flight Reservation System")
window.geometry("400x300")

# Welcome label
label = tk.Label(window, text="Welcome to Flight App ✈️", font=("Arial", 14))
label.pack(pady=20)

# Button to open booking form
book_btn = tk.Button(window, text="Book a Flight", width=20, command=open_booking_page)
book_btn.pack(pady=10)

# Button to view reservations
view_btn = tk.Button(window, text="View Reservations", width=20, command=open_reservations_page)
view_btn.pack(pady=10)

# Run the window
window.mainloop()
