
for i in range(1,501):
    s=0
    for j in range(1,i):
        if i%j==0:
            s = s+j
            # s*=0
    if s==i:
        print(i)