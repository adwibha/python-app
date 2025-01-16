from tkinter import *
from tkinter import messagebox
import pyspeedtest

# Create the main application window
app = Tk()
app.title("Network Connection Checker")
app.config(background="blue")
app.geometry("500x500")

# Create a label for the application
label1 = Label(app, text="Internet speed checker", font=("Arial", 16), fg="white", bg="blue")
label1.pack(pady=20)

# Function to check internet speed
def check_speed():
    try:
        # Initialize SpeedTest
        speed = pyspeedtest.SpeedTest()
        
        # Perform download, upload, and ping tests
        download_speed = speed.download() / 1_000_000  # Convert to Mbps
        upload_speed = speed.upload() / 1_000_000      # Convert to Mbps
        ping = speed.ping()

        # Show results in a message box
        messagebox.showinfo("Speed Test Results", f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps\nPing: {ping} ms")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

# Create a button to trigger the speed test
check_button = Button(app, text="Check Speed", command=check_speed, font=("Arial", 14), bg="green", fg="white")
check_button.pack(pady=20)

# Run the application
app.mainloop()
