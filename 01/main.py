for i in range(1,10):
    for j in range(1,11-i):
        print(j,"*",i,"=",i*j," ",'\t',end=""),
    print(end='\n')
