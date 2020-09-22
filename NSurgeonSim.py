'''https://realpython.com/python-random/
https://stackoverflow.com/questions/5615648/python-call-function-within-class'''

# Importing modules
import random
import datetime

# Class that stores relevant information for the Patient Transcript
class PatientRecord:
    def __init__(self, doctor, patient, scen, brainArea, sym, tool, timeS, timeE, timeT, stat):
        self.doctor = doctor
        self.patient = patient
        self.scen = scen
        self.brainArea = brainArea
        self.sym = sym
        self.tool = tool
        self.timeS = timeS
        self.timeE = timeE
        self.timeT = timeT
        self.stat = stat
  
    # Writes and displays Patient Transcript 
    def displayRecord(self):
        transcript = open("PatientTranscript.txt", "w+") # File writing
        if self.stat == "alive":
            transcript.writelines("Who Cures? Hospital\nSurgery Report\n\nPatient name: {0}\nRoom number: 2.216\n"
                                  "Operation date: {1}\n\nThe patient went "
                                  "in for surgery due to head trauma from a {2} \nand {3}\nDr. {4} was on call "
                                  "and was head surgeon to perform awake craniotomy on {0}.\n\nO.R. Procedure\nDr. {4} "
                                  "began to perform the craniotomy using a/an {5}, the skull was set aside in wet "
                                  "solution "
                                  "for later reattachment.\nUsing a probe Dr. {4} chose to proceed into {6}, to which "
                                  "the Patient responded well and made it {7}.".format(self.patient, self.timeS,
                                                                                           self.scen,
                                                                                          self.sym, self.doctor,
                                                                                          self.tool, self.brainArea,
                                                                                          self.stat)) # format print
        else:
            transcript.writelines("Who Cures? Hospital\nSurgery Report\n\nPatient name: {0}\nRoom number: 2.216\n"
                                  "Operation date: {1}\nTime of death: {8}\n\nThe patient went "
                                  "in for surgery due to head trauma from a {2} \nand {3}\nDr. {4} was on call "
                                  "and was head surgeon to perform awake craniotomy on {0}.\n\nO.R. Procedure\nDr. {4} "
                                  "began to perform the craniotomy using a/an {5}, the skull was set aside in wet "
                                  "solution "
                                  "for later reattachment.\nUsing a probe Dr. {4} chose to proceed into {6}, to which "
                                  "the Patient did not responded well and was pronounced {7}.\n"
                                  "We are deeply sorry for your loss.".format(self.patient, self.timeS,
                                                                                           self.scen,
                                                                                           self.sym, self.doctor,
                                                                                           self.tool, self.brainArea,
                                                                                           self.stat, self.timeE)) 
        transcript.close()
        transcript = open("PatientTranscript.txt", "r") # File reading
        for line in transcript:
            print(line.strip("\n")) # walk through a string
        transcript.close()

# Function definition
def welcome():
# Tell them they are in a hospital and they are the surgeon
  print("Welcome to Who Cures Hospital! We've had a lot of accidents here, we need a lot of help.\n"
        "Let's get you checked in.")
  drname = input("\nWhat is your name? ") # Assignment statement
  print("Welcome Dr. "+drname+". We are glad you could help us.\n ")
  return drname

#Symptoms to be called into each scenario randomly
def symptoms():
    fsym = "has been experiencing sudden changes in behavior, such as aggression, \n questionable moral " \
           "judgement, loss of motor \n functions, and loss of memory – acting completely out of the ordinary.\n"
    psym = "has complained of being unable to feel things such as heat, pain, and pressure,\n essentially losing the " \
           "ability to process these stimuli.\n"
    osym = "has been experiencing loss of vision, blurred vision, illusions and hallucinations; \n tox-screen is " \
           "clean, so it's not drugs.\n"
    tsym = "has been having trouble speaking, is unable to understand language,\n depletion of hearing," \
           " loss of short term memory, and inability to form new memories.\n"
    sympts = fsym, psym, osym, tsym
    return sympts, fsym, psym, osym, tsym

