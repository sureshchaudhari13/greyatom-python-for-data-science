# --------------
# Code starts here

class_1=["Geoffrey Hinton","Andrew Ng","Sebastian Raschka","Yoshua Bengio"]
class_2=["Hilary Mason","Carla Gentry","Corinna Cortes"]
new_class=class_1+class_2
print(new_class)

new_class.append("Peter Warden")
print("New 1 list : ",new_class)

del new_class[5]
print("New 2 list : ",new_class)


# Code ends here


# --------------
# Code starts here

courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}
print(courses)
total=sum(courses.values())
print("total marks :",total)
percentage=total/500*100
print("percentage got : ", percentage)

# Code ends here


# --------------
# Code starts here
mathematics={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,
"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
print("Math scores are :" ,mathematics)

# calculate the max value
max_marks_scored=max(mathematics,key=mathematics.get)
print("Max markes scored in Math :",max_marks_scored)

topper=max_marks_scored

print("Topper : ",topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
namelist=topper.split()
print(namelist)
first_name=namelist[0]
last_name=namelist[1]
print(first_name,"+",last_name)

full_name = last_name + " " +first_name
certificate_name=full_name.upper()
# Code starts here
print(" Name on certificate is : ",certificate_name)


# Code ends here


