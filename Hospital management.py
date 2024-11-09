class information:
    def __init__(self,name,roomnumber,disease,doctor):
        self.name=name
        self.roomnumber=roomnumber
        self.disease=disease
        self.doctor=doctor
    def infoprint(self):
        print("Name=",self.name)
        print("Roomnumber=",self.roomnumber)
        print("Disease=",self.disease)
        print("Doctor=",self.doctor)
class patient(information):
    def __init__(self):
      self.listpname=[]
      self.listproom=[]
      self.listpdisease=[]
      self.listpdoctor=[]
      self.listroom=list(range(1,31))
    def patientinfo(self):  
      self.pname=input("Enter the name of the patient :\t")
      print("Room that are avaiable:")
      
      print(self.listroom)
      self.proom=int(input("Enter the room that will be allocated:\t"))
      if self.proom in self.listroom:
          self.listroom.remove(self.proom)
      else:
          print("Please enter the valid value")
          self.patientinfo()
          return    
      self.pdisease=input("Enter the name of the disease of patient:\t")
      self.pdoctor=input("Enter the name of doctor that will check the patient:\t")
      self.listpname.append(self.pname)
      self.listproom.append(self.proom)
      self.listpdisease.append(self.pdisease)
      self.listpdoctor.append(self.pdoctor)
      super().__init__(self.pname,self.proom,self.pdisease,self.pdoctor)
      super().infoprint()
      print("Do you want to add more patients?")
      self.msg=input("Enter yes for more records and No for not:\t")
      if(self.msg=="yes"):
        self.patientinfo()
      else:
        self.showpatientlist()    
    def showpatientlist(self):
        for i ,(lpnam,lproom,lpdisease,lpdoctor) in enumerate(zip(self.listpname,self.listproom,self.listpdisease,self.listpdoctor,)):
              print(f"Patient:{i+1}")
              print(f"Patient Name: {lpnam}")
              print(f"Patient Room: {lproom}")
              print(f"Patient Disease: {lpdisease}")
              print(f"Patient Doctor: {lpdoctor}")
              print("\n")
class doctor:
    def __init__(self):
        self.listdname=[]
        self.listspecial=[]
        self.listavailable=[]
        self.listpatient=[]
    def enter(self):
        self.dname=input("Enter the name of doctor:\t")
        self.special=input("Enter the Degree of that specialization:\t")
        self.available=input("Enter the Hours in which doctor is available:\t")
        self.dpatient=input("Enter the Number of patient that Doctor will check in a day:\t")
        self.listdname.append(self.dname)
        self.listspecial.append(self.special)
        self.listavailable.append(self.available)
        self.listpatient.append(self.dpatient)
        self.doctorlist()
        self.ask=input("Do you want to add more record :\t")
        if(self.ask=="Yes" or self.ask=="yes"):
            self.enter()
        else:
            print("Thanks")  
              
    def doctorlist(self):
        for i ,(ldname,ls,laval,lpatient) in enumerate(zip(self.listdname,self.listspecial,self.listavailable,self.listpatient)):
            print(f"Doctor No:{i+1}")
            print(f"Doctor Name :{ldname}")
            print(f"Doctor is specialized in :{ls}")
            print(f"Doctor is available : {laval} hours")
            print(f"Check the patient in a day: {lpatient}")
            
                          

    



print("Do you want to enter the data of doctor or patient")
user=input("For Doctor enter D and for patient enter P\n")
if(user=="D"):
    d=doctor()
    d.enter()
elif(user=="P"):
    p=patient()
    p.patientinfo()
        
          
        
               
              
                
    

     