# Function defintion with parameters
def accident(sympts):
    #welcome player + explain instructions

    while True:
        scenario = input("Choose a number from 1 to 3: ")
        randsym = random.choice(sympts) # random module
        if scenario == "1": # if statement
            character = "Bob"
            pname = "SquarePants, SpongeBob"
            accid = "car accident"
            print("\nScenario 1: SpongeBob was street racing with his friends on a Friday night.\n Everything was "
                  "going well and they were all having fun,\n unfortunately, Bob got into a car accident.\n His "
                  "friends take him to the hospital and the doctors explain that \n the accident caused severe brain "
                  "damage.\n Bob will need to get surgery, but sadly,\n the chances of surviving are low. "
                  "Everything must be done perfectly.\n\n {0} {1}".format(character, randsym))
            decision = input("Do you wish to start this surgery or would you rather choose a different scenario?\n"
                             "Enter \"s\" for Start or \"c\" for Choose new scenario: ").lower()
            if decision == "s": # nested if statement
                print("Thank you for helping Bob.")
                break
            elif decision == "c":
                print("Bob will understand.")
                continue

            else:
                decision = input("\nPlease enter a valid letter. \"s\" for Start or \"c\" for Choose new scenario: ")
                if decision == "s":
                    print("Thank you for helping Bob.")
                    break
                elif decision == "c":
                    print("Bob will understand.")
                    continue
                else:
                    print("Let's start over.")
                    continue
        if scenario == "2":
            character = "Snow White"
            pname = "White, Snow"
            accid = "banana slip"
            print("\nScenario 2: Snow White was playing tag with the Seven Dwarfs.\n They were running around until "
                  "Snow White slipped with a banana peel that Sleepy \n left behind... he was too "
                  "sleepy to notice it. \n However, Snow White's fall was hard enough to require a trip to the "
                  "hospital.\n The doctors said she got brain damage, so surgery must be done perfectly to ensure "
                  "she's back to normal.\n\n {0} {1}".format(character, randsym))
            decision = input("Do you wish to start this surgery or would you rather choose a different scenario?\n"
                             "Enter \"s\" for Start or \"c\" for Choose new scenario: ").lower()
            if decision == "s":
                print("Thank you for helping Snow White.")
                break
            elif decision == "c":
                print("Snow White will understand.")
                continue

            else:
                decision = input("Please enter a valid letter. \"s\" for Start or \"c\" for Choose new scenario: ")
                if decision == "s":
                    print("Thank you for helping Snow White.")
                    break
                elif decision == "c":
                    print("Snow White will understand.")
                    continue
                else:
                    print("Let's start over.")
                    continue
        if scenario == "3":
            character = "Nemo"
            pname = "Nemo"
            accid = "shark attack"
            print("\nScenario 3: Nemo was being a rebel and decided to abandon his dad.\n As Nemo was swimming by "
                  "himself, he quickly became attractive to nearby sharks, who ended up attacking him.\n Nemo "
                  "immediately regretted leaving his dad, but by this point,\n he had to focus on escaping the "
                  "sharks. He managed to flee,\n but he was not free of harm – the sharks ferociously "
                  "bit his head.\n Luckily, a witness immediately came to his help and took him to the underwater"
                  " hospital.\n The bite was strong enough to cause brain damage, so surgery will be needed.\n\n "
                  "{0} {1}".format(character, randsym))
            decision = input("Do you wish to start this surgery or would you rather choose a different scenario?\n"
                             "Enter \"s\" for Start or \"c\" for Choose new scenario: ").lower()
            if decision == "s":
                print("Thank you for helping Nemo.")
                break
            elif decision == "c":
                print("Nemo will understand.")
                continue

            else:
                decision = input("Please enter a valid letter. \"s\" for Start or \"c\" for Choose new scenario: ")
                if decision == "s":
                    print("Thank you for helping Nemo.")
                    break
                elif decision == "c":
                    print("Nemo will understand.")
                    continue
                else:
                    print("Let's start over.")
                    continue
        else:
            print("Please enter a valid number.")
            continue

    return scenario, character, pname, accid, randsym

