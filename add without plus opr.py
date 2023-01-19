def add(a,b):
    if a!=b:
        return (a*a-b*b)/(a-b)
    else:
        return 2*a
def main():
    a=int(input("Enter 1st num: "))
    b=int(input("Enter 2nd num: "))
    print("Sum is: ", int(add(a,b)))
main()    
          
