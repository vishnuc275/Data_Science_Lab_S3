def fibo(n):
    f1 = 0
    f2 = 1
    if (n < 1):
         return
    for x in range(0, n):
         print(f1, end=" ")
         f3 = f2 + f1
         f1 = f2
         f2 = f3
n=int(input("enter the first N no: "))
fibo(n)