#Contains all tools that could be possibly used
def toolTray():
    tools = ('hammer', 'drill', 'tongs', 'saw', 'scalpel', 'scissors', 'gauze', 'electric probe', 'stimulator', 'needle') # tuple
    return tools

#Getting ready to start the surgery
def surgeryPrep():
    print("\nAfter the patient stabilized, they were prepped for surgery.\nThey are now in the operating room being "
          "anesthetized.\nYou will begin with a craniotomy, then search for the damaged area in the brain.")
    ready = input("Are you ready? ").upper()
    try: # try except
        if ready == "YES":
            print("Good, you had no other choice. Scrub in.")
        elif ready == "NO":
            print("Well, you have no other choice. Scrub in.")
        else:
            raise Exception
    except:
        print("I'll take that as a yes! Time to scrub in.")
        
# Fucntion with parameters
def chooseArea(randsym, fsym, psym, osym, tsym):
    print("\nThe occipital lobe is responsible for sight and visual processing.")
    print("The temporal lobe affects speech and speech recognition.")
    print("The frontal lobe involves changes in behavior and motor functions.")
    print("The parietal lobe controls basic survival functions such as temperature regulation, sensation, and pain.\n")
    score = 100
    while True: # while loop
        area = input("What area do you want to inspect? Choose \"o\" for Occipital, \"t\" for Temporal, \"f\" for "
                     "Frontal, or \"p\" for Parietal: ").lower()
        if randsym == osym:
            if area == "o":
                break
            else:
                score -= 20
                print("Incorrect choice: -20 pts. Please choose again.")
                continue
        elif randsym == tsym:
            if area == "t":
                break
            else:
                score -= 20
                print("Incorrect choice: -20 pts. Please choose again.")
                continue
        elif randsym == psym:
            if area == "p":
                break
            else:
                score -= 20
                print("Incorrect choice: -20 pts. Please choose again.")
                continue
        else:
            if area == "f":
                break
            else:
                score -= 20
                print("Incorrect choice: -20 pts. Please choose again.")
                continue
    return area, score

