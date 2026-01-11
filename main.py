import time, os, sys, random, string
#Varibiles
Name, Version, Creator = "INTERNAL", "BETA", "ItsBubbaStudiosOffical"
DEBUG = True
command_input = "INTERNAL > "
Max_Verstappen = """
Max Verstappen - F1 Driver

    _________
   | ORACLE  |
 __|_RedBull_|
"""

# Idea's List
ideas_list = {
    "IDEA TEMPLATE ('Idea' made by 'Creator' its was on 'Platform')",
    "INTERNAL frist brought from ItsBubbaStudiosOffical",
    "Word Maker by My sibiling",
    "Random Max Verstappen refernce by MasterOwel6713 on Youtube"
}
# Word Choice list
wordchoice = [
    "5 Letters"
]

# Print All Of The Idea's
def INTERNAL_CREDITS():
    global ideas_list, Max_Verstappen
    randomnumber = random.randint(0, 100)
    if randomnumber == 45:
        print(Max_Verstappen)
        print()
    if DEBUG:
        print(randomnumber)
    for item in ideas_list:
        print(item)

INTERNAL_CREDITS()

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        print("OS not supported for this command")

def random_word():
    global wordchoice
    for item in wordchoice:
        print(item)    
    choice = input("Chose your option")
    def fiveletter():
        letter1 = random.choice(string.ascii_letters)
        letter2 = random.choice(string.ascii_letters)
        letter3 = random.choice(string.ascii_letters)
        letter4 = random.choice(string.ascii_letters)
        letter5 = random.choice(string.ascii_letters)
        print("Your word is")
        print(f"{letter1}{letter2}{letter3}{letter4}{letter5}")
    if choice == wordchoice[0]:
        print("Getting Letters")
        fiveletter()
    else:
        print("ERROR - THAT IS NOT A SELECTABLE OPTION")

def kernal():
    global command_input
    while True:
        command = input(command_input)
        if command == "exit":
            break
        elif command == "help":
            print("exit - Quits the terminal\nclear - Clears the terminal\ncredits - pops up the credits and the ideas people have made\nRESTART - restarts the program\nword - makes a random word and I mean random")
        elif command == "clear":
            clear()
        elif command == "credits":
            INTERNAL_CREDITS()
        elif command == "RESTART":
            os.execv(sys.executable, ['python'] + sys.argv)
        elif command == "word":
            random_word()
        else:
            print("ERROR - INVAILED COMMAND\nType help fot a list of commands")

def boot(MaxPercentage, Process, command, Delay):
    percenage = 0
    for i in range(MaxPercentage):
        percenage += 1
        print(f"Process: {Process}\n{percenage} / {MaxPercentage}")
        time.sleep(Delay)
    command()
boot(100, "Booting", kernal, 0.1)
