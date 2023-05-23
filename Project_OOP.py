import csv
from abc import ABC
Date_list = []
list=[]
DR_list=[]
P_list=[]
M_list =[]
class Person(ABC):
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display_attributes(self):
        return self.name,self.age,self.gender
class Doctor(Person):
    Doc_name = []

    def __init__(self,name,age,gender,__specification):
        super().__init__(name,age,gender)
        self.__specification = __specification
    def get_name(self):
        return self.name
    def register(self):
        return self.name,self.age,self.gender,self.__specification
    def add_doctor(self):
        doctor = Doctor(self.name,self.age,self.gender,self.__specification)
        DR_list.append(doctor.register())
        Doctor.Doc_name.append(self.name)
    @staticmethod
    def remove_doc():
        try:
            name = input("Doctor name: ")
            for search in Doctor.Doc_name:
                if name == search:
                    print("Got Matched")
                    index = Doctor.Doc_name.index(name)
                    del DR_list[index]
                    print("Successfully removed from the records.............!")
        except:
            print("Please! Enter the valid input ","\n","Thank you!")
    @staticmethod
    def check_specific_date_pat():
        date = input("Enter the specific date(DD.MM.YYYY): ")
        for dates in Patient.pat_date_list:
            if date == dates:
                index = Patient.pat_date_list.index(date)
                print(P_list[index])

    @staticmethod
    def Patient_checkup():
        i = 1
        j = 1
        while j == 1:
            try:
                print(Object1.record())
                choice = int(input("add or end____1 or 0"))
                if choice == 1:
                    while i == 1:
                        Object1.append_pat_list()
                        break
                if choice == 0:
                    break
            except:
                print("Please! Enter the correct choice for patient check up ","\n","Thank you!")
        P_list.append(Object1.record())
class Patient(Person):
    Pat_list=[]
    Pat_name = []
    rem_patient_list = []
    pat_date_list = []
    admit_list = []
    discharged_list = []
    def __init__(self,name,age,gender,contact,address):
        super().__init__(name,age,gender)
        self.contact = contact
        self.address=address
        self.date = date_time
        self.pat_list = []
    def get_name(self):
        return self.name
    def get_name_contact(self):
        return self.name,self.contact
    def get_date(self):
        return self.date
    def record(self):
        return self.date,self.name,self.age,self.gender,self.contact,self.address,self.pat_list
    def append_pat_list(self):
        try:
            return self.pat_list.append(input("Recommended Medincine: "))
        except:
            print("please enter the valid name of medicine","\n","Please try again")
    def add_patient(self):
        try:
            print(" ___Patient Details for Checkup___ :")
            patients = Patient(self.name, self.age, self.gender, self.contact, self.address)
            Patient.Pat_name.append(patients.get_name())
            Patient.rem_patient_list.append(patients.get_name_contact())
            Patient.pat_date_list.append(patients.get_date())
        except:
            print("PLease enter the correct detail of te patient for admit the patient","\n","Thank you!")

    def rem_patient(self):
        try:
            name_contact = input("Patient Name: "), int(input("Patient Contact: "))
            for search in Patient.rem_patient_list:
                if search == name_contact:
                    print("Matched found........")
                    index = Patient.rem_patient_list.index(name_contact)
                    del Patient.rem_patient_list[index]
                    del P_list[index]
                    print("Successfully removed from record.")
        except:
            print("please enter the correct ID for removing the patient","\n","Please Try again","\n","Thank you!")
    def admit_Patient(self):
        print("Fulfil the following details to admit a Patient: ")
        status = "Admitted"
        print(Patient.rem_patient_list)
        try:
            name_contact = input("Patient Name: "), int(input("Patient Contact: "))
            for search in Patient.rem_patient_list:
                if search == name_contact:
                    print("Matched found........")
                    index = Patient.rem_patient_list.index(name_contact)
                    data = P_list[index], date_time,status
                    Patient.admit_list.append(data)
                    print(P_list[index], "is admitted on", date_time)
        except:
            print("Please enter your patient ID for admit in hospital ","\n","Thank you!")
    def discharged_Patient(self):
        print("Fulfil the following details to admit a Patient: ")
        status = "Discharged"
        print(Patient.rem_patient_list)
        try:
            name_contact = input("Patient Name: "), int(input("Patient Contact: "))
            for search in Patient.rem_patient_list:
                if search == name_contact:
                    print("Matched found........")
                    index = Patient.rem_patient_list.index(name_contact)
                    data = P_list[index], date_time,status
                    Patient.discharged_list(data)
                    del Patient.admit_list[index]
                    print(P_list[index], "is discharged on", date_time)
        except:
            print("Please enter your patient ID for admit in hospital ","\n","Thank you!")
    @staticmethod
    def veiw_history():
        try:
            name_contact = input("Patient Name: "), int(input("Patient Contact: "))
            for search in Patient.rem_patient_list:
                if search == name_contact:
                    print("Matched found........")
                    index = Patient.rem_patient_list.index(name_contact)
                    print(P_list[index])
        except Exception as e:
            print(e,"  Try Again and care about errors.")