#Function that deals with the Frontal lobe
def frontal(score, tools, randsym, fsym, psym, osym, tsym):
    # score = 100
    print("The frontal lobe is responsible emotion control, decision making, and intellectual ability.")
    choiceF = input("Perform operation? (Yes) or (No): ")
    if choiceF.lower() == "yes":
        # print("You proceed to was your hands. Do you: \n 1. Turn on the faucet and let the water run from your thumb
        # to your pinky (input 1+enter)\n2.Turn on the faucet and let the water run from your hands down your wrist ")
        #include in main?
        print("From your tray, you notice you have a:\n -needle\n -saw\n -drill\n -syringe\n -clamp\n -gauze\n "
              "-scalpel")
        print("")
        while True:
            theTool = input("Pick a tool: ")  # makes doctor choose the appropriate tool
            if theTool.lower() == "syringe":
                print("yay")
                break
            elif theTool.lower() == "saw":
                print("Nope.Try again.")
                score -= 5 # -= use
                continue
            elif theTool.lower() == "drill":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "needle":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "clamp":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "gauze":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "scalpel":
                print("Nope.Try again.")
                score -= 5
                continue
            else:
                print("Dr, are you okay? That's not on the tray. Look again.")
                score -= 5
                continue

        print("You pick up the " + theTool + " and you: ")
        try:
            decision = input("1) Move left \n2) Move right\n3) Move center\n\nEnter corresponding Number: ")
            if decision.lower() == "1":
                print("The patient has no reaction")
            else:
                score -= 10
                print("The patient has lost their moral compass, and has no control.")
        except:
            print("Pick a valid decision.")
        while (True):
            choiceFr = input("What would you like to do now?\n Continue:(press c + enter)\n Retreat and count "
                             "your losses: (press l + enter): ")
            if choiceFr.lower() == "c":
                deep = input(
                    "You proceed deeper into the brain and find a lesion. Do you:\n Remove the lesion? (press r + "
                    "enter)\nGently shank the area away?"
                    " (press s + enter)\nDo nothing and hope nobody else noticed.(press n + enter): ")
                if deep == "s":
                    score -= 10
                    print("\nUh oh... there appear to be some complications...")
                    print("...")
                    print("Unfortunately, the patient did not make it, but you'll keep working just in case.")
                    # status = "dead"
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                    break
                elif deep == "r":
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                    # return theTool, status
                    break
                else:
                    score -= 10
                    print("\nUh oh... there appear to be some complications...")
                    print("...")
                    print("Unfortunately, the patient did not make it")
                    status = "dead"
                    break
            else:
                print("Retreating did not treat the present damage and made it worse.\nUnfortunately,"
                      "the patient did not make it.")
                status = "dead"
                print("Your score is " + str(score))
                break
        return theTool, status
    else:
        print("You have no other choice.")
        print("From your tray, you notice you have a:\n -needle\n -saw\n -drill\n -syringe\n -clamp\n -gauze\n "
              "-scalpel")
        print("")
        while True:
            theTool = input("Pick a tool: ")  # makes doctor choose the appropriate tool
            if theTool.lower() == "syringe":
                print("yay")
                break
            elif theTool.lower() == "saw":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "drill":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "needle":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "clamp":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "gauze":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "scalpel":
                print("Nope.Try again.")
                score -= 5
                continue
            else:
                print("Dr, are you okay? That's not on the tray. Look again.")
                score -= 5
                continue

        print("You pick up the " + theTool + " and you: ")
        try:
            decision = input("1) Move left \n2) Move right\n3) Move center\n\nEnter corresponding Number: ")
            if decision.lower() == "1":
                print("The patient has no reaction")
            else:
                score -= 10
                print("The patient has lost their moral compass, and has no control.")
        except:
            print("Pick a valid decision.")
        while (True):
            choiceFr = input("What would you like to do now?\n Continue:(press c + enter)\n Retreat and count "
                             "your losses: (press l + enter): ")
            if choiceFr.lower() == "c":
                deep = input(
                    "You proceed deeper into the brain and find a lesion. Do you:\n Remove the lesion? (press r + "
                    "enter)\nGently shank the area away?"
                    " (press s + enter)\nDo nothing and hope nobody else noticed.(press n + enter): ")
                if deep == "s":
                    score -= 10
                    print("\nUh oh... there appear to be some complications...")
                    print("...")
                    print("Unfortunately, the patient did not make it, but you'll keep working just in case.")
                    # status = "dead"
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                    break
                elif deep == "r":
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                    break
                    #return theTool, status
                else:
                    score -= 10
                    print("\nUh oh... there appear to be some complications...")
                    print("...")
                    print("Unfortunately, the patient did not make it")
                    status = "dead"
                    break
            else:
                print("Retreating did not treat the present damage and made it worse.\nUnfortunately,"
                      "the patient did not make it.")
                status = "dead"
                print("Your score is " + str(score))
                break
        return theTool, status
          
