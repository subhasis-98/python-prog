str1 = "aabbbc"
counted =[]
s = str1.lower()

maxal = None
max_count = 0
for ch in s:
    if ch not in counted:
        count = s.count(ch)
        print(f"{ch} : {count}")
        counted.append(ch)
    
    if(max_count < count):
        max_count=count
        maxal = ch
print(maxal,max_count)

