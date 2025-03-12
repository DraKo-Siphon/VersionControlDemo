def main():
    def banner():
        print("**************SNOWBLOWA EXTREME SKIS**************")
        print("Hello there, this is a simple survey for Snowblowa Extreme Skis which determines whehther you are eligible for a membership.")

    banner()
    #Ask user for their Name
    name = ""
    while not name.isalpha():
        user_name = input("Please enter your name")
        if not user_name.isalpha():
            print("")
            print("Please enter your name - you cannot enter special characters")
        if user_name.isalpha():
            break

    

    #Ask & validate Age
    user_age = 0
    while user_age < 1 or user_age > 100:
            try:
                user_age = int(input("What is your age? (Please enter a valid age between 1 and 100)"))
                if user_age < 1 or user_age > 100:
                    print("")
                    print("Please enter a valid age between 1 and 100.")
            except ValueError:
                    print("")
                    print("Please enter a valid age as a number.")

    #Ask & Validate Income
    user_income = -1
    while user_income < 0:
            try:    
                user_income = int(input("What is your income per annum? (enter value in $)"))
                if user_income < 0:
                    print("Please enter a positive value.")
                    print("")
            except ValueError:
                    print("")
                    print("Please enter a valid income as a number.")

    #Ask & Validate Expierence
    user_expierence = -1
    while user_expierence < 0 or user_expierence > 100:
            try:
                user_expierence = int(input("What is your skiing expierence? (enter in years)"))
                if user_expierence < 0 or user_expierence > 100:
                    print("")
                    print("Please enter a valid value.")
                    print("")
            except ValueError:
                    print("Please enter a valid income as a number.")

                
    #Check if the criteria has been met
    if user_age < 25 and user_income >= 40000 and user_expierence >= 5:
            print("Congratulations, you are eligible for a membership at Snowblowa Exterme skis.")
            print("")
            print("Name:", user_name)
            print("")
            print("Age:", user_age)
            print("")
            print("Income $:", user_income,)
            print("")
            print("Expierence (years):", user_expierence)
                      

    elif user_age > 25 and user_income >= 40000 and user_expierence >= 5:
            print("")
            print("Sorry, you are not eligible for a membership as your age is too high")
            print("")
            print("The age inputed:", user_age)

    elif user_age < 25 and user_income < 40000 and user_expierence >=5:
            print("")
            print("Sorry, you are not eligible for a membership as your income is too low")
            print("The income inputed:", "$",user_income)

    elif user_age < 25 and user_income >= 40000 and user_expierence <5:
            print("")
            print("Sorry, you are not eligible for a membership as your expierence is too low")
            print("The expierence inputed:", user_expierence)

    elif user_age < 25 and user_income < 40000 and user_expierence <5:
            print("")
            print("Sorry, you are not eligible for a membership as your expierence and income are too low")
            print("The expierence and income inputed:", user_expierence,"&","$",user_income)

    elif user_age > 25 and user_income < 40000 and user_expierence >=5:
            print("Sorry, you are not eligible for a membership as your age is too high and income is too low")
            print("The age and income inputed:", user_age,"&", "$",user_income)

    elif user_age > 25 and user_income >= 40000 and user_expierence <5:
            print("")
            print("Sorry, you are not eligible for a membership as your age is too high and expierence is too low")
            print("The age and expierence inputed:", user_age, "&", "$",user_expierence)

    else:
        print("")
        print("Sorry, you are not eligible for a membership as you have not met any of the criteria")
        print("The age,income & expierence inputed:", user_age, "$",user_income, "&", user_expierence)

    #Ask user if they want to restart
    while True:
        restart = input("Do you want to restart? (yes/no)")
        if restart == "yes":
            main()
        elif restart == "no":
            exit()
        else:
            input("Please enter yes or no:")
        


main()

