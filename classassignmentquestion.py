class classfunctionassignment():
    def Subfields():
        print("Sub-Fields in AI are:")
        course = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for subfields in course:
            print(subfields)
        
    def oddeven():
        num = int(input("Enter a number:"))
        if (num % 2 == 0):
            print(f"{num} is even number")
        else:
            print(f"{num} is odd number")
            
    def elegibile():
        a=input("Enter your genter:")
        num = int(input("Enter the age:"))    
        if(num == 18):
            print("Female age Elegible for marriage:")
            message="female elegible age"
        elif(num == 21):
            print("Male age elegible for marraige:")
            message = "males elegible age"
        else:
            print("not elegible")
            message = "not elegible"
        return message
    
    def percentage ():
        subject1=int(input("subject1="))
        subject2=int(input("subject2="))
        subject3=int(input("subject3="))
        subject4=int(input("subject4="))
        subject5=int(input("subject5="))
        total=subject1+subject2+subject3+subject4+subject5
        percentage = (total/500)*100
        print("total:=",total)
        print("Percentage:=",percentage)
        
    def triangle():
        h=int(input("Height = "))
        b=int(input("Breadth = "))
        print("Area formula:(Height*Breadth)/2")
        Areaoftriangle = (h*b)/2
        print(" Area of triangle =", Areaoftriangle)
        h1=int(input("height1 = "))
        h2=int(input("height2 = "))
        b1=int(input("Breadth = "))
        print("Perimeter formula:(Height1+Height2+Breadth)")
        parimeter = h1+h2+b1
        print("Perimeter of Triange = ",parimeter)
        