#Function to dedal with the temporal lobe
def temporal(score, tools, randsym, fsym, psym, osym, tsym):
    print("The temporal lobe affects speech and speech recognition. \nYou will need "
          "to inspect this area to determine specifically whether it was \nWernicke's, Broca's, or the Memory Inducing "
          "area that was affected.")

    choiceF = input("Perform operation? (Yes) or (No): ")
    if choiceF.lower() == "yes":
        print("From your tray, you notice you have a:\n -needle\n -saw\n -drill\n -syringe\n -clamp\n -gauze\n "
              "-scalpel\n -electric probe\n -stimulator")
        print("")
        while True:
            theTool = input("Pick a tool: ")  # makes doctor choose the appropriate tool
            if theTool.lower() == "syringe":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "saw":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "drill":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "needle":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "clamp":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "gauze":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "scalpel":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "electric probe":
                print("Yay!")
                break
            elif theTool.lower() == "stimulator":
                print("Yay!")
                break
            else:
                print("Dr, are you okay? That's not on the tray. Look again.")
                score -= 5
                continue
    else:
        print("You have no other choice.")
        print("From your tray, you notice you have a:\n -needle\n -saw\n -drill\n -syringe\n -clamp\n -gauze\n "
              "-scalpel\n -electric probe\n -stimulator")
        print("")
        while True:
            theTool = input("Pick a tool: ")  # makes doctor choose the appropriate tool
            if theTool.lower() == "syringe":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "saw":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "drill":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "needle":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "clamp":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "gauze":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "scalpel":
                print("Nope.Try again.")
                score -= 5
                continue
            elif theTool.lower() == "electric probe":
                print("Yay!")
                break
            elif theTool.lower() == "stimulator":
                print("Yay!")
                break
            else:
                print("Dr, are you okay? That's not on the tray. Look again.")
                score -= 5
                continue
    tempArea = "Wernicke's", "Broca's", "Memory Inducing"
    randArea = random.choice(tempArea)
    print("As you are inspecting the temporal lobe, you discover that the " + randArea + " area was "
                                                                                         "damaged.")
    if randArea == "Wernicke's":
        print("The patient will not be able to form coherent words")
        while True:
            evokeMem = input("Do you want to go deeper or choose another area of the brain to inspect?\nEnter \"g\" to "
                             "Go deeper or \"c\" to Choose again: ").lower()
            if evokeMem == "g":
                result = "finished surgery", "complications"
                randResult = random.choice(result)
                if randResult == "finished surgery":
                    print("\nAs you dug even deeper, you found that you could not improve the damage. "
                          "However, you'll keep working just in case.")
                    # status = "alive"
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                    # return result, status
                else:
                    print("\nUh oh... there appear to be some complications...")
                    print("...")
                    print("Unfortunately, the patient did not make it, but you'll keep working just in case.")
                    # status = "dead"
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                    # return result, status
            elif evokeMem == "c":
                print("Choosing a different area did not treat the present damage and made it worse.\nUnfortunately,"
                      "the patient did not make it.")
                status = "dead"
                #break
            else:
                print("Please enter a valid letter.")
                continue
            return theTool, status
    elif randArea == "Broca's":
        print("The patient will only be able to say one word from now on.")
        while True:
            evokeMem = input("Do you want to go deeper or choose another area of the brain to inspect?\nEnter \"g\" to "
                             "Go deeper or \"c\" to Choose again: ").lower()
            if evokeMem == "g":
                result = "finished surgery", "complications"
                randResult = random.choice(result)
                if randResult == "finished surgery":
                    print("\nAs you dug even deeper, you found that everything was fine. However, you'll keep working "
                          "just in case.")
                    # status = "alive"
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                    # return result, status
                else:
                    print("\nUh oh... there appear to be some complications...")
                    print("...")
                    print("Unfortunately, the patient did not make it, but you'll keep working just in case.")
                    # status = "dead"
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                    # return result, status
            elif evokeMem == "c":
                print("Choosing a different area did not treat the present damage and made it worse.\nUnfortunately,"
                      "the patient did not make it.")
                status = "dead"

            else:
                print("Please enter a valid letter.")
                continue
            return theTool, status
    else:
        print("A memory was evoked in the patient, but you did not find any damage.")
        while True:
            evokeMem = input("Do you want to go deeper or choose another area of the brain to inspect?\nEnter \"g to Go"
                             " deeper or \"C to Choose again: ").lower()
            if evokeMem == "g":
                result = "finished surgery", "complications"
                randResult = random.choice(result)
                if randResult == "finished surgery":
                    print("\nAs you dug even deeper, you found that everything was fine. However, you'll keep working "
                          "just in case.")
                    # status = "alive"
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
                else:
                    print("\nUh oh... there appear to be some complications...")
                    print("...")
                    print("Unfortunately, the patient did not seem to make it, but you'll keep working just in case.")
                    # status = "dead"
                    chance = random.randint(0, 100)
                    if chance <= score:
                        print("You got to the end and... Surgery successful!")
                        status = "alive"
                    else:
                        print("You got to the end and... Fail :(")
                        status = "dead"
                    print('Your score is', score)
            elif evokeMem == "c":
                print("Choosing a different area did not treat the present damage and made it worse.\nUnfortunately,"
                      "the patient did not make it.")
                status = "dead"
            else:
                print("Please enter a valid letter.")
                continue
            return theTool, status
  

