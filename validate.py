def check_name(x):
  l = x.split(' ')
  if (len(l) == 1):
    return False
  if (len(l) == 2):
    return False

  if l[0][0].islower():
    return False
  if l[1][0].islower():
    return False
  if l[2][0].islower():
    return False
  if ''.join(l).isalpha() == False:
    return False
  else:
    return True


def check_aadhar_card(x):
  if x.isdigit() == False:
    return False
  if len(x) != 12:
    return False
  else:
    return True


def check_pan_card(x):
  a = x[:5]
  b = x[5:9]
  c = x[9:]
  if a.isupper() == False:
    return False
  if a.isalpha() == False:
    return False
  if b.isdigit() == False:
    return False
  if c.isalpha() == False:
    return False
  else:
    return True


def check_dob(x):
  l = x.split('/')
  dd = int(l[0])
  mm = int(l[1])
  yy = int(l[2])
  if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    max_days = 31
  elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    max_days = 30
  elif yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0:
    max_days = 28
  else:
    max_days = 29

  if mm < 1 or mm > 12:
    return False
  elif dd < 1 or dd > max_days:
    return False
  else:
    return True


def check_departments(x):
  departments = [
      'hr', 'it', 'sales', 'fin', 'legal', 'sglobal services', 'mess'
  ]
  if x not in departments:
    return False
  else:
    return True


def check_designation(x):
  Designation = [
      'senior developer', 'software developer', 'accountant', 'analyst'
  ]
  if x not in Designation:
    return False
  else:
    return True


def check_gender(x):
  genders = ['male', 'female', 'others']
  if x in genders:
    return True
  else:
    return False


def check_empid(x):
  x = int(x)
  if x > 0 and x < 1000:
    return True
  else:
    return False


def check_salary(x):
  x = int(x)
  if x > 0:
    return True
  else:
    False


#print(check_name("Ajay Singh Rawat"))
# check_aadhar_card("90000")
#print(check_pan_card("DBNPA4127D"))
