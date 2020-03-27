from datetime import datetime, timedelta, date
# Written by Paul Swisher, all rights reserved.
# This program will take a deciaml hour number like 4.32 and output a quiiting time based on 8 hours
# This was made to work with Amazon's hourly numbers.

class Hours(object): 
    def main(self): 
        # import class varibales, calls the function 
        MINUTES, NOW, QUITTING_TIME = self.math_func()
        # print the result of the entire code
        print (
            MINUTES, "minutes remaining for 8 hours\n", 
            NOW, "<-- This is now\n",
            QUITTING_TIME, "<------ This is quitting time\n"
            )
        # Re-run the program    
        again = input("Run Again? (y, n): ") 
        if again == "y":
            self.main()
        else: # program exits if No
            exit(0)    

    def math_func(self):
        # class scope variable
        querry, REMAINDER = self.main_logic()
        IN_TIME = querry
        # equations for converting decimal into human readable time
        TIMELEFT = (((REMAINDER - float(IN_TIME))*100)/1.67)*60 
        MINUTES = str(TIMELEFT/60).split(".")[0]
        NOW = str(datetime.now()).split(".")[0]
        QUITTING_TIME = str(datetime.now() + timedelta(seconds=TIMELEFT)).split(".")[0]
        return MINUTES, NOW, QUITTING_TIME
    
    # main Logic
    def main_logic(self):
        try:
            if date.today().weekday() != 4: # if not yet Friday, run this statement
                while True: # input validation
                    try:    
                        querry = float(input("Please enter a time worked so far TODAY: "))       
                    except ValueError:
                        print("Sorry, I didn't understand that.")
                    else: 
                        break # end of while loop for input validation, ensures float() can run                 
                if querry < 40:
                    REMAINDER = 8 # sets value of 8 for math_func()
                if querry >= 8: # eight hour day is over!
                    print("Quitting Time!!")
                    exit (0)
            elif date.today().weekday() == 4: # if it is friday, run this statement
                while True: # input validation for friday code block, ensures float() can run
                    try:    
                        querry = float(input("\nPlease enter the number for the WEEK: "))      
                    except ValueError:
                        print("Sorry, I didn't understand that.")
                    else: 
                        break # end input validation
                if querry <= 40: # sets the value for the whol eweek for the math_func()
                    REMAINDER = 40 
                elif querry > 40 and querry < 80: 
                    REMAINDER = 80 # sets the vaule for the math_func if querry(input) is higher than 40
                elif querry >= 80:
                    print("Quitting Time!!")
                    exit (0)
            return querry, REMAINDER
        except Exception as e:
            print (e)

if __name__ == "__main__":
    Hours().main()