# add in parameters later based on other 
def occipital(score, tools, randsym, fsym, psym, osym, tsym):
    # give information on the occipital lobe
    print("""   The occipital lobe is responsible for sight and visual processing. 
    Patients with injury to the occipital lobe exhibit loss of visual capability,
    inability to identify colors, and hallucinations.
    Left and right side signify the left and right lobes of the brain.
    Levels signify the depth of the affected tissue, 1 being surface level, and 3 being deep tissue.\n""")
    side = ['right', 'left'] # list
    sideShort = ['L','R'] # list
    level = ['1','2','3']
    sideInjured = random.choice(side)
    affected = random.choice(level)
    print('We are told the patient fell on their '+sideInjured+' side of their head.'
        'The area that was affected was '+affected+'.'
        '\nWe need to fix the damaged area by stitching it together. ')
    goToSide = input('Which side do you want to operate on? Type "R" to go right or "L" to go left: ').upper()
    while goToSide not in sideShort:
        goToSide = input('Please enter a valid input: ').upper()
    if sideInjured == 'left':
        sideInjured = 'L'
    else:
        sideInjured = 'R'
    if goToSide != sideInjured:
        score -= 25
    levelNow = 1
    while levelNow < 3:
        print('We are at level '+str(levelNow)+' now.' ' Do you want to operate at this level or move deeper?')
        goToLevel = input('Type "M" to move deeper or "S" to stay: ').upper()
        if goToLevel == "M":
            levelNow += 1
        elif goToLevel == "S":
            break
        else:
            goToLevel = input('Please enter a valid input: ')
    print('We are at level ----', levelNow)
    if levelNow != int(affected):
        score -= 25
        if levelNow == 1:
            condition = 'Patient went blind.'
        elif levelNow == 2:
            condition = 'Patient cannot recognize faces.'
        else:
            condition = 'Patient was paralyzed.'
    print('Here are your tools: ')
    for tool in tools: # for loop
        print(tool)
    tries = 3
    choice = input('Select a tool to use. Type in the name of the tool to choose: ').lower()
    while choice != 'needle':
        if choice not in tools:
            choice = input('Please enter a valid input: ')
        else:
            score -= 1
            tries -= 1
            if tries == 0:
                score -= 25
                break
            else:
                print('Are you sure that is the right choice? We need to stitch the area.')
                print('Here are your tools: ')
                for tool in tools: # nested loops
                    print(tool)
                choice = input('Please enter the tool you would like to use: ')
    print('\nYou use the '+choice+' to operate on the brain. The surgery is long and hard. Finally we see the results: ')
    status = fate(score) # Function that calls another funtion
    if status == 'alive':
        print('Congratulations Doctor! The patient is stable. Your hard work paid off!')
    else:
        print('Unfortunately, the patient did not make it. In the middle of the surgery, a mistake was made. '+condition)
    return status, choice
   # print('Your score is',score)

