from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

# dummy
def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title('Pharmacy Management SoftWare')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text='Pharmacy Management System', font=('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.LoginFrame1 = Frame(self.frame, width=1000, height=300, bd=20, relief='ridge')
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=1000, height=100, bd=20, relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)

        self.LoginFrame3 = Frame(self.frame, width=1000, height=200, bd=20, relief='ridge')
        self.LoginFrame3.grid(row=3, column=0, pady=2)

        # ==================================================================================================

        self.LabelUsername = Label(self.LoginFrame1, text='Username', font=('arial', 30, 'bold'), bd=20)
        self.LabelUsername.grid(row=0, column=0)
        self.TextUsername = Entry(self.LoginFrame1, font=('arial', 30, 'bold'), bd=20, textvariable=self.Username)
        self.TextUsername.grid(row=0, column=1)

        self.LabelPassword = Label(self.LoginFrame1, text='Password', font=('arial', 30, 'bold'), bd=20)
        self.LabelPassword.grid(row=1, column=0)
        self.TextPassword = Entry(self.LoginFrame1, font=('arial', 30, 'bold'), bd=20, textvariable=self.Password)
        self.TextPassword.grid(row=1, column=1)
        # ==================================================================================================

        self.Login = Button(self.LoginFrame2, text='Login', width=17, font=('arial', 20, 'bold'),
                            command=self.Logging_in)
        self.Login.grid(row=0, column=0)

        self.Reset = Button(self.LoginFrame2, text='Reset', width=17, font=('arial', 20, 'bold'),
                            command=self.Resetting)
        self.Reset.grid(row=0, column=1)

        self.Exit = Button(self.LoginFrame2, text='Exit', width=17, font=('arial', 20, 'bold'),
                           command=self.Exitting)
        self.Exit.grid(row=0, column=2)

        # ==================================================================================================

        self.patient_button = Button(self.LoginFrame3, text='Patient Registration', font=('arial', 20, 'bold'),
                                     state=DISABLED, command=self.Patient_window)
        self.patient_button.grid(row=0, column=0)

        self.hospital_button = Button(self.LoginFrame3, text='Hospital Registration', font=('arial', 20, 'bold'),
                                      state=DISABLED, command=self.Hospital_window)
        self.hospital_button.grid(row=0, column=1)

        # ==================================================================================================

    def Logging_in(self):
        user = (self.Username.get())
        pass_word = (self.Password.get())

        if user == str(12345) and pass_word == str(12345):
            self.patient_button.config(state=NORMAL)
            self.hospital_button.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno('Pharmacy Management System',
                                        'Invalid Credentials! Do you want to retry?')
            self.patient_button.config(state=DISABLED)
            self.hospital_button.config(state=DISABLED)
            self.Username.set('')
            self.Password.set('')
            self.TextUsername.focus()

    def Resetting(self):
        self.patient_button.config(state=DISABLED)
        self.hospital_button.config(state=DISABLED)
        self.Username.set('')
        self.Password.set('')
        self.TextUsername.focus()

    def Exitting(self):
        self.Exitting = tkinter.messagebox.askyesno('Pharmacy Management System', 'Do you want to exit?')
        if self.Exitting > 0:
            self.master.destroy()
            return

        # ==================================================================================================

    def Patient_window(self):
        self.new_window = Toplevel(self.master)
        self.app = Window2(self.new_window)

    def Hospital_window(self):
        self.new_window = Toplevel(self.master)
        self.app = Window3(self.new_window)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title('Patient Registration')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title('Hospital Management')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == '__main__':
    main()
