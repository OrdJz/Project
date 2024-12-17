import function as fnc

# Header

if __name__ == "__main__" :
    fnc.clss()
    print("Welcome To Library".center(50," "))
    print("="*50,"\n")

    while True :
        print("Create Data : 1\nRead Data : 2\nUpdate Data : 3\nDelete Data : 4")
        
        print("\n"+"="*50)
        
        insert = str(input("\nInsert Here : "))

        print("\n")

        match insert :
            case "1" : fnc.create_data()
            case "2" : fnc.read()
            case "3" : fnc.updates()
            case "4" : fnc.delete()
            case _ : print("Input a valid index !")

        continues = str(input("\nContinue y/n : ")).strip().lower()
        
        if continues == "y" :
            fnc.clss()
        else :
            break
    fnc.clss()