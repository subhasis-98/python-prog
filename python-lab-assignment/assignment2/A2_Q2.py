phy=int(input("Enter marks in physics :"))
chem=int(input("Enter marks in chemistry :"))
math=int(input("Enter marks in math :"))
IT=int(input("Enter marks in IT :"))
bio=int(input("Enter marks in bio :"))
total_mark = phy+math+chem+IT+bio
per = (total_mark/500)*100


print(per)