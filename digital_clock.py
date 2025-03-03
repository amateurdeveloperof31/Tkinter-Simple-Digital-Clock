# ---------------------------------------------------Imports------------------------------------------------------------
from tkinter import *
from datetime import datetime
import pyglet

# --------------------------------------------------Main Class----------------------------------------------------------
class DigitalClock:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Digital Clock")
        width, height = 200, 50
        self.windows.minsize(width, height)
        self.windows.resizable(False, False)
        self.windows.config(bg="white")

        pyglet.options['win32_gdi_font'] = True
        pyglet.font.add_file('digital-7.ttf')

        self.canvas = Canvas(width=200, height=50, bg="white", highlightthickness=0)
        self.hour_text = self.canvas.create_text(40, 20, text="00", font=('digital-7', 16), fill='#fa0a2f')
        self.minute_text = self.canvas.create_text(80, 20, text="00", font=('digital-7', 16), fill='#0032ff')
        self.seconds_text = self.canvas.create_text(120, 20, text="00", font=('digital-7', 16), fill='#FF5733')
        self.ampm_text = self.canvas.create_text(160, 20, text="AM", font=('digital-7', 16), fill='#cc03bd')
        self.date_text = self.canvas.create_text(100, 40, text="Monday 01-01-2024", font=('digital-7', 10), fill='#333333')
        self.canvas.pack()

        self.update_clock()

        self.windows.mainloop()

# -------------------------------------------------Update Clock---------------------------------------------------------
    def update_clock(self):
        hour_now = datetime.now().strftime("%I")
        minute_now = datetime.now().strftime("%M")
        seconds_now = datetime.now().strftime("%S")
        ampm_now = datetime.now().strftime("%p")

        date_now = datetime.now().strftime("%A, %d-%B-%Y")

        self.canvas.itemconfig(self.hour_text, text=hour_now)
        self.canvas.itemconfig(self.minute_text, text=minute_now)
        self.canvas.itemconfig(self.seconds_text, text=seconds_now)
        self.canvas.itemconfig(self.ampm_text, text=ampm_now)

        self.canvas.itemconfig(self.date_text, text=date_now)

        self.windows.after(1000, lambda: self.update_clock())

# -----------------------------------------------Run the Program--------------------------------------------------------
DigitalClock()
