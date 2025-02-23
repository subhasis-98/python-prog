def funn(n1,n2):
    common_factor = {i for i in range(1,min(n1+1,n2+1))if n1 % i == 0 and n2 % i == 0}

funn(10,20)