def parietal(score, tools, randsym, fsym, psym, osym, tsym):#should we include score as a parameter for our area functions?
    print("The parietal lobe was damaged in the accident.\nThis is the largest site of neural integration in the "
          "central nervous system.\nIt controls perception, awareness, thought, memory, as well as the patient's "
          "consciousness.\n")
    print("From your tray, you notice you have a:\n -needle\n -saw\n -drill\n -syringe\n -clamp\n -gauze\n -scalpel")
    print("")
    theTool = 0
    while theTool != "needle":
        theTool = input("Pick a tool: ")#makes doctor choose the appropriate tool
        if theTool.lower() == "needle":
            print("Nice choice Doctor!")
            break
        elif theTool.lower() == "saw":
            print("Dr. are you sure?")
            score -= 5
        elif theTool.lower() == "drill":
            print("Dr. are you sure?")
            score -= 5
        elif theTool.lower() == "syringe":
            print("Dr. are you sure?")
            score -= 5
        elif theTool.lower() == "clamp":
            print("Dr. are you sure?")
            score -= 5
        elif theTool.lower() == "gauze":
            print("Dr. are you sure?")
            score -= 5
        elif theTool.lower() == "scalpel":
            print("Dr. are you sure?")
            score -= 5
        else:
            print("Enter a valid tool please! (You lost 5 points for trolling.)")
            score -= 5
            continue

    print("You pick up the " + theTool +" and you: ")
    print("1) Move left \n2) Move right\n3) Move center\n\nEnter corresponding Number.") 

    try:
        decision = input("")
        if decision.lower() == "1":
            print("The patient has no reaction")
        else:
            score -= 10
            print("The patient sits up and starts dabbing")
    except:
        print("Pick a valid decision.")
    print("Do you want to continue operating on the parietal or are you done? ")
    print("To continue operating on the parietal, press 'c + enter'\nTo exit this lobe, press 'e + enter'")
    while(True):
        choice2 = input("")
        if choice2.lower() == "c":
            print("You proceed deeper into the brain and find a small anomaly. Do you:\n Remove the small affected area?"
                  "(press r + enter)\nSprinkle your magic serum consisting of flour and flowers? (press s + enter)\nDo "
                  "nothing (press n + enter)")
            deep = input("")
            if deep == "r":
                score -= 10
                break
            elif deep == "s":
                score -= 10
                break
            elif deep == "n":
                break
            else:
                print("I guess we'll take that as 'We need to exit'.")
                break
        elif choice2.lower() == "e":
            break
    print("Your score is "+str(score))
    print('The surgery was long and difficult, but finally we see the results:')
    status = fate(score)
    if status == 'alive':
        print('Congratulations Doctor! The patient is alive and well! Good work!')
    else:
        print('Unfortunately, the patient did not make it through the surgery.')
    
    return status, theTool
    
def fate(score):
    n = score
    chance = random.randint(0, 100)
    if chance <= n and chance >= 0:
        status = 'alive'
        print("Success!")
    else:
        status = 'dead'
        print("Fail :(")
    return status

      
def main():
    #Imporing time module pts:TBD
    timeStart = datetime.datetime.now()
    timeEnd = datetime.datetime.now()
    # totalTime is how long it took to do the surgery
    totalTime = timeEnd-timeStart

  # other code to perform surgery
    drname = welcome()
    sympts, fsym, psym, osym, tsym = symptoms()
    scenario, character, pname, accid, randsym = accident(sympts)
    tools = toolTray()
    surgeryPrep()
    
    area, score = chooseArea(randsym, fsym, psym, osym, tsym)
    if area == "o":
        status, theTool = occipital(score, tools, randsym, fsym, psym, osym, tsym)
        print("\nThe following transcript of this operation is also available to you for future reference under the "
              "file \"PatientTranscript.txt\":\n\n")
        newPatient = PatientRecord(drname, pname, accid, "the occipital lobe", randsym, theTool, timeStart, timeEnd,
                                   totalTime,
                                   status)
        newPatient.displayRecord()
    elif area == "t":
        theTool, status = temporal(score, tools, randsym, fsym, psym, osym, tsym)
        print("\nThe following transcript of this operation is also available to you for future reference under the "
              "file \"PatientTranscript.txt\":\n\n")
        newPatient = PatientRecord(drname, pname, accid, "the temporal lobe", randsym, theTool, timeStart, timeEnd,
                                   totalTime,
                                   status)
        newPatient.displayRecord()
    elif area == "f":
        theTool, status = frontal(score, tools, randsym, fsym, psym, osym, tsym)
        print("\nThe following transcript of this operation is also available to you for future reference under the "
              "file \"PatientTranscript.txt\":\n\n")
        newPatient = PatientRecord(drname, pname, accid, "the frontal lobe", randsym, theTool, timeStart, timeEnd,
                                   totalTime,
                                   status)
        newPatient.displayRecord()
    else:
        status, theTool = parietal(score, tools, randsym, fsym, psym, osym, tsym)
        print("\nThe following transcript of this operation is also available to you for future reference under the "
              "file \"PatientTranscript.txt\":\n\n")
        newPatient = PatientRecord(drname, pname, accid, "the parietal lobe", randsym, theTool, timeStart, timeEnd,
                                   totalTime,
                                   status)
        newPatient.displayRecord()
  

main()