class Medicine(Patient):
    Med_list = []
    Med_name_price = []
    Med_name = []
    Med_Q = []
    def __init__(self,name,expiry_date,quantity,price):
        self.name = name
        self.expiry_date = expiry_date
        self.quantity = quantity
        self.price = price

    def get_quantity(self):
        return self.quantity
    def rack(self):
        return self.name,self.expiry_date,self.quantity,self.price
    def get_name_price(self):
        return self.name,self.price
    def add_medicine(self):
        medicine= Medicine(self.name,self.expiry_date,self.quantity,self.price)
        Medicine.Med_list.append(medicine.rack())
        M_list.append(medicine.rack())
        Medicine.Med_name.append(medicine.get_name())
        Medicine.Med_name_price.append(medicine.get_name_price())
        Medicine.Med_Q.append(medicine.get_quantity())
    @staticmethod
    def sell_record():
        try:
            name = input("Enter the name: ")
            price = float(input("Enter the price: "))
            exp_date = input("Enter expiry date: ")
            sell_quantity = int(input("Enter the sell quantity: "))
            for z in Medicine.Med_name:
                if name == z:
                    ind = Medicine.Med_name.index(name)
                    if sell_quantity <= Medicine.Med_Q[ind]:
                        Medicine.Med_Q[ind] = Medicine.Med_Q[ind] - sell_quantity
                        print(name, "Rs", "has been sold", "\n", "Remainings are", Medicine.Med_Q[ind])
                        del M_list[ind]

                    new = Medicine(name, exp_date, Medicine.Med_Q[ind], price)
                    M_list.append(new.rack())
                else:
                    print("No such Medicine found.......!")
        except:
            print("Please enter the correct record of medicine for selling then you get the remaining quantity of medicine","\n","Thank you!")
print("DD.MM.YYYY")
date_time = input("Date: ")
print("                                       Hospital Management System ---- Eti & Sami")
print("                                                       ",date_time)
print("\n")
print("                                    ___________Initializing the System__________")
print("\n")
print("                        ___________There are Three zone in our Hospital management system________")
print("\n")
print("                                        ______________Medicine________________")
print("                                        ______________Doctor__________________")
print("                                        ______________Patient_________________")
while True:
    try:
        doc_count = int(input("How many Doctors are in Hospital: "))
        try:
            for i in range(doc_count):
                Object = Doctor(input("Doctor's Name: :"), int(input("Doctor's Age :")), input("Doctor's Gender: "),input("Doctor's Specification :"))
                Object.add_doctor()
            break
        except:
            print("Ensure details are valid: ", "\n", "Thank you! ________ No doctor has been added")
    except:
        print("Please enter the valid input like in positive integer.")

i=2
while i>1:
    try:
        action = input("Zone: ")
    except:
        print("please enter only ______Medicine________Doctor_______Patient____for entering zone in hospital",
              "\n", "Thank you!")
        print(exit())

    if action == "Doctor":
        try:
            print(" ADD = Add a new doctor","\n","Remove = Remove a Existed Doctor","\n","CSDP = Check_specific_date Patients")
            choice = input("ADD/Remove/CSDP")
        except:
            print("please enter the choice for run the program","\n","Thank you!")

        if choice == "ADD":
            try:
                Object = Doctor(input("Doctor's Name: :"), int(input("Doctor's Age :")), input("Doctor's Gender: "),
                                input("Doctor's Specification :"))
                Object.add_doctor()
                print(DR_list)
            except:
                print("Please enter the true data of doctor","\n","Try again")
        if choice == "Remove":
            try:
                Object.remove_doc()
                print(DR_list)
            except:
                print("please define your function then you will be able to remove some doctor","\n","Thank you!")
        if choice == "CSDP":
                Doctor.check_specific_date_pat()
    if action == "Patient":
        try:
            choice = input("Choose for patient _________Add/Remove/Admit/Discharged/View History Treatment/Save today patient record")
        except:
            print("Please enter the valid choice for patient history","\n","Thank you!")
        if choice== "Add":
            try:
                Object1 = Patient(input("Patient's Name: "), int(input("Patient's Age: ")), input("Patient's Gender: "),int(input("Contact: ")), input("Address: "))
                Object1.add_patient()
                Object.Patient_checkup()
                print(P_list)
            except:
                print("please enter the detail of patient in a valid way","___May be Doctor is not present:","\n","Thank you!")
        if choice == "Remove":
            try:
                Object1.rem_patient()
                print(P_list)
            except:
                print("please add the details of patient then you will remove it","\n","Then you define the function","\n","Thank you!")

        if choice == "Admit":
            turn = input("View Admitted/Admit Patient_______________V/A")
            if turn == "V":
                print(*Patient.admit_list, sep= "\n")
            if turn == "A":
                try:
                    Object1.admit_Patient()
                    print(*Patient.admit_list, sep="\n" )
                except:
                    print("Please define your function with the help of add function","\n","Thank you")
            else:
                print("Wrong Inputs...........!")
        if choice == "Discharged":
            turn = input("View Discharged/Discharged Patient_______________V/D")
            if turn == "V":
                print(*Patient.discharged_list, sep="\n")
            elif turn == "D":
                try:
                    Object1.discharged_Patient()
                    print(*Patient.discharged_list, sep="\n" )
                except:
                    print("Please define your function with the help of add function","\n","Thank you")
            else:
                print("Wrong Inputs..........!")
        if choice == "VHT":
            Patient.veiw_history()
        if choice == "save":
            file = open('Patients.csv', 'w+', newline='')
            with file:
                write = csv.writer(file)
                write.writerows(P_list)
    if action == "Medicine":
        try:
            choice = input("choice __Add_Sell__")
        except:
            print("please enter te valid choice for medicine","\n","Try again")
        if choice == "Add":
            try:
                Object_a = Medicine(input("Enter the name of medicine :"),
                                    int(input("Enter the Expiry date of medicine :")),
                                    int(input("Enter the quantity of the medicine :")),
                                    int(input("Enter the price of the medicine :")))
                Object_a.add_medicine()
                print(M_list)
            except:
                print("please enter the valid detail of medicine","\n","Tank you!")
        if choice == "Sell":
            try:
                Medicine.sell_record()
                print(M_list)
            except:
                print("please define your function with the help of adding medicine","\n","Thank you!")