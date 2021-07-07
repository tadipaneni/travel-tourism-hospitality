def sdp_16():
    sum = 0
    print("Hello!")
    print("Welcome to TIME TRAVELS!!")
    print("We can assure you that you are going to have a wonderful trip")
    print("We request you to fill the details in order to get register")
    name = str(input ("Enter your name: "))
    mobilenum = str(input("Enter your Mobile number: "))
    address =str(input("Enter your Address details: "))
    emailid = str(input("Enter your Email-id details: "))
    print("Hello",name,"Your details are")
    print("Mobile-Number",mobilenum)
    print("Address",address)
    print("Email-id",emailid)
    print("Create a password which contains alphanumeric characters of min length 8")
    password = input()
    print("Thank you for registering in our travel agency")
    print("We would like to gather some information about your choices")
    print("What kind of climate do you prefer to choose destiny?")
    print("Type warm or cool or pleasant climate")
    climate = input()
    if climate =="warm":
        print("Here are the places which suits your taste:\n1. Rajasthan\n2. Punjab\n3. UttarPradesh")
        print("Select a number from the displayed places")
        place = input()
        if place == "1":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a number for the mode of travelling you prefer to go")
            if mode == "1":
                sum = sum + 15250
            if mode == "2":
                sum = sum + 17500
            if mode == "3":
                sum = sum + 15000
            if mode == "4":
                sum = sum + 25000
           
        if place == "2":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a mode of travelling")
            if mode == "1":
                sum = sum + 13500
            if mode == "2":
                sum = sum + 14950
            if mode == "3":
                sum = sum + 12500
            if mode == "4":
                sum = sum + 22500
             
        if place == "3":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a mode of travelling")
            if mode == "1":
                sum = sum + 15000
            if mode == "2":
                sum = sum + 17500
            if mode == "3":
                sum = sum + 16500
            if mode == "4":
                sum = sum + 20000
           
    if climate == "cool":
        print("Here are the places which suits your taste:\n1. Shimla\n2. Banglore\n3. Nainital")
        print("Select a number from the displayed places")
        place = input()
        if place == "1":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a number for the mode of travelling you prefer to go")
            if mode == "1":
                sum = sum + 20000
            if mode == "2":
                sum = sum + 25000
            if mode == "3":
                sum = sum + 23500
            if mode == "4":
                sum = sum + 30000
             
        if place == "2":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a number for the mode of travelling you prefer to go")
            if mode == "1":
                sum = sum + 18500
            if mode == "2":
                sum = sum + 20000
            if mode == "3":
                sum = sum + 19000
            if mode == "4":
                sum = sum + 25000
             
        if place == "3":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a number for the mode of travelling you prefer to go")
            if mode == "1":
                sum = sum + 16500
            if mode == "2":
                sum = sum + 19500
            if mode == "3":
                sum = sum + 15000
            if mode == "4":
                sum = sum + 32500
             
    
    if climate == "pleasant":
        print("Here are the places which suits your taste:\n1. Maharashtra\n2. Tamilnadu\n3. Karnataka")
        print("Select a number from the displayed places")
        place = input()
        if place == "1":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a number for the mode of travelling you prefer to go")
            if mode == "1":
                sum = sum + 20000
            if mode == "2":
                sum = sum + 25000
            if mode == "3":
                sum = sum + 23500
            if mode == "4":
                sum = sum + 30000
            
        if place == "2":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a number for the mode of travelling you prefer to go")
            if mode == "1":
                sum = sum + 18500
            if mode == "2":
                sum = sum + 20000
            if mode == "3":
                sum = sum + 19000
            if mode == "4":
                sum = sum + 25000
            
        if place == "3":
            print("Which mode of travelling you would prefer to go the destination?")
            print("1. Bus\n 2. Car\n 3. Train\n 4.Airplane" )
            print("Select a number for the mode of travelling you prefer to go")
            if mode == "1":
                sum = sum + 16500
            if mode == "2":
                sum = sum + 19500
            if mode == "3":
                sum = sum + 15000
            if mode == "4":
                sum = sum + 32500
                
  #print(sum)   

            
            
sdp_16();
 
