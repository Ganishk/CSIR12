#!/usr/bin/env python3
#Shebang is used to directly execute the script in unix based systems.

import os #For OS specific actions if allowed. It may not work as expected in python IDLE
import time

def clearScreen():
    """This function is used to clear the terminal or command prompt screen."""
    try:
     if os.name=="nt": os.system('cls')
     elif os.name=="posix": os.system('clear') #Unix based systems.
    except: pass

def getData():
    """@sets
    name: Name of the user
    yob: Year of birth
    age: Age of the user
    """
    global name,yob,age;
    name = input("What is your name? ").strip();
    greet(name);
    print(greetStr+', '"welcome to our program");
    while True:
     try:
        yob = int(input("\nEnter your year of birth: "))
        break
     except ValueError: print("Enter correct valid year")
    age = startTime.tm_year - yob

def greet(Name):
    hr = startTime.tm_hour
    global greetStr
    greetStr = "Good "+("morning" if hr>=2 and hr<=10 else
        "afternoon" if hr>=10 and hr<=14 else "evening"
        if hr>=14 and hr<=22 else "night")+" "+ Name.title()

def tellAge(): print("Your age is", age)

def parsePool(pool):
    print("",end="| ");
    for x in pool:
        print(" | ".join(pool[x]),end=" | ")
    else: print()

def birthDay():
    """@assert: if more than one word from a pool is chosen then the 1st chosen word is preferred
    """
    global mob, day, birthBits
    birthBits = 0b11 # The 1st bit checks for the presence of mob while the 2nd bit is for day
    monthBit = 0b01; dayBit=0b10
    while birthBits:
        clearScreen()
        print("Try a new statement by selecting the words from each pool which are suitable to your date of birth. You can capitalize words if needed but spacing should be as it is."
            "\neg. I born on day in which the Second World War came to an end\n") #1st April
        if (birthBits&monthBit):
            print("Month pool:")
            parsePool(months)
        if (birthBits & dayBit):
            print("\nDay pool:")
            parsePool(days)
        statement = input("\nEnter your statement here: ").casefold().split()
        for word in statement:
            for month in months:
                if birthBits&monthBit and word in months[month]:
                    mob = month
                    birthBits ^= monthBit
                    break
            for d in days:
                if birthBits&dayBit and word in days[d]:
                    day = d
                    birthBits ^= dayBit
                    break
    print(f"\n{name}, your DOB is {day}-{mob}-{yob}\n")

def state():
#Assert: Union Territories are considered to be their
#surrounded or nearest state such it shares more border with that.
    clearScreen()
    print("State Clues:")
    for st in STATES:
        print(" "+st)
    opt = input("Choose the option that is more related your state [1-28]: ").strip()
    for x in STATES:
        if x.startswith(opt+"."):
            print(f"Your state is {STATES[x]}")
            return
    else: raise ValueError

def area():
    import math
    area = 0
    sq = lambda:float(input("Enter the side of the square: "))**2
    rect = lambda: \
      float(input("Enter the length of the rectangle: "))* \
      float(input("Enter the breadth of the rectangle: "))
    circle = lambda: math.pi*float(input("Enter the radius of the circle: "))**2
    shapes = [sq, rect, circle]
    print("""
What is the shape of the geometry?
    1: Square
    2: Rectangle
    3: Circle
Enter your option[1-3]: """,end='')
    opt = int(input())
    if opt<1 or opt>3: raise ValueError("Option out of range")
    area = shapes[opt-1]()
    print(f"The area of the shape is {area}")

def temp():
    opt = input("""
What you want to convert?
    1. Celsius to Farenheit
    2. Farenheit to Celcius
Enter your option[1-2]: """)
    opt = int(opt)
    if opt<1 or opt>2: raise ValueError("Option out of range")
    temp = float(input("\nEnter the temperature: "))
    ctf = not (opt-1); del opt
    T = 9*temp/5 + 32 if ctf else (temp-32)*5/9
    print(f"The converted temperature is {T}\u00B0{'F' if ctf else 'C'}")


def main():
    opt=int(input(f"""
{greetStr}, how can i help you?
    1: Find my age
    2: Guess my birthday
    3: Guess my birth state in India
    4: To find area of a shape
    5: Temperature conversion
    0: Exit

Enter your option [0-5]: """))
    if opt>5 or opt<0: raise ValueError("Option out of range")
    options[opt]();

