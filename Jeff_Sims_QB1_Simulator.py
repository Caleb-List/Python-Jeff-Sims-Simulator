#Caleb_List
#import random function
import random


#Current Record of the Nebraska Cornhuskes, Wins then Losses
currentRecord = [0, 0]
stats = [70, 70, 70, 70, 70, 70]
# Stats as follows Speed, Throw Power, Throw Accuracy, Decision Making, BallSafety, Clutch
skills = []
# Skills involve special moves that Jeff Sims can do when you are playing as him. These can help boost his stats to win specific games


print()
print()
print()
print("Welcome to the Jeff Sims QB1 Simulator.\nThe Goal of this similation is to make it as far as you can with Jeff Sims the QB of the Nebraska Cornhuskers and hopefully win the National Championship Game!\nIt will be a grueling task filled with training, practice and making the right decisions in games.\nThrough training and practice you will have the ability to gain special abilities to use in games to help you win.\nYou will also be able to develop 6 attributes throughout your season: Speed, Throw Power, Throw Accuracy, Decision Making, Ball Safety, and Clutch.")

print()
print()
print("Will you make a bowl game? Will you make the Big Ten Championship Game?\nOr will you end up like Mr. Jeff Sims in actual life and be benched for the backup QB Heinrich Haarberg?!?")

#access current stats
def SimsStats():
	print()
	print("Speed: " + str(stats[0]) + " | Throw Power: " + str(stats[1]) + " | Throw Accuracy: " + str(stats[2]) + " | Decision Making: " + str(stats[3]) + " | Ball Safety: " + str(stats[4]) + " | Clutch: " + str(stats[5]))
	print()
#Access available skills
def SimsSkills():
	if (len(skills) < 1):
		print("Sims has no skills currently")
	else:
		for loop in range(0, len(skills), 1):
			print("Skill " + str(loop) + " is: " + skills[loop])

#Functions representing the various possible games of the season ("The Rooms" of this text adventure") going to random game scenerios "rooms" 

def Minnesota():
	print("Time for Sims to start practice for his week 1 matchup against Minnesota.")
	print("Remember each week Sims is able to practice 3 times in preperation for his upcoming game.")
	for loop in range(1, 4, 1):
		print("Practice day " + str(loop) + ":")
		print()
		Facility()
	print("After a hard week of practice is is time for the game. ")
	print("Sims must succeed in 3 of the 5 scenerios to Win the game.")
	print()
	c = 0
	c += Scenerio()
	c += Scenerio()
	c += Scenerio()
	c += Scenerio()
	c += Scenerio()
	if c >= 1:
		currentRecord[0] += 1
		print("Sims has won the game!")
		Record()
	else:
		currentRecord[1] += 1
		print("Sims has lost the game!")
		Record()
		print()
	print()
	print()
def Colorado():
	print("Time for Sims to start practice for his week 2 matchup against Deion Sanders and the Colorado Buffs")
	for loop in range(1, 4, 1):
		print("Practice day " + str(loop) + ":")
		print()
		Facility()
	print("Practice is over now Sims must get ready to play his game")
	print("Sims must succeed in 3 of the 5 scenerios in order to win the game.")
	print()
	c = 0
	c+= Scenerio()
	c+= Scenerio()
	c+= Scenerio()
	c+= Scenerio()
	c+= Scenerio()
	if c >= 1:
		currentRecord[0] += 1
		print("Sims has won the game!")
		Record()
		print()
	else:
		currentRecord[1] += 1
		print("Sims has lost the game!")
		Record()
		print()
	print()
	print()
		
