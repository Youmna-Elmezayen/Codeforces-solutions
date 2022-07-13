def checkWinner(gesture1, gesture2, gesture3):
    if gesture1 == "rock": # the only way rock will win is if both the other gestures are scissors
        if gesture2 == "scissors" and gesture3 == "scissors":
            return True
        else:
            return False
    elif gesture1 == "paper": # the only way paper will win is if both the other gestures are rock
        if gesture2 == "rock" and gesture3 == "rock":
            return True
        else:
            return False
    elif gesture1 == "scissors": # the only way scissors will win is if both the other gestures are paper
        if gesture2 == "paper" and gesture3 == "paper":
            return True
        else:
            return False

gestureF = input()
gestureM = input()
gestureS = input()

if checkWinner(gestureF, gestureM, gestureS):
    print("F")
elif checkWinner(gestureM, gestureF, gestureS):
    print("M")
elif checkWinner(gestureS, gestureM, gestureF):
    print("S")
else:
    print("?")