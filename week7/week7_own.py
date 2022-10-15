names = ['Heidi', 'John', 'Jenny']
print("-and-".join(names)) # Heidi-and-John-and-Jenny
# --------------------------------------------------------------
name = 'Heidi'
name.isalpha() # False if there were 0-9
age = '22'
age.isdigit() # False if there were a-z
nameAndAge = 'Heidi22'
nameAndAge.isalnum() # can be both
# ----- lambda -------------------------------------------------
m = lambda x: x+10
print(m(3)) # 13
# --------------------------------------------------------------


