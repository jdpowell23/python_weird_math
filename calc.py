from math import add, sub, multi, div

# Welcome to Draxx Calc
print("\n\nWelcome to Draxxus' Calc!!\n\n")

# Start app with while loop
run = True
while run == True:
    mode = ""
    mode = input("What type of Machine do you want?(Addition, Subtraction, Multiply, Divide) You may also type 'exit' ")
    
    mode = mode.lower()
    if mode == "addition":
        print("\nFUCK YEAH!! ADDITION!\n")
        num1 = int(input("What is the first interger you would like to add? "))
        num2 = int(input("What is the second interger you would like to add? "))
        result = add(num1,num2)
        print("Result: ", result)
    elif mode == "subtraction":
        print("\nFUCK YEAH!! SUBTRACTION!\n")
        num1 = int(input("What is the first interger you would like to subtract? "))
        num2 = int(input("What is the second interger you would like to subtract? "))
        result = sub(num1,num2)
        print("Result: ", result)
    elif mode == "multiplication":
        print("\nFUCK YEAH!! MULTIPLICATION!\n")
        num1 = int(input("What is the first interger you would like to multiply? "))
        num2 = int(input("What is the second interger you would like to multiply? "))
        result = multi(num1,num2)
        print("Result: ", result)
    elif mode == "divide":
        print("\nTHIS IS JUST A FUCKIN FRACTION!\n")
        num1 = int(input("What is the dividend? "))
        num2 = int(input("What is the divisor? "))
        result = div(num1,num2)
        print("Result: ", result)
    elif mode == "vecna":
        print("The morning after the Feast of Mimar, certain citizens of Fteeth came out of the town and entreated upon the besiegers to speak with Lord Vfecna, the Whispered One in his spidered pavilion . They told him they were ready to place the city and all their possessions at his dis crete on, provided their lives were spared. The Whispered One replied that he could not agree to such terms, nor indeed to any others, and that he would see the heads of all Fleeth stacked before him. Hearing his terrible utterance on their fate, these same burghers beseeched him to mercy offering themselves if he would spare the good people of Fleeth, Perhaps the Whispered One was amused. for he ordered them to place one of their number his family and slaves into Lord Vecnas bands. Lots were taken and an upright burthen Goodman Arlan, called his family from within the walls. Join me, for the Great Lord has granted us salety to leave this land be told his wife , seeking to ease her mind. Reassured by his gentle words, she and her children passed through the gate to join her husband. Pleased. the Whispered One gave them ail over to Kas the Hateful. For a day the burghers watched Goodman Artau and his family die at the hands of Kas. When at last it was done, the bur ghers pleaded to take their leave, certain their city had been saved. But the Whispered One turned to his barons and spoke to them. My lordshe said, the people of this city are ready to surrender it at my discretion , on condition that their lives are spared. However I will not make peace with them on these terms, nor any others, ex¬ cept with your consent! Our sagacious master.replied the barons we advise, and even beg you, to accept the terms they offer But the Whispered One did not listen. That very day the mangonels and war wizards were set up outside the walls. The as¬ sault went on for about live hours and then the wizened lord broke the walls of Fleeth with a wave of his hand. By the dawn, the beads of citi¬ zens were stacked before the burg¬ ers. Their own wives and children stared at them foremost This was the humor of Vecna, and as his final cruelty, he allowed these bur ghers to depart in peace and guaranteed their safety for the remainders of their sorrowful lives.\n\n")
    elif mode == "exit":
        print("Thank you for trying Draxxus' dumb FUCKIN  Math Machine!")
        break
    else:
        print("Must choose: Addition, Subtraction, Multiply, Divide, or exit\n\n")
    

# Ask what machine the user wants? Addition, subtraction, multiplication, division or exit

# input numbers

# display result