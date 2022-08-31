#from operator import is_


#count = 10

#if count > 20:
 #   print("Count is greater")
#else:
#    print("Count is not greater")

#If..elif..elif..else
#is_fanta = False
#is_coke = True
#is_mirinda = False

#if is_fanta:
 #   print("Buying Fanta")
#elif is_coke:
 #   print("Buying coke")
#elif is_mirinda:
 #   print("Buynig Mirinda")
#else:
    #print("Buying water")

from operator import is_

is_raining = False
is_sunny = True
voting_age = 18

age = int(input("How old are you?"))

if age >= voting_age:
    if is_raining:
        print("Please carry your umbrella and go voting")

    elif is_sunny:
        print("Please wear light cloths and go for voting")

    else:
        print("Please wear normal cloths")

else:
        print("Sorry your not allowed to vote")

# write a program that converts tempreture from 
# degrees celious to degrees fahrenheight.
# the figure should be from user input..
# use if statement to check which coversion the user
# wants to perform.

FAHRENHEIT = 1
CELICIUS = 2
KELVIN = 3
user_choice = int(input("Enter 1 for Fahrebheit to celicius, 2 for celicius to fahrenhiet, 3 for kelvin to fahrenheight"))
if user_choice == FAHRENHEIT:
         fah = float(input(" Enter temp in Fahrenheight: "))
         cel = (fah - 32) * 5/9
         print(str(fah) + " degrees in fahrenheit is " + str(cel) + " degress celicius") 
elif user_choice == CELICIUS:
         cel = float(input(" Enter temp in celicius: "))
         fah = cel  * 9/5 + 32
         print(str(cel) + " degrees in celicius is " + str(fah) + " degress Fahrenhrit") 
elif user_choice == KELVIN:
         Kev = float(input(" Enter temp in kelvin: "))
         fah = Kev * 9/5 - 459.67
         print(str(Kev) + " degrees in kelvin is " + str(fah) + " degress Fahrenhrit") 
else:
         print("Invalid choice, please chose 1,2 or 3")
     
     