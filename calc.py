import tkinter as tk
import tkinter.messagebox

calc = tk.Tk()
calc.title('Calculator Using Python')
frame = tk.Frame(master=calc, bg="black", padx=10)
frame.pack()
entry = tk.Entry(master=frame, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def dbutton():
   calc.destroy()

def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Something went wrong", "Something went wrong")

def click(number):
	entry.insert(tk.END, number)

def clear():
	entry.delete(0, tk.END)

one = tk.Button(master=frame, text='1', width=5, command=lambda: click(1))
one.grid(row=1, column=0, pady=2)

two = tk.Button(master=frame, text='2', width=5, command=lambda: click(2))
two.grid(row=1, column=1, pady=2)

three = tk.Button(master=frame, text='3', width=5, command=lambda: click(3))
three.grid(row=1, column=2, pady=2)

four = tk.Button(master=frame, text='4',width=5, command=lambda: click(4))
four.grid(row=2, column=0, pady=2)

five = tk.Button(master=frame, text='5', width=5, command=lambda: click(5))
five.grid(row=2, column=1, pady=2)

six = tk.Button(master=frame, text='6', width=5, command=lambda: click(6))
six.grid(row=2, column=2, pady=2)

seven = tk.Button(master=frame, text='7', width=5, command=lambda: click(7))
seven.grid(row=3, column=0, pady=2)

eight = tk.Button(master=frame, text='8', width=5, command=lambda: click(8))
eight.grid(row=3, column=1, pady=2)

nine = tk.Button(master=frame, text='9', width=5, command=lambda: click(9))
nine.grid(row=3, column=2, pady=2)

zero = tk.Button(master=frame, text='0', width=5, command=lambda: click(0))
zero.grid(row=4, column=1, pady=2)

# zeroo = tk.Button(master=frame, text='00', width=5, command=lambda: click(00))
# zeroo.grid(row=6, column=2, pady=2)

add = tk.Button(master=frame, text="+", width=5, command=lambda: click('+'))
add.grid(row=4, column=0, pady=2)

sub = tk.Button(master=frame, text="-",  width=5, command=lambda: click('-'))
sub.grid(row=5, column=1, pady=2)

mult = tk.Button(master=frame, text="*",  width=5, command=lambda: click('*'))
mult.grid(row=4, column=2, pady=2)

div = tk.Button(master=frame, text="/",  width=5, command=lambda: click('/'))
div.grid(row=5, column=0, pady=2)

clear = tk.Button(master=frame, text="clear",width=15, command=clear)
clear.grid(row=6, column=0, columnspan=2, pady=2)

exit = tk.Button(master=frame, text="Exit",width=6, command=dbutton)
exit.grid(row=6, column=2, pady=2)

equal = tk.Button(master=frame, text="=",  width=5, command=equal)
#equal.grid(row=7, column=0, columnspan=3, pady=2)
equal.grid(row=5, column=2, pady=2)

calc.mainloop()
