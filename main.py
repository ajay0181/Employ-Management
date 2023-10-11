from validate import *


class employees:
  ids = []
  depdict = {}

  def __init__(self, empid, name, aadhar, pan, dob, department, designation,
               gender, salary):
    self.empid = empid
    self.name = name
    self.aadhar = aadhar
    self.pan = pan
    self.dob = dob
    self.department = department
    self.designation = designation
    self.gender = gender
    self.salary = salary
    if self.empid not in self.ids:
      self.ids.append(self.empid)
    if self.department in self.depdict.keys():
      self.depdict[self.department].append(self.name)
    else:
      self.depdict[self.department] = [self.name]

  def display(self):
    print(self.empid, "  ", self.name, " ", self.aadhar, " ", self.pan, " ",
          self.dob, " ", self.department, " ", self.designation, " ",
          self.gender, " ", self.salary)

  @classmethod
  def departmentwisedetails(self):
    for k, v in self.depdict.items():
      print(k, '=', v)


employeelist = []
while (True):
  print(
      "----------------------------------------------------------------------------"
  )
  print(
      "----------------------------------------------------------------------------"
  )
  print(
      "----------------------------------------------------------------------------"
  )

  print("press 1 for Add record")
  print("press 2 for display record")
  print("press 3 for search record")
  print("press 4 for delete a  record")
  print("press 5 for department wise Details")
  print("press 6 for update Details")
  print("press 7 for finding maximum salary")
  print("press 8 for finding minimum slary ")
  print("press 9 for exit")
  choice = int(input("enter your choice"))
  if choice == 1:
    while True:
      name = input("enter your Full Name")
      if check_name(name):
        break
      else:
        print("please enter your name correctly")
    while True:
      dob = input("enter your date of birth")
      if check_dob(dob):
        break
      else:
        print("please enter your date of birth correctly")
    while True:
      aadhar = input("enter your aadhar number")
      if check_aadhar_card(aadhar):
        break
      else:
        print("please enter your aadhar number correctly")
    while True:
      pan = input("enter your pan number ")
      if check_pan_card(pan):
        break
      else:
        print("please enter your pan number correctly")
    while True:
      department = input("enter your department")
      if check_departments(department):
        break
      else:
        print("please enter your repective department correctly")
    while True:
      designation = input("enter your designation ")
      if check_designation(designation):
        break
      else:
        print("please enter your designation correctly")
    while True:
      gender = input("enter your gender ")
      if check_gender(gender):
        break
      else:
        print("please enter your gender correctly")
    while True:
      empid = input("enter your employee id number ")
      if empid in employees.ids:
        print("Employee ID already taken")
        continue
      if check_empid(empid):
        break
      else:
        print("please enter your employee id  correctly")

    while True:
      salary = input("enter your salary ")
      if check_salary(salary):
        break
      else:
        print("please enter your salary correctly")

    obj = employees(empid, name, aadhar, pan, dob, department, designation,
                    gender, salary)
    employeelist.append(obj)
  elif choice == 2:
    for i in employeelist:
      i.display()
  elif choice == 3:
    print("press A to search by employeeid")
    print("press B to search by name")
    print("press C to search by aadhar card")

    ch = input("enter your choice")
    if ch == 'A':
      emid = input("enter employee-id")
      for i in employeelist:
        if i.empid == emid:
          i.display()

    if ch == 'B':
      emname = input("enter employee Full Name")
      for i in employeelist:
        if i.name == emname:
          i.display()

    if ch == 'C':
      aad = input("enter your aadhar number")
      for i in employeelist:
        if i.aadhar == aad:
          i.display()

  elif choice == 4:
    print("press A to delete by employeeid")
    print("press B to delete by name")
    print("press C to delete by aadhar card")

    ch = input("enter your choice")
    if ch == 'A':

      emid = input("enter employee-id")
      for i in employeelist:
        if i.empid == emid:
          employeelist.remove(i)

    if ch == 'B':
      emname = input("enter employee Full Name")
      for i in employeelist:
        if i.name == emname:
          employeelist.remove(i)

    if ch == 'C':
      aad = input("enter your aadhar number")
      for i in employeelist:
        if i.aadhar == aad:
          employeelist.remove(i)

  elif choice == 5:
    employees.departmentwisedetails()

  elif choice == 6:

    print("press A to change by employee-Name")
    print("press B to change DOB")
    print("press C to change aadhar card")
    print("press D to change by salary")
    print("press E to change pan")
    print("press F to change department ")
    print("press G to change Designation ")
    choce = input("Enter Your Choice")
    eid = input('enter employee id')
    if choce == 'A':
      newname = input("enter the name you want to change")
      for i in employeelist:
        if i.empid == eid:
          i.name = newname
    if choce == 'B':
      db = input("enter the Date Of Birth you want to change")
      for i in employeelist:
        if i.empid == eid:
          i.dob = db
    if choce == 'D':
      sal = input("enter the new salary")
      for i in employeelist:
        if i.empid == eid:
          i.salary = sal
    if choce == 'C':
      aadr = input("enter the New Aadhar")
      for i in employeelist:
        if i.empid == eid:
          i.aadhar = aadr
    if choce == 'E':
      pen = input("enter the New PAN  ")
      for i in employeelist:
        if i.empid == eid:
          i.pan = pen
    if choce == 'F':
      deep = input("enter the new Department")
      for i in employeelist:
        if i.empid == eid:
          i.department = deep
    if choce == 'G':
      designat = input("enter the New Designation")
      for i in employeelist:
        if i.empid == eid:
          i.designation = designat
    # else:
    #   print("please enter a valid choice")

  elif choice == 7:
    max = 0
    for i in employeelist:
      if int(i.salary) > max:
        max = int(i.salary)
    print("maximum salary is ", max)

  elif choice == 8:
    min = 999999999
    for i in employeelist:
      if int(i.salary) < min:
        min = int(i.salary)
    print("min salary is ", min)
  elif choice == 9:
    break
  else:
    print("please enter a valid choice")

  print(
      "----------------------------------------------------------------------------"
  )
  print(
      "----------------------------------------------------------------------------"
  )
  print(
      "----------------------------------------------------------------------------"
  )