#############################################
#############################################
#############################################
"""The following global variables initialized
at import or start of the script"""
#############################################
#############################################
startTime = time.localtime()
options=[exit,tellAge,birthDay,state,area,temp]
#option variable defined inside main function will not recognise outside function names.
months = {
 "January": ("new year", "pongal","year"),
 "February": ("black day", "valentine","black"),
 "March": ("water","women"),
 "April": ("fool", "earth"),
 "May": ("worker","may","mother"),
 "June": ("jallian wala bagh","father","jallian"),
 #Repeating a word in spaced words to allow them to detect and also give a clear-cut hint
 "July": ("kamarajar","kamarasar", "abdul kalam","apj","kalam"),
 "August": ("independence",),
 "September": ("world war 2", "second world war","world"),
 "October": ("gandhi","student"),
 "November": ("children",),
 "December": ("christ","aids")
}
# Dictionary is faster than tuple and list and so it is used below.
days = {
 1: ("start of wwii","foolish","first day","first","start","started"),
 2: ("end of wwii","end","ended"),
 3: ("disabled persons","disabled"),
 4: ("navy",),
 5: ("teacher",),
 6: ("habitat",),
 7: ("health",),
 8: ("red cross","cross"),
 9: ("legal","post"),
 10: ("human","rights"),
 11: ("technology",),
 12: ("dandi","march"),
 13: ("idndr","disaster"),
 14: ("nehru",),
 15: ("army",),
 16: ("tolerance","peace"),
 17: ("telecommunication",),
 18: ("heritage",),
 19: ("integration","indira gandhi","rajiv gandhi","indira","rajiv"),
 20: ("child rights","children rights","children","child"),
 21: ("iodine",),
 22: ("diversity","biological diversity"),
 23: ("book",),
 24: ("tuberclosis","tb"),
 25: ("voter",),
 26: ("republic",),
 27: ("ngo",),
 28: ("science",),
 29: ("leap",),
 30: ('clean',"cleanliness"),
 31: ("mostly end of month","last day","mostly","last")
}
STATES = {
 "1. Kuchipudi": "Andhra Pradesh",
 "2. Dawn-lit Mountains": "Arunachal Pradesh",
 "3. I'm well known for my tea and silk":"Assam",
 "4. I've a famous city which was built by Magadha ruler":"Bihar",
 "5. The streams of Arpa and Pairi goes through me":"Chhattisgarh",
 "6. May everyone see goodness, may none suffer any pain":"Goa",
 "7. Gandhiji was born here":"Gujarat",
 "8. Capital was supposed to be my part":"Haryana",
 "9. I'm in the western Himalayas":"Himachal Pradesh",
 "10. Dhoni was born here":"Jharkhand",
 "11. I've a palace at a place also called as Erumaiyur & KGF":"Karnataka",
 "12. Guruvaayurappa":"Kerala",
 "13. Rani Lakshmibai attained her brave death":"Madhya Pradesh",
 "14. Chhatrapati Shivaji Maharaj Terminus was here":"Maharashtra",
 "15. Loktak Lake was situated here & I'm the Land of Gold":"Manipur",
 "16. Pilgramage of of Lord Shiva is here":"Meghalaya",
 "17. Mount Saramati is the highest peak of mine":"Nagaland",
 "18. My very own dance is oddisi":"Odisha",
 "19. Golden Temple of Sikhs":"Punjab",
 "20. Only I have a desert in India presently":"Rajastan",
 "21. Conqueror of the three worlds":"Sikkim",
 "22. The language that the first evolved man spoke":"Tamil Nadu",
 "23. Divided from Andhra":"Telangana",
 "24. Most populated state":"Uttar Pradesh",
 "25. Land of Gods - Devbhumi":"Uttarakhand",
 "26. Bengal Tigers in Sundarbans National Park":"West Bengal",
 "27. Land of Mizos":"Mizoram",
 "28. Tripura Sundari Temple":"Tripura"
}
#############################################
#############################################
#############################################

if __name__=="__main__":
    """Entry point as a script starts here"""
    getData();
    while True:
     clearScreen()
     try: main();
     except ValueError: print("[!] Please enter a valid option")
     except KeyboardInterrupt:
         print(); exit() #SIGINT
     input("Press enter to continue...");
# The exits either by SIGINT or exit option (SIGQUIT)
