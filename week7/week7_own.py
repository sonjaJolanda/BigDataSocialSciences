name = 'Heidi'
name.isalpha() # False if there were 0-9
age = '22'
age.isdigit() # False if there were a-z
nameAndAge = 'Heidi22'
nameAndAge.isalnum() # can be both
# ToDo everything above is not part of the midterm, thats why I haven't included it in the summary
# ----- lambda -------------------------------------------------
m = lambda x: x+10
print(m(3)) # 13
# ToDo the apply function + the lambda function (apply is part of pandas because its a DF function
# --------------------------------------------------------------
names = ['Heidi', 'John', 'Jenny']
print("-and-".join(names)) # Heidi-and-John-and-Jenny
# --------------------------------------------------------------






