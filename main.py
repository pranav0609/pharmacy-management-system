import MySQLdb
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time

connection = MySQLdb.connect(host='localhost', user='root', password='shubham1701')
cursor = connection.cursor()


# dummy
def main():
    string = "use pythondb"
    cursor.execute(string)
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
        self.TextPassword = Entry(self.LoginFrame1, show="*", font=('arial', 30, 'bold'), bd=20, textvariable=self.Password)
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

        string = 'select username from users where username="%s"'
        arg1 = (user,)
        cursor.execute(string % arg1)
        checker1 = cursor.fetchone()
        if checker1 is not None:
            # checking whether the password for the username is valid or not
            string = 'select pass_word from users where username="%s"'
            arg2 = (user,)
            cursor.execute(string % arg2)
            checker2 = cursor.fetchone()
            if checker2[0] == pass_word:
                self.patient_button.config(state=NORMAL)
                self.hospital_button.config(state=NORMAL)
            else:
                tkinter.messagebox.askyesno('Pharmacy Management System',
                                            'Invalid Password! Do you want to retry?')
                self.patient_button.config(state=DISABLED)
                self.hospital_button.config(state=DISABLED)
                self.Username.set('')
                self.Password.set('')
                self.TextUsername.focus()
        else:
            tkinter.messagebox.askyesno('Pharmacy Management System',
                                        'Invalid Username! Do you want to retry?')
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

        # _____________________________________________________________________________________________________________
        DateOfOrder = StringVar()
        DateOfOrder.set(time.strftime("%d/%m/%Y"))
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        amount = StringVar()
        var4 = IntVar()

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        med_quantity = StringVar()
        telephone = StringVar()
        Ref = StringVar()

        adhar = StringVar()
        adhar.set("")

        # ===============Functions==================
        def iExit():
            iExit = tkinter.messagebox.askyesno("registration window", "are you sure to exit?")
            if iExit > 0:
                self.master.destroy()
                return

        def Reset():
            Firstname.set("")
            # Surname.set("")
            Address.set("")
            med_quantity.set("")
            telephone.set("")
            Ref.set("")
            adhar.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboMedicince.current(0)
            # self.cboTypeOfMember.current(0)
            self.cboMethodofPayment.current(0)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("registration window",
                                                          "do you want to reset all registered users to 0 too?")
            if iResetRecord <= 0:
                Reset()
            elif iResetRecord > 0:
                Reset()
                # self.txtReceipt.config(state=NORMAL)
                self.txtReceipt.delete("1.0", END)
                return

        def Ref_no_Generator():
            x = random.randint(10903, 68921)
            random_Ref = str(x)
            Ref.set(random_Ref)

        def Record_Add():
            # Ref_no_Generator()
            patient_id = Ref.get()
            patient_name = Firstname.get()
            patient_address = Address.get()
            patient_tele = telephone.get()
            quantity = med_quantity.get()
            medicine = var1.get()
            adhaar_number = adhar.get()
            if (
                    patient_id == "" or patient_name == "" or patient_address == "" or patient_tele == "" or quantity == "" or adhaar_number == ""):
                tkinter.messagebox.showinfo("inert status", "all fields are not filled")
            else:

                self.txtReceipt.insert(END, "\t" + Ref.get() + "\t\t" + Firstname.get() + "\t\t" + telephone.get()
                                       + "\t\t" + DateOfOrder.get() + "\t\t" + "\t" + var1.get() + "\t\t" + med_quantity.get() + "\n")
                string = "insert into patients(patient_name, patient_id, adhaar_number," \
                         "patient_address, patient_phno, medicine, quantity ) " \
                         "values('%s','%s', '%s', '%s', '%s', '%s', '%s')"
                args = (patient_name, patient_id, adhaar_number, patient_address, patient_tele, medicine,
                        quantity)
                cursor.execute(string % args)
                connection.commit()
                ChangeLot(medicine)
                tkinter.messagebox.showinfo("insert status", "patient inserted successfully")
                cursor.close()

        def Price():
            if var4.get() == 1:

                quan = int(med_quantity.get())
                self.txtAmount.configure(state=NORMAL)
                if var1.get() == "Paracetamol":
                    item1 = int(50 * quan)
                    amount.set("$" + str(item1))
                elif var1.get() == "Penicillin":
                    item1 = int(40 * quan)
                    amount.set("$" + str(item1))
                elif var1.get() == "Cod liver oil Tabs":
                    item1 = int(30 * quan)
                    amount.set("$" + str(item1))
                elif var1.get() == "Benadryl":
                    item1 = int(20 * quan)
                    amount.set("$" + str(item1))
            elif var4.get() == 0:
                self.txtAmount.configure(state=DISABLED)
                amount.set("0")

        def ChangeLot(medicine_name):
            string = 'select medicine_units from medicines where medicine_name = "%s"'
            args = (medicine_name,)
            cursor.execute(string % args)
            med_units = cursor.fetchone()
            temp_lot1 = int(med_units[0])
            temp_quantity = int(med_quantity.get())
            temp_lot2 = int(temp_lot1 - temp_quantity)
            string = 'update medicines set medicine_units = "%s" where medicine_name = "%s"'
            args = (temp_lot2, medicine_name)
            cursor.execute(string % args)
            connection.commit()
            return

        # =========================Frames=========================

        MainFrame = Frame(self.master)
        MainFrame.grid()

        Ttileframe = Frame(MainFrame, bd=20, width=1350, padx=26, relief=RIDGE)
        Ttileframe.pack(side=TOP)

        self.lblTtile = Label(Ttileframe, font=('arial', 50, 'bold'), text="Patient Reciept Window", padx=2)
        self.lblTtile.grid()

        # ===================Lower frames ====================
        MemberDeatilsFrame = LabelFrame(MainFrame, bd=20, width=1350, height=500, pady=5, relief=RIDGE)
        MemberDeatilsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDeatilsFrame, width=880, bd=10, height=400, relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, width=350, height=450, font=('arial', 20, 'bold'),
                                   text="Customer Name ", relief=RIDGE)
        MembersName_F.grid(row=0, column=0)

        ReceiptButtomFrame = LabelFrame(MemberDeatilsFrame, bd=10, width=1000, height=450, relief=RIDGE)
        ReceiptButtomFrame.pack(side=RIGHT)

        # ===============================================
        self.lblReferenceNo = Label(MembersName_F, font=('arial', 14, 'bold'), text="Reference no", bd=7)
        self.lblReferenceNo.grid(row=0, column=0)
        self.txtReferenceNo = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=Ref, insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblFirstName = Label(MembersName_F, font=('arial', 14, 'bold'), text="Name", bd=7)
        self.lblFirstName.grid(row=1, column=0)
        self.txtFirstName = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=Firstname,
                                  insertwidth=2)
        self.txtFirstName.grid(row=1, column=1)

        # self.lblLastName = Label(MembersName_F, font=('arial', 14, 'bold'), text="Username", bd = 7)
        # self.lblLastName.grid(row=2, column=0)
        # self.txtLastName = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=Surname,
        #  insertwidth=2)
        # self.txtLastName.grid(row=2, column=1)

        self.lblQuantity = Label(MembersName_F, font=('arial', 14, 'bold'), text="Quantity", bd=7)
        self.lblQuantity.grid(row=7, column=0)
        self.txtQuantity = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=med_quantity,
                                 insertwidth=2)
        self.txtQuantity.grid(row=7, column=1)

        self.lblAddress = Label(MembersName_F, font=('arial', 14, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=2, column=0)
        self.txtAddress = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=Address,
                                insertwidth=2)
        self.txtAddress.grid(row=2, column=1)

        self.lblTele = Label(MembersName_F, font=('arial', 14, 'bold'), text="Telephone No", bd=7)
        self.lblTele.grid(row=3, column=0)
        self.txtTele = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=telephone,
                             insertwidth=2)
        self.txtTele.grid(row=3, column=1)

        self.lblAdhar = Label(MembersName_F, font=('arial', 14, 'bold'), text="Adhar no", bd=7)
        self.lblAdhar.grid(row=4, column=0)
        self.txtAdhar = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=adhar,
                              insertwidth=2)
        self.txtAdhar.grid(row=4, column=1)

        self.lblDate = Label(MembersName_F, font=('arial', 14, 'bold'), text="Date", bd=7)
        self.lblDate.grid(row=5, column=0)
        self.txtDate = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=DateOfOrder,
                             insertwidth=2)
        self.txtDate.grid(row=5, column=1)

        # ===============================================

        # ===================Member info================
        self.lblMedicine = Label(MembersName_F, font=('arial', 14, 'bold'), text="Medicine", bd=7)
        self.lblMedicine.grid(row=6, column=0)

        self.cboMedicince = ttk.Combobox(MembersName_F, textvariable=var1, state='readonly', font=('arial', 14, 'bold'),
                                         width=19)
        self.cboMedicince['value'] = ('', 'Paracetamol', 'Penicillin', 'Cod liver oil Tabs', 'Benadryl')
        self.cboMedicince.current(0)
        self.cboMedicince.grid(row=6, column=1)
        self.chkAmount = Checkbutton(MembersName_F, text="Refresh Amount", font=('arial', 14, 'bold'), variable=var4,
                                     onvalue=1, offvalue=0, command=Price).grid(row=8, column=0)
        # self.lblAmount = Label(MembersName_F, font=('arial', 14, 'bold'), text="Total Amount", bd = 7)
        # self.lblAmount.grid(row=8, column=1)
        self.txtAmount = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=amount, bd=7,
                               insertwidth=2)
        self.txtAmount.grid(row=8, column=1)

        self.lblMethodOfpayment = Label(MembersName_F, font=('arial', 14, 'bold'), text="Payment method", bd=7)
        self.lblMethodOfpayment.grid(row=9, column=0)

        self.cboMethodofPayment = ttk.Combobox(MembersName_F, textvariable=var3, state='readonly',
                                               font=('arial', 14, 'bold'), width=19)
        self.cboMethodofPayment['value'] = ('', 'Cash', 'Credit card', 'Debit  card', 'UPI wallets')
        self.cboMethodofPayment.current(0)
        self.cboMethodofPayment.grid(row=9, column=1)

        # ==============Receipt=====================
        self.lblLabel = Label(ReceiptButtomFrame, font=('arial', 10, 'bold'), pady=10,
                              text='Patient ID\t Patient Name \t Telephone \t Date of Registration \t Medicine \t Quantity',
                              bd=7
                              )
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(ReceiptButtomFrame, width=112, height=22, font=('arial', 10, 'bold'))
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        # ===================Buttons=================
        self.btnReceipt = Button(ReceiptButtomFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13,
                                 text='Add', command=Record_Add).grid(row=2, column=0)
        self.btnReset = Button(ReceiptButtomFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13,
                               text='Reset', command=iResetRecord).grid(row=2, column=1)
        self.btnExit = Button(ReceiptButtomFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13,
                              text='Exit', command=iExit).grid(row=2, column=2)

        # _____________________________________________________________________________________________________________


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title('Hospital Management')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        # ____________________________________________________________________________________________________________
        comboNameTablets = StringVar()
        Dose = StringVar()
        NumberOfTablets = StringVar()
        Lot = StringVar()
        MfgDate = StringVar()
        ExpDate = StringVar()
        Doctor = StringVar()
        SideEffects = StringVar()
        Information = StringVar()
        Reference = StringVar()
        PhoneNumber = StringVar()
        RoomNumber = StringVar()
        DirectionsToUse = StringVar()
        PatientID = StringVar()
        AadharNumber = StringVar()
        PatientName = StringVar()
        PatientDOB = StringVar()
        PatientAddress = StringVar()

        # ________________________________________________________________________________________
        def FetchFromDatabase(medicine):
            string = 'select * from medicines where medicine_name = "%s"'
            args = (medicine,)
            cursor.execute(string % args)
            adder = cursor.fetchone()
            Lot.set(adder[1])
            MfgDate.set(adder[2])
            ExpDate.set(adder[3])

        def GetData():
            if comboNameTablets.get() == "Paracetamol":
                FetchFromDatabase('Paracetamol')
            elif comboNameTablets.get() == "Ibuprofen":
                FetchFromDatabase('Ibuprofen')
            return

        def ChangeLot(medicine_name):
            temp_lot1 = int(Lot.get())
            temp_quantity = int(NumberOfTablets.get())
            temp_lot2 = int(temp_lot1 - temp_quantity)
            Lot.set(temp_lot2)
            string = 'update medicines set medicine_units = "%s" where medicine_name = "%s"'
            args = (temp_lot2, medicine_name)
            cursor.execute(string % args)
            connection.commit()
            return

        def iExit():
            iExit = tkinter.messagebox.askyesno("Hospital Management System",
                                                "Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return

        def iPrescription():
            if (comboNameTablets == "" or PatientName == "" or PatientID == "" or PatientDOB == '' or AadharNumber == ''
                    or RoomNumber == "" or PatientAddress == '' or PhoneNumber == '' or Dose == "" or NumberOfTablets == ''
                    or Lot == '' or MfgDate == '' or ExpDate == '' or Doctor == '' or SideEffects == ''
                    or Information == '' or Reference == '' or DirectionsToUse == ''):
                tkinter.messagebox.showinfo("inert status", "all fields are not filled")
            else:
                self.txtPrescription.insert(END, "Name of Tablets:\t\t" + comboNameTablets.get() + "\n" +
                                            "Patient Name:\t\t" + PatientName.get() + "\n" +
                                            "Room Number:\t\t" + RoomNumber.get() + "\n" +
                                            "Doctor:\t\t" + Doctor.get() + "\n" +
                                            "Number of Tablets:\t\t" + NumberOfTablets.get() + "\n" +
                                            "Side Effects:\t\t" + SideEffects.get() + "\n" +
                                            "Further Information:\t\t" + Information.get() + "\n" +
                                            "Directions to use:\t\t" + DirectionsToUse.get() + "\n")
            return

        def iPrescriptionData():
            name_of_tablet = comboNameTablets.get()
            number_of_tablets = int(NumberOfTablets.get())
            patient_name = PatientName.get()
            patient_id = PatientID.get()
            patient_dob = PatientDOB.get()
            adhaar = AadharNumber.get()
            room_no = RoomNumber.get()
            patient_address = PatientAddress.get()
            ph_no = PhoneNumber.get()
            self.lblLabel = Label(FrameDetail, font=('arial', 10, 'bold'),
                                  text='Name Of Tablets\t\t\tPatient Name\t\t\tReference No.\t\tDosage\t\t'
                                       'Lot\t\tMfg Date\t\tExp Date\t\tPhone Number', pady=8)
            self.lblLabel.grid(row=0, column=0)
            if (comboNameTablets == "" or PatientName == "" or PatientID == "" or PatientDOB == '' or AadharNumber == ''
                    or RoomNumber == "" or PatientAddress == '' or PhoneNumber == '' or Dose == "" or NumberOfTablets == ''
                    or Lot == '' or MfgDate == '' or ExpDate == '' or Doctor == '' or SideEffects == ''
                    or Information == '' or Reference == '' or DirectionsToUse == ''):
                tkinter.messagebox.showinfo("inert status", "all fields are not filled")
            else:
                self.txtFrameDetail.insert(END, comboNameTablets.get() + "\t\t\t" + PatientName.get() + "\t\t\t" +
                                           Reference.get() + "\t\t" + Dose.get() + "\t\t" + Lot.get() + "\t\t" +
                                           MfgDate.get() + "\t\t" + ExpDate.get() + "\t\t" +
                                           PhoneNumber.get() + "\t\t" + "\n")
                string = "insert into patients values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                args = (patient_name, patient_id, patient_dob, adhaar, room_no,
                        patient_address, ph_no, name_of_tablet, number_of_tablets)
                cursor.execute(string % args)
                connection.commit()
                ChangeLot(comboNameTablets.get())
                tkinter.messagebox.showinfo("insert status", "patient inserted successfully")
                cursor.close()

            return

        def iReset():
            comboNameTablets.set("")
            self.comboNameTablet.current(0)
            Dose.set("")
            NumberOfTablets.set("")
            Lot.set("")
            MfgDate.set("")
            ExpDate.set("")
            Doctor.set("")
            SideEffects.set("")
            Information.set("")
            Reference.set("")
            PhoneNumber.set("")
            RoomNumber.set("")
            DirectionsToUse.set("")
            PatientID.set("")
            AadharNumber.set("")
            PatientName.set("")
            PatientDOB.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            return

        def iDelete():
            comboNameTablets.set("")
            self.comboNameTablet.current(0)
            Dose.set("")
            NumberOfTablets.set("")
            Lot.set("")
            MfgDate.set("")
            ExpDate.set("")
            Doctor.set("")
            SideEffects.set("")
            Information.set("")
            Reference.set("")
            PhoneNumber.set("")
            RoomNumber.set("")
            DirectionsToUse.set("")
            PatientID.set("")
            AadharNumber.set("")
            PatientName.set("")
            PatientDOB.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            self.txtFrameDetail.delete("1.0", END)
            return

        # ________________________________________________________________________________________

        MainFrame = Frame(self.master)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 40, 'bold'),
                              text='Hospital Management System', padx=2)
        self.lblTitle.grid()

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=200,
                            padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=50,
                            padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1350, height=450,
                          padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, width=800, height=300,
                                   padx=20, relief=RIDGE, font=('arial', 12, 'bold'),
                                   text='Patient Information')
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=10, width=450, height=250,
                                    padx=20, relief=RIDGE, font=('arial', 12, 'bold'),
                                    text='Receipt')
        DataFrameRight.pack(side=RIGHT)
        # ________________________________________________________________________________________

        self.lblNameTablet = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                   text='Name of tablet:', padx=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        self.comboNameTablet = ttk.Combobox(DataFrameLeft,
                                            textvariable=comboNameTablets,
                                            state='readonly', font=('arial', 12, 'bold'),
                                            width=20)
        self.comboNameTablet['value'] = ('', 'Paracetamol', 'Ibuprofen')
        self.comboNameTablet.current(0)
        self.comboNameTablet.grid(row=0, column=1)

        self.lblInformation = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                    text='Further Information:', padx=2)
        self.lblInformation.grid(row=0, column=2, sticky=W)
        self.txtInformation = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                    textvariable=Information)
        self.txtInformation.grid(row=0, column=3)

        self.lblReference = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                  text='Reference Number:', padx=2)
        self.lblReference.grid(row=1, column=0, sticky=W)
        self.txtReference = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                  textvariable=Reference)
        self.txtReference.grid(row=1, column=1)

        self.lblStorageAdvice = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                      text='Phone Number:', padx=2)
        self.lblStorageAdvice.grid(row=1, column=2, sticky=W)
        self.txtStorageAdvice = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                      textvariable=PhoneNumber)
        self.txtStorageAdvice.grid(row=1, column=3)

        self.lblDosage = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                               text='Dosage:', padx=2)
        self.lblDosage.grid(row=2, column=0, sticky=W)
        self.txtDosage = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                               textvariable=Dose)
        self.txtDosage.grid(row=2, column=1)

        self.lblRoomNumber = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                   text='Room Number:', padx=2)
        self.lblRoomNumber.grid(row=2, column=2, sticky=W)
        self.txtRoomNumber = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                   textvariable=RoomNumber)
        self.txtRoomNumber.grid(row=2, column=3)

        self.lblNumberOfTablets = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                        text='Number of Tablets:', padx=2)
        self.lblNumberOfTablets.grid(row=3, column=0, sticky=W)
        self.txtNumberOfTablets = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                        textvariable=NumberOfTablets)
        self.txtNumberOfTablets.grid(row=3, column=1)

        self.lblDirections = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                   text='Directions to Use:', padx=2)
        self.lblDirections.grid(row=3, column=2, sticky=W)
        self.txtDirections = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                   textvariable=DirectionsToUse)
        self.txtDirections.grid(row=3, column=3)

        self.lblLot = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                            text='Lot:', padx=2)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                            textvariable=Lot)
        self.txtLot.grid(row=4, column=1)

        self.lblPatientID = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                  text='Patient ID:', padx=2)
        self.lblPatientID.grid(row=4, column=2, sticky=W)
        self.txtPatientID = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                  textvariable=PatientID)
        self.txtPatientID.grid(row=4, column=3)

        self.lblMfgDate = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                text='Mfg Date:', padx=2)
        self.lblMfgDate.grid(row=5, column=0, sticky=W)
        self.txtMfgDate = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                textvariable=MfgDate)
        self.txtMfgDate.grid(row=5, column=1)

        self.lblAadhar = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                               text='Aadhar Number:', padx=2)
        self.lblAadhar.grid(row=5, column=2, sticky=W)
        self.txtAadhar = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                               textvariable=AadharNumber)
        self.txtAadhar.grid(row=5, column=3)

        self.lblExpDate = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                text='Exp Date:', padx=2)
        self.lblExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                textvariable=ExpDate)
        self.txtExpDate.grid(row=6, column=1)

        self.lblPatientName = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                    text='Patient Name:', padx=2)
        self.lblPatientName.grid(row=6, column=2, sticky=W)
        self.txtPatientName = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                    textvariable=PatientName)
        self.txtPatientName.grid(row=6, column=3)

        self.lblDailyDose = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                  text='Doctor:', padx=2)
        self.lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                  textvariable=Doctor)
        self.txtDailyDose.grid(row=7, column=1)

        self.lblPatientDOB = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                   text='Patient DOB:', padx=2)
        self.lblPatientDOB.grid(row=7, column=2, sticky=W)
        self.txtPatientDOB = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                   textvariable=PatientDOB)
        self.txtPatientDOB.grid(row=7, column=3)

        self.lblSideEffects = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                    text='Side Effects:', padx=2)
        self.lblSideEffects.grid(row=8, column=0, sticky=W)
        self.txtSideEffects = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                    textvariable=SideEffects)
        self.txtSideEffects.grid(row=8, column=1)

        self.lblPatientAddress = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                       text='Patient Address:', padx=2)
        self.lblPatientAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientAddress = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                       textvariable=PatientAddress)
        self.txtPatientAddress.grid(row=8, column=3)
        # ________________________________________________________________________________________
        self.txtPrescription = Text(DataFrameRight, font=('arial', 12, 'bold'),
                                    width=43, height=14, padx=2, pady=4)
        self.txtPrescription.grid(row=0, column=0)
        # ________________________________________________________________________________________
        self.lblLabel = Label(FrameDetail, font=('arial', 10, 'bold'),
                              text='Name Of Tablets\t\t\tPatient Name\t\t\tReference No.\t\tDosage\t\t'
                                   'Lot\t\tMfg Date\t\tExp Date\t\tPhone Number', pady=8)
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail = Text(FrameDetail, font=('arial', 12, 'bold'),
                                   width=141, height=4, padx=2, pady=4)
        self.txtFrameDetail.grid(row=1, column=0)
        # ________________________________________________________________________________________
        self.btnAddDetails = Button(ButtonFrame, text='Add Details', font=('arial', 12, 'bold'),
                                    width=20, command=GetData)
        self.btnAddDetails.grid(row=0, column=0)
        self.btnPrescription = Button(ButtonFrame, text='Receipt', font=('arial', 12, 'bold'),
                                      width=20, command=iPrescription)
        self.btnPrescription.grid(row=0, column=1)
        self.btnPrescriptionData = Button(ButtonFrame, text='Receipt Log', font=('arial', 12, 'bold'),
                                          width=20, command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=2)
        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'),
                                width=20, command=iDelete)
        self.btnDelete.grid(row=0, column=3)
        self.btnReset = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'),
                               width=20, command=iReset)
        self.btnReset.grid(row=0, column=4)
        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'),
                              width=20, command=iExit)
        self.btnExit.grid(row=0, column=5)
        # ____________________________________________________________________________________________________________


if __name__ == '__main__':
    main()
