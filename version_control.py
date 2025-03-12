#Version 1
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
