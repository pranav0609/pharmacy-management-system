import MySQLdb
from tkinter import *
import tkinter.messagebox
from tkinter import ttk

connection = MySQLdb.connect(host='localhost', user='root', password='shubham1701')
cursor = connection.cursor()
string = "use pythondb"
cursor.execute(string)


class Hospital:

    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

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
                root.destroy()
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

        MainFrame = Frame(self.root)
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


root = Tk()
application = Hospital(root)
root.mainloop()
