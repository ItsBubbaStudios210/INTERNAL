import time
#Varibiles
Name, Version, Creator = "INTERNAL", "BETA", "ItsBubbaStudiosOffical"

# Idea's List
ideas_list = {
    "IDEA TEMPLATE ('Idea' made by 'Creator' its was on 'Platform')",
    "INTERNAL frist brought from ItsBubbaStudiosOffical",
    "Word Maker by My sibiling"
}

# Print All Of The Idea's
for item in ideas_list:
    print(item)

def boot(MaxPercentage, Process, command, Delay):
    percenage = 0
    for i in range(MaxPercentage):
        percenage += 1
        print(f"Process: {Process}\n{percenage} / {MaxPercentage}")
        time.sleep(Delay)
    command()
boot(200, "Booting", None, 0.1)
