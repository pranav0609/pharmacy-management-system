import MySQLdb
from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Receipt window")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        DateOfOrder = StringVar()
        DateOfOrder.set(time.strftime("%d/%m/%Y"))
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        amount = StringVar()
        var4=IntVar()

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        med_quantity = StringVar()
        telephone = StringVar()
        Ref = StringVar()

        adhar = StringVar()
        adhar.set("")

        #===============Functions==================
        def iExit():
            iExit = tkinter.messagebox.askyesno("registration window", "are you sure to exit?")
            if iExit>0:
                root.destroy()
                return

        def Reset():
            Firstname.set("")
            #Surname.set("")
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
            #self.cboTypeOfMember.current(0)
            self.cboMethodofPayment.current(0)
        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("registration window", "do you want to reset all registered users to 0 too?")
            if iResetRecord<=0:
                Reset()
            elif iResetRecord>0:
                Reset()
                #self.txtReceipt.config(state=NORMAL)
                self.txtReceipt.delete("1.0", END)
                return
        def Ref_no_Generator():
            x=random.randint(10903, 68921)
            random_Ref = str(x)
            Ref.set(random_Ref)
        
        def Record_Add():
            #Ref_no_Generator()
            patient_id = Ref.get()
            patient_name = Firstname.get()
            patient_address = Address.get()
            patient_tele = telephone.get()
            quantity = med_quantity.get()
            medicine = var1.get()
            adhaar_number = adhar.get()
            patient_room = 3
            if(patient_id=="" or patient_name=="" or patient_address=="" or patient_tele==""or quantity==""or patient_room==0 or adhaar_number==""):
                tkinter.messagebox.showinfo("inert status", "all fields are not filled")
            else:
                
                self.txtReceipt.insert(END, "\t\t" + Ref.get()+ "\t\t" + Firstname.get() + "\t\t" + telephone.get()
                +"\t\t"+DateOfOrder.get() + "\t\t"+ "\t"+ var1.get()+"\t\t"+ med_quantity.get()+"\n")
                connection = MySQLdb.connect(host='localhost', user='root', password='12345')
                string = "use pythondb"
                cursor = connection.cursor()
                cursor.execute(string)
                
                string = "insert into patients values('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                args = ( patient_name, patient_id, adhaar_number, patient_room, patient_address, patient_tele, medicine, quantity)
                cursor.execute(string % args)
                connection.commit()
                tkinter.messagebox.showinfo("insert status", "patient inserted successfully")
                cursor.close()
        def Price():
            if(var4.get() == 1):
                
                quan = int(med_quantity.get())
                self.txtAmount.configure(state=NORMAL)
                if(var1.get() == "Paracetamol"):
                    item1 = int(50*quan) 
                    amount.set("$"+str(item1))
                elif(var1.get() == "Penicillin"):
                    item1 = int(40*quan)
                    amount.set("$"+str(item1)) 
                elif(var1.get() == "Cod liver oil Tabs"):
                    item1 = int(30*quan) 
                    amount.set("$"+str(item1)) 
                elif(var1.get() == "Benadryl"):
                    item1 = int(20*quan) 
                    amount.set("$"+str(item1)) 
            elif(var4.get() == 0):
                self.txtAmount.configure(state=DISABLED)
                amount.set("0")



    #=========================Frames=========================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        Ttileframe = Frame(MainFrame, bd=20, width=1350, padx=26, relief=RIDGE)
        Ttileframe.pack(side=TOP)

        self.lblTtile = Label(Ttileframe, font=('arial', 50, 'bold'), text="Patient Reciept Window", padx = 2)
        self.lblTtile.grid()

    #===================Lower frames ====================
        MemberDeatilsFrame = LabelFrame(MainFrame, bd = 20, width=1350, height = 500,  pady = 5, relief = RIDGE)
        MemberDeatilsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDeatilsFrame, width=880, bd=10, height=400, relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, width=350, height=450, font=('arial', 20, 'bold'), text="Customer Name ", relief=RIDGE)
        MembersName_F.grid(row=0, column=0)

        ReceiptButtomFrame = LabelFrame(MemberDeatilsFrame, bd=10, width=1000, height=450, relief=RIDGE)
        ReceiptButtomFrame.pack(side=RIGHT)

        #===============================================
        self.lblReferenceNo = Label(MembersName_F, font=('arial', 14, 'bold'), text="Reference no", bd = 7)
        self.lblReferenceNo.grid(row=0, column=0)
        self.txtReferenceNo = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=Ref, insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblFirstName = Label(MembersName_F, font=('arial', 14, 'bold'), text="Name", bd = 7)
        self.lblFirstName.grid(row=1, column=0)
        self.txtFirstName = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=Firstname,
         insertwidth=2)
        self.txtFirstName.grid(row=1, column=1)

        # self.lblLastName = Label(MembersName_F, font=('arial', 14, 'bold'), text="Username", bd = 7)
        # self.lblLastName.grid(row=2, column=0)
        # self.txtLastName = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=Surname,
        #  insertwidth=2)
        # self.txtLastName.grid(row=2, column=1)
        
        self.lblQuantity = Label(MembersName_F, font=('arial', 14, 'bold'), text="Quantity", bd = 7)
        self.lblQuantity.grid(row=7, column=0)
        self.txtQuantity = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=med_quantity,
         insertwidth=2)
        self.txtQuantity.grid(row=7, column=1)
        
        self.lblAddress = Label(MembersName_F, font=('arial', 14, 'bold'), text="Address", bd = 7)
        self.lblAddress.grid(row=2, column=0)
        self.txtAddress = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=Address,
         insertwidth=2)
        self.txtAddress.grid(row=2, column=1)
        
        self.lblTele = Label(MembersName_F, font=('arial', 14, 'bold'), text="Telephone No", bd = 7)
        self.lblTele.grid(row=3, column=0)
        self.txtTele = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=telephone,
         insertwidth=2)
        self.txtTele.grid(row=3, column=1)

        self.lblAdhar = Label(MembersName_F, font=('arial', 14, 'bold'), text="Adhar no", bd = 7)
        self.lblAdhar.grid(row=4, column=0)
        self.txtAdhar = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=adhar,
         insertwidth=2)
        self.txtAdhar.grid(row=4, column=1)
        
        self.lblDate = Label(MembersName_F, font=('arial', 14, 'bold'), text="Date", bd = 7)
        self.lblDate.grid(row=5, column=0)
        self.txtDate = Entry(MembersName_F, font=('arial', 14, 'bold'),  bd=7, textvariable=DateOfOrder,
         insertwidth=2)
        self.txtDate.grid(row=5, column=1)
        
        #===============================================

        #===================Member info================
        self.lblMedicine = Label(MembersName_F, font=('arial', 14, 'bold'), text="Medicine", bd = 7)
        self.lblMedicine.grid(row=6, column=0)

        self.cboMedicince = ttk.Combobox(MembersName_F, textvariable=var1, state='readonly', font=('arial', 14, 'bold'), width=19)
        self.cboMedicince['value'] = ('', 'Paracetamol', 'Penicillin', 'Cod liver oil Tabs', 'Benadryl')
        self.cboMedicince.current(0)
        self.cboMedicince.grid(row=6, column=1)
        self.chkAmount = Checkbutton(MembersName_F, text="Refresh Amount",font=('arial', 14, 'bold'), variable=var4, onvalue=1, offvalue=0, command=Price).grid(row=8, column=0)
        # self.lblAmount = Label(MembersName_F, font=('arial', 14, 'bold'), text="Total Amount", bd = 7)
        # self.lblAmount.grid(row=8, column=1)
        self.txtAmount = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=amount,  bd=7,
         insertwidth=2)
        self.txtAmount.grid(row=8, column=1)

        self.lblMethodOfpayment = Label(MembersName_F, font=('arial', 14, 'bold'), text="Payment method", bd = 7)
        self.lblMethodOfpayment.grid(row=9, column=0)

        self.cboMethodofPayment = ttk.Combobox(MembersName_F, textvariable=var3, state='readonly', font=('arial', 14, 'bold'), width=19)
        self.cboMethodofPayment['value'] = ('', 'Cash', 'Credit card', 'Debit  card', 'UPI wallets')
        self.cboMethodofPayment.current(0)
        self.cboMethodofPayment.grid(row=9, column=1)

        #==============Receipt=====================
        self.lblLabel = Label(ReceiptButtomFrame, font=('arial', 10, 'bold'), pady=10, 
        text='Patient ID\t Patient Name \t Telephone \t Date of Registration \t Medicine \t Quantity', bd=7
        )
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(ReceiptButtomFrame, width=112, height=22, font=('arial', 10, 'bold'))
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        #===================Buttons=================
        self.btnReceipt = Button(ReceiptButtomFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13,
        text='Add', command=Record_Add).grid(row=2, column=0)
        self.btnReset = Button(ReceiptButtomFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13,
        text='Reset', command= iResetRecord).grid(row=2, column=1)
        self.btnExit = Button(ReceiptButtomFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13,
        text='Exit', command=iExit).grid(row=2, column=2)





if __name__ == "__main__":
    root = Tk()
    application = Registration(root)
    root.mainloop()
    