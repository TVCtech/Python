import tkinter as tk
from tkinter import ttk
# Start coding here

class LabelInput(tk.Frame):
    """A widget containing a label and input together."""

    def __init__(self, parent, label='', input_class=ttk.Entry,    
                input_var=None, input_args=None, label_args=None, **kwargs):


        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = input_var

        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["text"] = label
            input_args["variable"] = input_var
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
            input_args["textvariable"] = input_var

        self.input = input_class(self, **input_args)
        self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        super().grid(sticky=sticky, **kwargs)

    def get(self):
            try:
                if self.variable:
                    return self.variable.get()
                elif type(self.input) == tk.Text:
                    return self.input.get('1.0', tk.END)
                else:
                    return self.input.get()
            except (TypeError, tk.TclError):
                # happens when numeric fields are empty.
                return ''


    def set(self, value, *args, **kwargs):
        if type(self.variable) == tk.BooleanVar:
                self.variable.set(bool(value))
        elif self.variable:
                self.variable.set(value, *args, **kwargs)
        elif type(self.input) in (ttk.Checkbutton, ttk.Radiobutton):
            if value:
                self.input.select()
            else:
                self.input.deselect()
        elif type(self.input) == tk.Text:
            self.input.delete('1.0', tk.END)
            self.input.insert('1.0', value)
        else:
            self.input.delete(0, tk.END)
            self.input.insert(0, value)



class DataRecordForm(tk.Frame):
    """The input form for our widgets"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # A dict to keep track of input widgets
        self.inputs = {}
        self.reset()

        recordinfo = tk.LabelFrame(self, text="Record Information")

        self.inputs['Date'] = LabelInput(
            recordinfo, "Date",
            input_var=tk.StringVar()
            )
        self.inputs['Date'].grid(row=0, column=0)

        self.inputs['Time'] = LabelInput(recordinfo, "Time",
        input_class=ttk.Combobox, 
        input_var=tk.StringVar(),
        input_args={"values": ["8:00", "12:00", "16:00", "20:00"]}
        )

        self.inputs['Time'].grid(row=0, column=1)

        self.inputs['Technician'] = LabelInput(recordinfo,"Technician",
        input_var=tk.StringVar()
        )
        self.inputs['Technician'].grid(row=0, column=2)


        #line 2
        self.inputs['Lab'] = LabelInput(recordinfo, "Lab",
        input_class=ttk.Combobox, input_var=tk.StringVar(),
        input_args={"values": ["A", "B", "C", "D", "E"]})
        self.inputs['Lab'].grid(row=1, column=0)

        self.inputs['Plot'] = LabelInput(recordinfo, "Plot",
        input_class=ttk.Combobox, input_var=tk.IntVar(),
        input_args={"values": list(range(1, 21))})
        self.inputs['Plot'].grid(row=1, column=1)

        self.inputs['Seed sample'] = LabelInput(
        recordinfo, "Seed sample", input_var=tk.StringVar())
        self.inputs['Seed sample'].grid(row=1, column=2)

        recordinfo.grid(row=0, column=0, sticky=tk.W + tk.E)

        #Environment Data

        environmentinfo = tk.LabelFrame(self, text="Environment Data")

        self.inputs['Humidity'] = LabelInput(
        environmentinfo, "Humidity (g/m³)",
        input_class=tk.Spinbox, input_var=tk.DoubleVar(),
        input_args={"from_": 0.5, "to": 52.0, "increment": .01})

        self.inputs['Humidity'].grid(row=0, column=0)


        self.inputs['Equipment Fault'] = LabelInput(
        environmentinfo, "Equipment Fault",
        input_class=ttk.Checkbutton,
        input_var=tk.BooleanVar())
        self.inputs['Equipment Fault'].grid(
        row=1, column=0, columnspan=3)

#plant info
        plantinfo = tk.LabelFrame(self, text="Plant Data")

        self.inputs['Plants'] = LabelInput(
        plantinfo, "Plants",
        input_class=tk.Spinbox,
        input_var=tk.IntVar(),
        input_args={"from_": 0, "to": 20}
        )
        self.inputs['Plants'].grid(row=0, column=0)

        self.inputs['Blossoms'] = LabelInput(
        plantinfo, "Blossoms",
        input_class=tk.Spinbox,
        input_var=tk.IntVar(),
        input_args={"from_": 0, "to": 1000}
        )
        self.inputs['Blossoms'].grid(row=0, column=1)

        
        self.inputs['Fruit'] = LabelInput(
        plantinfo, "Fruit",
        input_class=tk.Spinbox,
        input_var=tk.IntVar(),
        input_args={"from_": 0, "to": 20}
        )
        self.inputs['Fruit'].grid(row=0, column=2)


        self.inputs['Height'].grid(row=0, column=0)
        self.inputs['Height'] = LabelInput(
        plantinfo, "Height",
        input_class=tk.Spinbox,
        input_var=tk.IntVar(),
        input_args={"from_": 0, "to": 1000}
        )
        self.inputs['Blossoms'].grid(row=0, column=1)

        #Notes section
        self.inputs['Notes'] = LabelInput(
        self, "Notes",
        input_class=tk.Text,
        input_args={"width": 75, "height": 10}
        ) 
        self.inputs['Notes'].grid(sticky="w", row=3, column=0)

    def get(self):
        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
            return data

    def reset(self):
        for widget in self.inputs.values():
            widget.set('')




class Application(tk.Tk):
    """Application root window"""




#page 108




if __name__ == "__main__":
    app = Application()
    app.mainloop()