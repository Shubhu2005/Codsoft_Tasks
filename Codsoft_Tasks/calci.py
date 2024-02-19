while(True):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplcation")
    print("4.Division")
    print("5.Modulo")
    print("6.Exit")

    ch=int(input("Enter choice:"))

    if(ch==6):
        print("Good Bye")
        break;

    no1=int(input("enter first number:"))
    no2=int(input("enter second number:"))

    if(ch==1):
        print("Addition is:",no1+no2)
    elif(ch==2):
     print("Subtraction is:",no1-no2)
    elif(ch==3):
       print("Multiplication is:",no1*no2)
    elif(ch==4):
      print("Division is:",no1/no2)
    elif(ch==5):
      print("Modulous is:",no1%no2)
    else:
      print("wrong choice")
      

    
