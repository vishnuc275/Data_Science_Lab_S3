n1=int(input("enter lower limit : "))
n2=int(input("enter higher limit : "))
for num in range(n1,n2+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num)
                break