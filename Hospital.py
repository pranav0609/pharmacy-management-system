from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


class Hospital:

    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        comboNameTablets = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberOfTablets = StringVar()
        Lot = StringVar()
        MfgDate = StringVar()
        ExpDate = StringVar()
        Dosage = StringVar()
        SideEffects = StringVar()
        Information = StringVar()
        Reference = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        DirectionsToUse = StringVar()
        PatientID = StringVar()
        AadharNumber = StringVar()
        PatientName = StringVar()
        PatientDOB = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()

        # ________________________________________________________________________________________

        def iExit():
            iExit = tkinter.messagebox.askyesno("Hospital Management System",
                                                "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def iPrescription():

            self.txtPrescription.insert(END, "Name of Tablets:\t\t" + comboNameTablets.get() + "\n"
                                        )
            return

        def iPrescriptionData():
            self.lblLabel = Label(FrameDetail, font=('arial', 10, 'bold'),
                                  text='Name Of Tablets\tReference No.\tDosage\t'
                                       'No. of Tablets\tLot\tMfg Date\tExp Date\t'
                                       'Daily Dosage\tStorage Advice\tAdhaar Number\t'
                                       'Patient Name\tDOB\tAddress', pady=8)
            self.lblLabel.grid(row=0, column=0)

            self.txtFrameDetail.insert(END, "\t" + comboNameTablets.get() + "\t\t" +
                                       Dose.get() + "\t\t" + NumberOfTablets.get() + "\t" +
                                       Lot.get() + "\t" + MfgDate.get() + "\t" +
                                       ExpDate.get() + "\t" + Dosage.get() + "\t\t" +
                                       StorageAdvice.get() + "\t" + AadharNumber.get() + "\t\t" +
                                       PatientName.get() + "\t" + PatientDOB.get() + "\t" +
                                       PatientAddress.get() + "\n")
            return

        def iReset():
            comboNameTablets.set("")
            self.comboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberOfTablets.set("")
            Lot.set("")
            MfgDate.set("")
            ExpDate.set("")
            Dosage.set("")
            SideEffects.set("")
            Information.set("")
            Reference.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            DirectionsToUse.set("")
            PatientID.set("")
            AadharNumber.set("")
            PatientName.set("")
            PatientDOB.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            # self.txtFrameDetail.delete("1.0", END)
            return

        def iDelete():
            comboNameTablets.set("")
            self.comboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberOfTablets.set("")
            Lot.set("")
            MfgDate.set("")
            ExpDate.set("")
            Dosage.set("")
            SideEffects.set("")
            Information.set("")
            Reference.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
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
                                    text='Prescription')
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
                                      text='Storage Advice:', padx=2)
        self.lblStorageAdvice.grid(row=1, column=2, sticky=W)
        self.txtStorageAdvice = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                      textvariable=StorageAdvice)
        self.txtStorageAdvice.grid(row=1, column=3)

        self.lblDosage = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                               text='Dosage:', padx=2)
        self.lblDosage.grid(row=2, column=0, sticky=W)
        self.txtDosage = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                               textvariable=Dose)
        self.txtDosage.grid(row=2, column=1)

        self.lblDrivingMachines = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                                        text='Driving Machines:', padx=2)
        self.lblDrivingMachines.grid(row=2, column=2, sticky=W)
        self.txtDrivingMachines = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                        textvariable=DrivingUsingMachines)
        self.txtDrivingMachines.grid(row=2, column=3)

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
                                  text='Dosage:', padx=2)
        self.lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(DataFrameLeft, font=('arial', 12, 'bold'),
                                  textvariable=Dosage)
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
                              text='Name Of Tablets\tReference No.\tDosage\t'
                                   'No. of Tablets\tLot\tMfg Date\tExp Date\t'
                                   'Daily Dosage\tStorage Advice\tAdhaar Number\t'
                                   'Patient Name\tDOB\tAddress', pady=8)
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail = Text(FrameDetail, font=('arial', 12, 'bold'),
                                   width=141, height=4, padx=2, pady=4)
        self.txtFrameDetail.grid(row=1, column=0)
        # ________________________________________________________________________________________
        self.btnPrescription = Button(ButtonFrame, text='Prescription', font=('arial', 12, 'bold'),
                                      width=24, command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)
        self.btnPrescriptionData = Button(ButtonFrame, text='Prescription Data', font=('arial', 12, 'bold'),
                                          width=24, command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)
        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'),
                                width=24, command=iDelete)
        self.btnDelete.grid(row=0, column=2)
        self.btnReset = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'),
                               width=24, command=iReset)
        self.btnReset.grid(row=0, column=3)
        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'),
                              width=24, command=iExit)
        self.btnExit.grid(row=0, column=4)


root = Tk()
application = Hospital(root)
root.mainloop()
