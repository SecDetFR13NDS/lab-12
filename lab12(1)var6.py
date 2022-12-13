a=int(input())
b=int(input())
lst=[a,b]
def kratni(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
 
    print(a + b)
kratni(a,b)
def krat(lst):
    for i in range(1, min(lst)+1):
        if all([not num % i for num in lst]):
            print(i)
krat(lst)