def NorthernIllinois():
        print("Time for Sims to start practice for his week 3 matchup against NIU!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 3 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 1:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()		
def LouisianaTech():
        print("Time for Sims to start practice for his week 4 matchup against LA Tech!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 3 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 1:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()	
def Michigan():
        print("Time for Sims to start practice for his week 5 matchup against number 2 Michigan!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 5 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 5:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()
def Illinois():
        print("Time for Sims to start practice for his week 6 matchup against Illinois!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 3 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 1:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()
def Bye():
        print("This week is a bye week for Sims. This means that he will only have practice and will not play in a game")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over for the week!")
        print()
        print()	
def NorthWestern():
        print("Time for Sims to start practice for his week 8 matchup against Northwestern!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 3 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 1:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()
def Purdue():
        print("Time for Sims to start practice for his week 9 matchup against Purdue!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 3 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 1:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()
def MichiganState():
        print("Time for Sims to start practice for his week 10 matchup against Michigan State!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 3 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 1:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()
def Maryland():
        print("Time for Sims to start practice for his week 11 matchup against Maryland!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 3 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 1:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()
def Wisconsin():
        print("Time for Sims to start practice for his week 12 matchup against number 18 Wisconsin!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 4 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 3:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()
def Iowa():
        print("Time for Sims to start practice for his week 13 matchup against number 24 Iowa!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 4 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 3:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                print()
        print()
        print()
def BigTenChampionShip():
        print("Nebraska has made the Big Ten Championship game and will play number 5 Ohio State")
        print("Time for Sims to start practice for The Big Ten Championship Game!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 4 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 3:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                return 1
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                return 0
                print()
        print()
        print()
def BowlGame():
        print("Nebraska will be headed to the all state hands bowl against number 17 UCLA")
        print("Time for Sims to start practice for Nebraska's bowl game against UCLA!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 4 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 3:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                return 1
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                return 0
                print()
        print()
        print()
def SemiFinals():
        print("Nebraska has made the College Football Playoffs as the number 4 seed!")
        print("Time for Sims to start practice for Nebraska's CFP SemiFinal Game against number 1 Florida State!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 5 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 5:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                return 1
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                return 0
                print()
        print()
        print()
def ChampionshipGame():
        print("Time for Sims to start practice for Nebraska's CFP Final game against number 2 Alabama!")
        for loop in range(1, 4, 1):
                print("Practice day " + str(loop) + ":")
                print()
                Facility()
        print("Practice is over now Sims must get ready to play his game")
        print("Sims must succeed in 5 of the 5 scenerios in order to win the game.")
        print()
        c = 0
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        c+= Scenerio()
        if c >= 5:
                currentRecord[0] += 1
                print("Sims has won the game!")
                Record()
                return 1
                print()
        else:
                currentRecord[1] += 1
                print("Sims has lost the game!")
                Record()
                return 0
                print()
        print()
        print()
	
def upgradeStat(pkst):
	upgrade = ""
	skillUsed =""
	if(pkst == 0):
		upgrade = "Fast Feet"	
	if(pkst == 1):
		upgrade = "Rocket Arm"
	if(pkst == 2):
		upgrade = "Sweet Touch"
	if(pkst == 3):
		upgrade = "IQ Boost"
	if(pkst == 4):
		upgrade = "Careful Hands"
	if(pkst == 5):
		upgrade = "Ice In Veins"
	print("Would you like Sims to use one of his available skills?")
	print("Remember skills can only be used once")
	while "x" == "x":
		yesOrNo = input(("Type | 1 | to use a skill \nType | 2 | to not use a skill.\nType | 3 | to view current skills.\n"))
		if(yesOrNo == "2"):
			break
		elif(yesOrNo == "1"):
			if(len(skills) == 0):
				print("You have no sklls to use")
				break
			else:
				print("Your current skills are: ")
				SimsSkills()
				print("Pick wisely as your skills correspond to certain attributes.")
				print("A wrong choice will waste the skill")
				while "y" == "y" :
					skillUsed = input(("Type out the exact wording of the skill you wish to use"))
					if skillUsed == upgrade:
						print(str(upgrade) + " Has been applied to your attributes")
						skills.remove(upgrade)
						SimsStats()
						print()
						return 15
						break
					elif str(skillUsed) in skills:
						print("This skill does not apply to the attribute you are using")
						print("Sims has wasted his skill")
						skills.remove(skillUsed)
						return 0
						break			
					else:
						print("Enter a valid skill")
			break
		elif(yesOrNo == "3"):
			SimsSkills()
		else:
			print("Please enter a valid skill")
	return 0



def SpeedOptions():
	selectedStat = Options()
	num = 1
	if (selectedStat == 0):
		print("Sims has made the right choice to use his quick feet!")
		additionalBoost = int(upgradeStat(selectedStat))
		num = int(stats[selectedStat]) + additionalBoost
	else:
		print("Sims has made the wrong choice. Surely this won't end well")
		print()
	return num


def TPOptions():
	selectedStat = Options()
	num = 1
	if (selectedStat == 1):
		print("Sims has made the right choice to use his cannon of an arm!")
		additionalBoost = int(upgradeStat(selectedStat))
		num = int(stats[selectedStat]) + additionalBoost
	else:
		print("Sims has made the wrong choice. Surely this won't end well")
		print()
	return num

def TAOptions():
	selectedStat = Options()
	num = 1
	if(selectedStat == 2):
		print("Sims has made the right choice to use his pinpoint accuracy!")
		additionalBoost = int(upgradeStat(selectedStat))
		num = int(stats[selectedStat]) + additionalBoost
	else:
		print("Sims has made the wrong choice. Surely this won't end well")
		print()
	return num

def DMOptions():
	selectedStat = Options()
	num = 1
	if(selectedStat == 3):
		print("Sims has made the right choice to use his brains on this play!")
		additionalBoost = int(upgradeStat(selectedStat))
		num = int(stats[selectedStat]) + additionalBoost
	else:
		print("Sims has made the wrong choice. Surely this won't end well")
		print()
	return num


def BSOptions():
	selectedStat = Options()
	num = 1
	if(selectedStat == 4):
		print("Sims has made the right choice of making sure to try and not turn over the ball this play!")
		additionalBoost = int(upgradeStat(selectedStat))
		num = int(stats[selectedStat]) + additionalBoost
	else:
		print("Sims has made the wrong choice. Surely this wont end well")
		print()
	return num

def ClutchOptions():
	selectedStat = Options()
	num = 1
	if(selectedStat == 5):
		print("Sims has made the right choice to try and clutch up in this pivotal moment")
		additionalBoost = int(upgradeStat(selectedStat))
		num = int(stats[selectedStat]) + additionalBoost
	else:
		print("Sims has made the wrong choice. Surely this wont end well")
		print()
	return num

def Options():
	print("Current attributes are as follows: ")
	SimsStats()	
	print("Which one should Sims use?")
	while "x" == "x":
		choice = input(("Type | 0 | to use Speed\nType | 1 | to use Throw Power\nType | 2 | to use Throw Accuracy\nType | 3 | to use Decision Making\nType | 4 | to use Ball Safety\nType | 5 | to use Clutch"))
		if (choice == "0" or choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5"):
			choice == int(choice)
			break
		else:
			print("Enter a valid option")
	return int(choice)
# The following random in game scenerios will happen to Sims throughout the season these will have options for Sims to pick with the ability to use special attributes

def Scenerio():
	x = random.randint(1, 18)
	if (x == 1):
		print("Sims is faced against a tackler on the edge. What should he do?")
		print()
		num = SpeedOptions()
		if(num >= 73):
			print("Sims was able to outrun the tackler!\n")
			return 1
		else:
			print("The tackler was able to bring down Sims.\n")
			return -1
	if (x == 2):
		print("Sims is stuck in the pocket but sees a narrow lane. What should he do?")
		print()
		num = SpeedOptions()
		if(num >= 77):
			print("Sims was able to run through the gap in tha pocket and rush for 20 yards!\n")
			return 1
		else:
			print("Sims gets sacked from behind as he was not fast enough.\n")
			return -1			
	if (x == 3):
		print("Sims is up against two top defenders in the nation and must somehow make it between them. What should he do?")
		print()
		num = SpeedOptions()
		if(num >= 82):
			print("Sims runs right between the defenders and rushes for a toucdown!\n")
			return 1
		else:
			print("Sims is not fast enough to run past the defenders, gets rocked, and fumbles the ball.\n")
			return -1
	if (x == 4):
                print("Sims has an open reciever 25 yards down the field running down the sideline. What should he do?")
                print()
                num = TPOptions()
                if(num >= 73):
                        print("Sims rifles the ball to the open man for a 25 yard gain!\n")
                        return 1
                else:
                        print("Sims can't get the ball to the reciever as he is too weak.\n")
                        return -1
	if (x == 5):
                print("Sims has a slightly covered reciever 35 yards down the middle of the field. What should he do?")
                print()
                num = TPOptions()
                if(num >= 77):
                        print("Sims is able to get the ball to the reciever. What a throw!\n")
                        return 1
                else:
                        print("Sims' throw comes up short.\n")
                        return -1
	if (x == 6):
                print("Sims has a reciever 55 yards down the field who is beating his defender. What should he do?")
                print()
                num = TPOptions()
                if(num >= 82):
                        print("Sims lazers the ball to the open man and he scores a Touchdown!\n")
                        return 1
                else:
                        print("Sims throws the ball short and the defender intercepts the pass.\n")
                        return -1
	if (x == 7):
                print("Sims has to throw a simple wide open screen. What should he do?")
                print()
                num = TAOptions()
                if(num >= 73):
                        print("Sims is able to get the ball in the hands of the running back and the screen works for 10 yards!\n")
                        return 1
                else:
                        print("Sims can't even throw a simple screen and the fans start to boo him.\n")
                        return -1
	if (x == 8):
                print("Sims has to sneak a throw in above the linebackers over the middle on an RPO. What should he do?")
                print()
                num = TAOptions()
                if(num >= 77):
                        print("Sims is able to fit the ball over the linebackers for a 25 yard gain!\n")
                        return 1
                else:
                        print("Sims throws the ball right to the linebacker and he picks it off.\n")
                        return -1
	if (x == 9):
                print("Sims sees a reciever that has an open window 20 yards down the field covered by two defenders. What should he do?")
                print()
                num = TAOptions()
                if(num >= 82):
                        print("Sims fits the ball through the narrow gap, both defenders collide, and the reciver runs for a touchdown!\n")
                        return 1
                else:
                        print("Sims misses his reciever by a mile right into the hands of the defender who picks the ball off and returns it for a touchdown.\n")
                        return -1
	if (x == 10):
                print("Sims has 10 seconds left and must spike the football. What should he do?")
                print()
                num = DMOptions()
                if(num >= 73):
                        print("Sims spikes the ball allowing the offense to run another play!\n")
                        return 1
                else:
                        print("Sims is so dumb he takes a knee and the clock runs out.\n")
                        return -1
	if (x == 11):
                print("Sims has to decide between throwing a double coverage pass or running through an open gap in the rush. What should he do?")
                print()
                num = DMOptions()
                if(num >= 77):
                        print("Sims takes off and picks up a first down. The crowd goes ballistic!\n")
                        return 1
                else:
                        print("Sims throws the ball right ino double coverage which gets picked off.\n")
                        return -1
	if (x == 12):
                print("Sims sees a reciever who only appears to be open in the middle of the field. What should he do?")
                print()
                num = DMOptions()
                if(num >= 82):
                        print("Sims decides to just throw the ball away. Good choice there was a safety there the entire time!\n")
                        return 1
                else:
                        print("Sims doesn't see the safety lurking in the middle of the field who picks him off.\n")
                        return -1
	if (x == 13):
                print("Sims needs to cleanly recieve a snap. What should he do?")
                print()
                num = BSOptions()
                if(num >= 73):
                        print("Sims cleanly recieves the snap!\n")
                        return 1
                else:
                        print("Sims fumbles the snap and the defense recovers the ball!\n")
                        return -1
	if (x == 14):
                print("Sims gets tackled by a star linebacker. What should he do?")
                print()
                num = BSOptions()
                if(num >= 77):
                        print("Sims makes sure to protect the ball and goes dowm without fumbling!\n")
                        return 1
                else:
                        print("Sims gets hit sticked by the linebacker and fumbles the ball.\n")
                        return -1
	if (x == 15):
                print("Sims sees a narrow windowed reciever in the endzone but cant turn the ball over. What should he do?")
                print()
                num = BSOptions()
                if(num >= 82):
                        ("Sims throws the ball to the reciever fitting it through the defenders and doesn't turn it over. Touchdown!\n")
                        return 1
                else:
                        ("Sims rifles the ball to the reciever, but it is picked off by the cornerback.\n")
                        return -1
	if (x == 16):
                print("Sims has 15 seconds left in the half and the defender bites on the runningback on the read option. What should he do?")
                print()
                num = ClutchOptions()
                if(num >= 73):
                        print("Sims decides to hold onto the ball and runs for 15 yards and gets out of bounds after!\n")
                        return 1
                else:
                        print("Sims hands the ball off to the runningback who gets easily tackled.\n")
                        return -1
	if (x == 17):
                print("Sims has to lead Nebraska on a 2 minute drive to score at half. What should he do?")
                print()
                num = ClutchOptions()
                if(num >= 77):
                        print("Sims leads Nebraska down the field and they score a touchdown!\n")
                        return 1
                else:
                        print("Sims fails to lead Nebraska down the field and they have a turnover on downs.\n")
                        return -1
	if (x == 18):
                print("Sims has defenders all around him with 3 seconds left on the clock, but sees a reciever in single coverage in the endzone.\nWhat should he do?")
                print()
                num = ClutchOptions()
                if(num >= 82):
                        print("Sims is able to juke out both defenders and hit his man in the endzone. Touchdown! The stadium is electric!\n")
                        return 1
                else:
                        print("Sims is not able to complete the pass. Time runs out.\n")
                        return -1
	return 0
#Practice Facility Sims is able to move around in to train


def Facility():
	while "x" == "x":
		choice = (input(("Sims has entered the Nebraska Practice Facility.\nType | 1 | to enter the Weight Room.\nType | 2 | to enter the Practice Field.\nType | 3 | to enter the Film Room.\nType | 4 | to skip practice for the day.")))
		if choice == "1":
			WeightRoom()
			break
		elif choice == "2":
			PracticeField()
			break
		elif choice == "3":
			FilmRoom()
			break
		elif choice == "4":
			Skip()
			break
		else:
			print("Please enter a valid option")
		
#Weight Room for Sims to train at

#Returns a random upgrade to his stats

def Upgrade():
	return random.randint(2, 5)
#Returns a random downgrade too his stats

def DownGrade():
	return random.randint(1, 3)

#gives a random skill that sims can use later
def WhatSkill():
	num = random.randint(1, 6)
	if(num == 1):
		skills.append("Rocket Arm")
		print("Sims has gained Rocket Arm")
		print()
	if(num == 2):
		skills.append("Sweet Touch")
		print("Sims has gained Sweet Touch")
		print()
	if(num == 3):
		skills.append("Fast Feet")
		print("Sims has gained Fast Feet")
		print()
	if(num == 4):
		skills.append("IQ Boost")
		print("Sims has gained IQ Boost")
		print()
	if(num == 5):
		skills.append("Careful Hands")
		print("Sims has gained Careful Hands")
		print()
	if(num == 6):
		skills.append("Ice In Veins")
		print("Sims has gained Ice In Veins")
		print()
		

def WeightRoom():
	print("Sims has decided to work in the weight room today.")
	x = Upgrade()
	y = Upgrade()
	stats[0] += x
	stats[1] += y
	print("Sims has improved his Speed and Throw Power lifting today!")
	print("Speed +" + str(x) + " , Throw Power +" + str(y))
	SimsStats()
	num = random.randint(1, 3)
	if(num == 3):
		WhatSkill()
	else:
		print("Sims has not gained any skills")
	print()
#What happens if you skip practice

def Skip():
	print("Sims has stupidly decided to skip practice today.")
	for loop in range(0, len(stats), 1):
		stats[loop] -= DownGrade()
	print("All of Sims' stats have digressed! lol")
	SimsStats()
	print()	
	
#Practice field for Sims to train at

def PracticeField():
	print("Sims has decided to work out at the practice field today.")
	x = Upgrade()
	y = Upgrade()
	stats[2] += x
	stats[4] += y
	print("Sims has improved his Throw Accuracy and Ball Safety while practicing today!")
	print("Throw Acuuracy +" + str(x) + " , Ball Safety +" + str(y))
	SimsStats()
	num = random.randint(1, 3)
	if(num == 3):
		WhatSkill()
	else:
		print("Sims has not gained any skills")
	print()

#Film Room for Sims to study at

def FilmRoom():
	print("Sims has decided to study film today.")
	x = Upgrade()
	y = Upgrade()
	stats[3] += x
	stats[5] += y
	print("Sims has improved his Decision Making and Clutch while studying film today!")
	print("Decision Making +" + str(x) + " , Clutch +" + str(y))
	SimsStats()
	num = random.randint(1, 3)
	num = random.randint(1, 3)
	if(num == 3):
		WhatSkill()
	else:
		print("Sims has not gained any skills")
	print()
#Will Execute if Sims losess the starting Job and ends the game

def Lose():
	print("You have lost the starting job to the backup QB Heinrich Haarberg! Have fun rotting on the bench!")
	print("GAME OVER")

#prints Nebraskas Current Record

def Record():
	print("Nebraska's current record is " + str(currentRecord[0]) + " - " + str(currentRecord[1]))
#prints Nebraskas final record

def FinalRecord():
	print("Nebraska's final record is " + str(currentRecord[0]) + " - " + str(currentRecord[1]))   

print()	
print("Every week Sims will have three days to train his attributes before every game in order to help him win football games\nor maybe possibly get special skills.\nYou will have the choice of where to train in order to develop specific attributes.\nBe careful not to lose too many games as backup QB Haarberg will replace you\nand you will lose the game rotting on the bench for the rest of your career!")

print()
print("Starting attributes are as follows: ")
SimsStats()

print()
print("Starting special skills are as follows.\nMake sure to remember you can use each skill only one over the course of the season!\nYou may have duplicates of a certain skill as its only natural because football players repeat certain moves!:")
SimsSkills()

while "x" == "x":
	Minnesota()
	Colorado()
	NorthernIllinois()
	LouisianaTech()
	if(currentRecord[1] >= 3):
		Lose()
		break
	Michigan()
	Illinois()
	if(currentRecord[1] >= 4):
		Lose()
		break
	Bye()
	NorthWestern()
	Purdue()
	if(currentRecord[1] >= 5):
		Lose()
		break
	MichiganState()
	Maryland()
	if(currentRecord[1] >= 6):
		Lose()
		break
	Wisconsin()
	Iowa()
	if(currentRecord[0] >= 10):
		if(BigTenChampionShip() == 1):
			if(SemiFinals() == 1):
				if(ChampionshipGame() == 1):
					print("Congratulations on your historic season!")
					print("The Huskers are building a statue of Sims outside the stadium. All is right in the world")
					print("You will go down in the history books as one of the greatest to ever do it.")
					FinalRecord()
					print("GAME OVER")
					break			
				else:
					print("So Close! This will still go down in history as one of the greatest seasons of all time for the Huskers")
					print("A legacy season for Sims!")
					FinalRecord()
					print("GAME OVER")
					break
			else:
				print("Leading Nebraska to their first CFP appearance ever is nothing to be sad about")
				print("Sims will go down in Husker history as the best QBs ever for their current situation")
				FinalRecord()
				print("GAME OVER")
				break
		else:
			if(BowlGame() == 1):
				print("Congrats on your amazing season with Sims. He did far better than anyone expected.")
				FinalRecord()
				print("GAME OVER")
				break
			else:
				print("What a season but sadly you have come just short of a bowl win.")
				FinalRecord()
				print("GAME OVER")
				break
			
	elif(currentRecord[0] >= 6):
		if(BowlGame() == 1):
			print("Congrats on your amazing season with Sims. He did far better than anyone expected.")
			FinalRecord()
			print("GAME OVER")
			break
		else:
			print("What a season but sadly you have come just short of a bowl win.")
			FinalRecord()
			print("GAME OVER")
			break
	else:
		print("Sims and the Huskers have failed to make a bowl game!")
		print("Rhule has asked you to transfer. Have fun at South Dakota State University!")
		FinalRecord()
		print("GAME OVER")
		break
			









