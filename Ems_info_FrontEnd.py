from tkinter import *
import tkinter.messagebox
import random
import Ems_info_BackEnd
from tkinter import ttk






class Ems_info():
    def __init__(self, master):
        self.master = master
        self.master.title('Employee Record Management System')
        self.master.geometry('1350x750')
        self.master.config(bg='lightblue')

        def information(columns=None):
            # ========================================================Variables=====================================================================
            self.aydi = StringVar()
            self.name = StringVar()
            self.address = StringVar()
            self.gender = StringVar()
            self.mobno = StringVar()
            self.email = StringVar()
            self.department = StringVar()
            self.designation = StringVar()

            # ==========================================================Functions====================================================================
            def EmployeeRec(event):
                try:
                    global selected_tuple

                    index = self.listbox.curselection()[0]
                    selected_tuple = self.listbox.get(index)

                    self.Entry_aydi.delete(0, END)
                    self.Entry_aydi.insert(END, selected_tuple[1])
                    self.Entry_name.delete(0, END)
                    self.Entry_name.insert(END, selected_tuple[2])
                    self.Entry_address.delete(0, END)
                    self.Entry_address.insert(END, selected_tuple[3])
                    self.Entry_gender.delete(0, END)
                    self.Entry_gender.insert(END, selected_tuple[4])
                    self.Entry_mobno.delete(0, END)
                    self.Entry_mobno.insert(END, selected_tuple[5])
                    self.Entry_email.delete(0, END)
                    self.Entry_email.insert(END, selected_tuple[6])
                    self.Entry_department.delete(0, END)
                    self.Entry_department.insert(END, selected_tuple[7])
                    self.Entry_designation.delete(0, END)
                    self.Entry_designation.insert(END, selected_tuple[8])
                except IndexError:
                    pass

            def Add():
                if (len(self.name.get()) != 0):
                    Ems_info_BackEnd.insert(self.aydi.get(), self.name.get(), self.address.get(), self.gender.get(),
                                            self.mobno.get(), self.email.get(), self.department.get(), \
                                            self.designation.get())
                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (
                    self.aydi.get(), self.name.get(), self.address.get(), self.gender.get(), self.mobno.get(),
                    self.email.get(), self.department.get(), \
                    self.designation.get()))

            def Display():
                self.listbox.delete(0, END)
                for row in Ems_info_BackEnd.view():
                    self.listbox.insert(END, row, str(' '))

            def Exit():
                Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                if Exit > 0:
                    self.master.destroy()
                    return

            def Reset():
                self.aydi.set('')
                self.name.set('')
                self.address.set('')
                self.gender.set('')
                self.mobno.set('')
                self.email.set('')
                self.department.set('')
                self.designation.set('')
                self.listbox.delete(0, END)

            def Delete():
                if (len(self.name.get()) != 0):
                    Ems_info_BackEnd.delete(selected_tuple[0])
                    Reset()
                    Display()

            def Search():
                self.listbox.delete(0, END)
                for row in Ems_info_BackEnd.search(self.aydi.get(), self.name.get(), self.address.get(),
                                                   self.gender.get(), self.mobno.get(), self.email.get(),
                                                   self.department.get(), self.designation.get()):
                    self.listbox.insert(END, row, str(' '))

            def Update():
                if (len(self.name.get()) != 0):
                    Ems_info_BackEnd.delete(selected_tuple[0])
                if (len(self.name.get()) != 0):
                    Ems_info_BackEnd.insert(self.aydi.get(), self.name.get(), self.address.get(), self.gender.get(),
                                            self.mobno.get(), self.email.get(), self.department.get(), \
                                            self.designation.get())

                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (
                    self.aydi.get(), self.name.get(), self.address.get(), self.gender.get(), self.mobno.get(),
                    self.email.get(), self.department.get(), \
                    self.designation.get()))

            # ============================================================Frames=====================================================================

            self.Main_Frame = LabelFrame(self.master, width=1300, height=500, font=('arial', 20, 'bold'), \
                                         bg='lightblue', bd=15, relief='ridge')
            self.Main_Frame.grid(row=0, column=0, padx=10, pady=20)

            self.Frame_1 = LabelFrame(self.Main_Frame, width=600, height=400, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='lightpink',text='EMPLOYEES RECORD ')
            self.Frame_1.grid(row=1, column=0, padx=10)

            self.Frame_2 = LabelFrame(self.Main_Frame, width=750, height=400, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='lightpink', text='EMPLOYEE DATABASE')
            self.Frame_2.grid(row=1, column=1, padx=5)

            self.Frame_3 = LabelFrame(self.master, width=1200, height=100, font=('arial', 10, 'bold'), \
                                      bg='lightpink', relief='ridge', bd=13)
            self.Frame_3.grid(row=2, column=0, pady=10)

            # ========================================================Labels of Frame_1========================================================
            self.Label_aydi = Label(self.Frame_1, text='Employees ID', font=('arial', 20, 'bold'), bg='lightpink')
            self.Label_aydi.grid(row=0, column=0, sticky=W, padx=20, pady=10)
            self.Label_name = Label(self.Frame_1, text='Name', font=('arial', 20, 'bold'), bg='lightpink')
            self.Label_name.grid(row=1, column=0, sticky=W, padx=20)
            self.Label_address = Label(self.Frame_1, text='Address', font=('arial', 20, 'bold'), bg='lightpink')
            self.Label_address.grid(row=2, column=0, sticky=W, padx=20)
            self.Label_gender = Label(self.Frame_1, text='Gender', font=('arial', 20, 'bold'), bg='lightpink')
            self.Label_gender.grid(row=3, column=0, sticky=W, padx=20)
            self.Label_mobno = Label(self.Frame_1, text='Mobile Number', font=('arial', 20, 'bold'), bg='lightpink')
            self.Label_mobno.grid(row=4, column=0, sticky=W, padx=20)
            self.Label_email = Label(self.Frame_1, text='Email', font=('arial', 20, 'bold'), bg='lightpink')
            self.Label_email.grid(row=5, column=0, sticky=W, padx=20)
            self.Label_department = Label(self.Frame_1, text='Department', font=('arial', 20, 'bold'), bg='lightpink')
            self.Label_department.grid(row=6, column=0, sticky=W, padx=20)
            self.Label_designation = Label(self.Frame_1, text='Designation', font=('arial', 20, 'bold'), bg='lightpink')
            self.Label_designation.grid(row=7, column=0, sticky=W, padx=20, pady=10)

            # ========================================================Entries of Frame_1========================================================
            self.Entry_aydi = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.aydi)
            self.Entry_aydi.grid(row=0, column=1, padx=10, pady=5)
            self.Entry_name = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.name)
            self.Entry_name.grid(row=1, column=1, padx=10, pady=5)
            self.Entry_address = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.address)
            self.Entry_address.grid(row=2, column=1, padx=10, pady=5)
            self.Entry_gender = ttk.Combobox(self.Frame_1, values=(' ', "Male", "Female"), \
                                             font=('arial', 17, 'bold'), textvariable=self.gender, width=19)
            self.Entry_gender.grid(row=3, column=1, padx=10, pady=5)
            self.Entry_mobno = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.mobno)
            self.Entry_mobno.grid(row=4, column=1, padx=10, pady=5)
            self.Entry_email = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.email)
            self.Entry_email.grid(row=5, column=1, padx=10, pady=5)
            self.Entry_department = ttk.Combobox(self.Frame_1,
                                                 values=(' ',  "IT", "Operations", "Sales"), \
                                                 font=('arial', 17, 'bold'), textvariable=self.department, width=19)
            self.Entry_department.grid(row=6, column=1, padx=10, pady=5)

            self.Entry_designation = ttk.Combobox(self.Frame_1, values=(
            ' ', "Manager", "Asst Manager", "Project Manager", "Team Lead", "Senior Tester",
            "Junior Tester", "Senior Developer", "Junior Developer", "Intern"), \
                                                  font=('arial', 17, 'bold'), textvariable=self.designation, width=19)
            self.Entry_designation.grid(row=7, column=1, padx=10, pady=5)

            # ========================================================Buttons of self.Frame_3=========================================================
            self.btnSave = Button(self.Frame_3, text='SAVE', font=('arial', 17, 'bold'), width=8, command=Add)
            self.btnSave.grid(row=0, column=0, padx=10, pady=10)
            self.btnDisplay = Button(self.Frame_3, text='DISPLAY', font=('arial', 17, 'bold'), width=8, command=Display)
            self.btnDisplay.grid(row=0, column=1, padx=10, pady=10)
            self.btnReset = Button(self.Frame_3, text='NEW', font=('arial', 17, 'bold'), width=8, command=Reset)
            self.btnReset.grid(row=0, column=2, padx=10, pady=10)
            self.btnUpdate = Button(self.Frame_3, text='UPDATE', font=('arial', 17, 'bold'), width=8, command=Update)
            self.btnUpdate.grid(row=0, column=3, padx=10, pady=10)
            self.btnDelete = Button(self.Frame_3, text='DELETE', font=('arial', 17, 'bold'), width=8, command=Delete)
            self.btnDelete.grid(row=0, column=4, padx=10, pady=10)
            self.btnSearch = Button(self.Frame_3, text='SEARCH', font=('arial', 17, 'bold'), width=8, command=Search)
            self.btnSearch.grid(row=0, column=5, padx=10, pady=10)
            self.btnExit = Button(self.Frame_3, text='EXIT', font=('arial', 17, 'bold'), width=8, command=Exit)
            self.btnExit.grid(row=0, column=6, padx=10, pady=10)

            # ===============================================List Box and self.scrollbar========================================================
            self.scrollbar = Scrollbar(self.Frame_2)
            self.scrollbar.grid(row=0, column=1, sticky='ns')
            self.scrollbar = Scrollbar(self.Frame_2, orient=HORIZONTAL)
            self.scrollbar.grid(row=8, column=1, sticky='ns')
            self.listbox = Listbox(self.Frame_2, width=75, height=20, font=('arial', 12, 'bold'))
            self.listbox.bind('<<ListboxSelect>>', EmployeeRec)
            self.listbox.grid(row=0, column=0)
            self.scrollbar.config(command=self.listbox.yview)
            self.scrollbar.config(command=self.listbox.xview)

        information()


root = Tk()
obj = Ems_info(root)
root.mainloop()