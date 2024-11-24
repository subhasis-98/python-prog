gender =input("what is your gender 'male or female' : ")
first_name=input("enter your first name : ")
last_name=input("enter your last name : ")
age = int(input("enter your age : "))

if(gender == "female"):
    if age>=20:
        sts=input("enter your marrital status yes or no :")
        if(sts == "yes"):
            print("Mrs."+first_name+" "+last_name)
        else:
            print("Ms. "+first_name+" "+last_name)
    else:
        print(first_name +" "+last_name)

else:
    if( age >=20):
        print("Mr."+first_name+" "+last_name)
    else:
        print(first_name+" "+last_name)
        