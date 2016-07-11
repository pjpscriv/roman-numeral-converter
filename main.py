"""GUI for converting Arabic numbers to Roman Numerals
   Author: Peter J Scriven
   Started: 2015 sometime?
   Updated: 11th July 2016
   """

import logic
import tkinter as tk
import tkinter.ttk as ttk


class NumeralConverterGUI(object):
    
    def __init__(self, root):
        self.root = root
        self.number_to_numeral = True
        
        # Window Settings
        root.minsize(350, 200)
        root.title("Roman Numeral Converter")
        root.iconbitmap("icon.ico")
        root.bind('<Return>', self.convert)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Mainframe
        self.main = tk.Frame(self.root, bg="")
        self.main.columnconfigure(0, weight=0, minsize=30)
        self.main.columnconfigure(1, weight=1)
        self.main.columnconfigure(2, weight=0, minsize=30)
        self.main.rowconfigure(0, weight=0)
        self.main.rowconfigure(1, weight=1)
        self.main.rowconfigure(2, weight=1)
        self.main.grid(sticky="nsew")
        
        # TITLE
        self.t_var = tk.StringVar()
        self.t_var.set("Number to Numeral")
        self.t_frame = tk.Frame(self.main, borderwidth=5, bg="")
        self.t_frame.rowconfigure(0, weight=1)
        self.t_frame.columnconfigure(0, weight=1)
        self.t_frame.grid(row=0, column=1, sticky="nsew")
        self.title = ttk.Label(self.t_frame, textvariable=self.t_var, background="")
        self.title.grid()

        # SWITCH BUTTON
        self.photo = ARROWS
        self.switch = ttk.Button(self.main, image=ARROWS, command=self.switch)
        self.switch.grid(row=0, column=2)
        # rollover text?
        
        # TEXTBOX / BUTTON
        self.input_var = tk.StringVar()
        self.e_frame = tk.Frame(self.main, borderwidth=10, bg="")
        self.e_frame.columnconfigure(0, weight=1)
        self.e_frame.rowconfigure(0, weight=0)
        self.e_frame.rowconfigure(1, weight=0)
        self.e_frame.grid(row=1, column=1, sticky="ew", padx=10, pady=0)
        self.entry = ttk.Entry(self.e_frame, justify="center", width=20, textvariable=self.input_var)
        self.entry.grid(pady=10)
        self.button = ttk.Button(self.e_frame, text="Convert", command=self.convert)
        self.button.grid(row=1)
        
        # OUTPUT LABEL
        self.o_var = tk.StringVar()
        self.o_frame = tk.Frame(self.main, borderwidth=5, bg="")
        self.o_frame.columnconfigure(0, weight=1)
        self.o_frame.rowconfigure(0, weight=1)
        self.o_frame.grid(row=2, column=1, sticky="nsew")
        self.output = ttk.Label(self.o_frame, textvariable=self.o_var, justify="center", background="")
        self.output.grid()
                
    def convert(self, event=None):
        text_in = self.input_var.get()
        text_out = ""
        if self.number_to_numeral:
            if logic.is_valid_number(text_in):
                text_out = logic.number_to_numeral(int(text_in))
            else:
                text_out = "Invalid Number Input"
        else:
            text_in = text_in.upper()
            if logic.is_valid_numeral(text_in):
                number_out = logic.numeral_to_number(text_in)
                numeral_out = logic.number_to_numeral(number_out)
                if text_in == numeral_out:
                    text_out = number_out
                else:
                    text_out = "The value of the numeral you entered is:\n" + \
                                str(number_out) + "\n" + \
                                "However it is incorrect. You entered:\n" + \
                                text_in + "\n" + \
                                "The correct numeral is:\n" + \
                                numeral_out
            else:
                text_out = "Invalid Numeral Input"

        self.input_var.set("")
        self.o_var.set(text_out)

    def switch(self):
        if self.number_to_numeral:
            self.number_to_numeral = False
            self.t_var.set("Numeral to Number")
        else:
            self.number_to_numeral = True
            self.t_var.set("Number to Numeral")


window = tk.Tk()
ARROWS = tk.PhotoImage(file="switch.png").subsample(2, 2)
NumeralConverterGUI(window)
window.mainloop()
