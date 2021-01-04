from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Combobox

# ***************** Set Up root ****************
root = Tk()
root.title("Currency Conversion")
root.configure(bg='#1d3557', padx=40, pady=40)
root.geometry("1000x500")
# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 3.5 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 3 - windowHeight / 2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

# ***************** Set Up Main Frame ****************
mainFrame = Frame(root)
mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
mainFrame['bg'] = mainFrame.master['bg']
# ***************** Set Up Labels ****************

titleLabel = Label(mainFrame, text="Currency Converter", font=('lato black', 26, 'bold'), fg='#e63946', padx=20,
                   pady=20)
fromLabel = Label(mainFrame, text="From: ", font=('lato black', 20, 'bold'), fg='#f1faee', padx=20, pady=10)
toLabel = Label(mainFrame, text="To: ", font=('lato black', 20, 'bold'), fg='#f1faee', padx=20, pady=10)
amountLabel = Label(mainFrame, text="Amount: ", font=('lato black', 20, 'bold'), fg='#f1faee', padx=20, pady=30)

titleLabel['bg'] = titleLabel.master['bg']
fromLabel['bg'] = fromLabel.master['bg']
toLabel['bg'] = toLabel.master['bg']
amountLabel['bg'] = amountLabel.master['bg']

titleLabel.grid(columnspan="2")
fromLabel.grid(row=1, column=0)
toLabel.grid(row=2, column=0)
amountLabel.grid(row=3, column=0)
# ***************** Set Up Drop Down Menus ****************
AllCurrencies=['USD', 'EGP', 'GBP', 'CAD']

fromValue = StringVar()
toValue = StringVar()

fromCurrency = Combobox(mainFrame, width=27, textvariable=fromValue, state="readonly")
toCurrency = Combobox(mainFrame, width=27, textvariable=toValue, state="readonly")
fromCurrency['values'] = AllCurrencies
toCurrency['values'] = AllCurrencies

fromCurrency.grid(sticky=E, row=1, column=1)
toCurrency.grid(sticky=E, row=2, column=1)


# ***************** Set Up Amount Field ********************

amountField = Entry(mainFrame, width=30)
amountField.grid(sticky=E, row=3, column=1)


def amountvalidate(value):
    if value.isdigit() or value == ".":
        return True

    elif value is "":
        return True

    else:
        return False


amountreg = mainFrame.register(amountvalidate)
amountField.config(validate="key", validatecommand=(amountreg, '%S'))
# ***************** Set Up Convert Button ********************

buttonFrame = Frame(mainFrame, padx=10)
buttonFrame['bg'] = buttonFrame.master['bg']
buttonFrame.grid(row=3, column=2)

resultLabel = Label(mainFrame, font=('lato black', 20, 'bold'), fg='#f1faee', padx=20, pady=10)
resultLabel.grid(row=4, columnspan="3")
resultLabel['bg'] = resultLabel.master['bg']

# ***************** Result Calculations ********************

def setupresult(result):
    resultLabel['text'] = result


def result():
    f = fromCurrency.get()
    t = toCurrency.get()
    if f == '' or t == '' or amountField.get() == "":
        tkinter.messagebox.showinfo('Warning', "Please fill the All the fields!")
    if f != "" and t != "" and f == t:
        tkinter.messagebox.showinfo('Warning', "Can't convert to the same currency!")
    if f == 'USD' and t == 'EGP' and amountField.get() != "":
        return setupresult(float(amountField.get()) * 15.73)
    if f == 'USD' and t == 'GBP'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 0.7408)
    if f == 'USD' and t == 'CAD'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 1.2811)

    if f == 'EGP' and t == 'USD'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 0.0636)
    if f == 'EGP' and t == 'GBP'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 0.0471)
    if f == 'EGP' and t == 'CAD'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 0.0814)

    if f == 'GBP' and t == 'USD'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 1.3498)
    if f == 'GBP' and t == 'EGP'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 21.2464)
    if f == 'GBP' and t == 'CAD'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 1.7297)

    if f == 'CAD' and t == 'USD'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 0.781)
    if f == 'CAD' and t == 'EGP'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 12.2851)
    if f == 'CAD' and t == 'GBP'and amountField.get() != "":
        return setupresult(float(amountField.get()) * 0.5782)


cnvButton = Button(buttonFrame, text="Convert..", command=result, padx=5, bg='#e63946', fg='white',
                   font=('lato black', 15, 'bold'))
cnvButton.pack()
# ***************** Run ********************


root.mainloop()
