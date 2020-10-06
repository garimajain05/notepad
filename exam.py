for i in range(6):
    print("")
    for j in range(0,i):
        print("*",end=' ')

count=7
for i in range(6):
    print("")
    count-=1
    for j in range(0,i):
        print(f"{count}",end=' ')