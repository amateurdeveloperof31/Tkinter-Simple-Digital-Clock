# ---------------------------------------------------Imports------------------------------------------------------------
from tkinter import *
from datetime import datetime
import pyglet

# --------------------------------------------------Settings------------------------------------------------------------
width =200  # Window Width
height = 50  # Window Height
font = 'digital-7.ttf'  # Custom Font File
main_background = 'white'
hour_color = '#fa0a2f'
minute_color = '#0032ff'
seconds_color = '#FF5733'
ampm_color = '#cc03bd'
date_color = '#333333'

# --------------------------------------------------Main Class----------------------------------------------------------
class DigitalClock:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Digital Clock")
        self.windows.minsize(width, height)
        self.windows.resizable(False, False)
        self.windows.config(bg="white")

        pyglet.options['win32_gdi_font'] = True
        pyglet.font.add_file(font)

        self.canvas = Canvas(self.windows, width=200, height=50, bg=main_background, highlightthickness=0)
        self.canvas.pack()

        self.hour_text = self.canvas.create_text(40, 20, text="00", font=('digital-7', 16), fill=hour_color)
        self.minute_text = self.canvas.create_text(80, 20, text="00", font=('digital-7', 16), fill=minute_color)
        self.seconds_text = self.canvas.create_text(120, 20, text="00", font=('digital-7', 16), fill=seconds_color)
        self.ampm_text = self.canvas.create_text(160, 20, text="AM", font=('digital-7', 16), fill=ampm_color)
        self.date_text = self.canvas.create_text(100, 40, text="Monday 01-01-2024", font=('digital-7', 10),
                                                 fill=date_color)

        self.update_clock()

        self.windows.mainloop()

# -------------------------------------------------Update Clock---------------------------------------------------------
    def update_clock(self):
        time_now = datetime.now()

        self.canvas.itemconfig(self.hour_text, text=time_now.strftime("%I"))
        self.canvas.itemconfig(self.minute_text, text=time_now.strftime("%M"))
        self.canvas.itemconfig(self.seconds_text, text=time_now.strftime("%S"))
        self.canvas.itemconfig(self.ampm_text, text=time_now.strftime("%p"))
        self.canvas.itemconfig(self.date_text, text=time_now.strftime("%A, %d-%B-%Y"))

        self.windows.after(1000, self.update_clock)

# -----------------------------------------------Run the Program--------------------------------------------------------
DigitalClock()
