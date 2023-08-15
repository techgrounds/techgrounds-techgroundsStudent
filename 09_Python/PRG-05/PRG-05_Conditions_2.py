#Ask the user of your script for a number. Give them a response based on whether the number is higher than, lower than, or equal to 100.
EIS = int(input("Waar zit je aan te denken?"))

if EIS > 100:
    print("Op wat voor site heb jij zitten snuffelen? Per uur?? Tot ziens")
elif EIS < 100:
    print("Dit kan ik voor je regelen. Bel HR maar en ze zullen een en ander naar je faxen")
else:
    print("Warempel, Dat zijn geen peanuts! Goed, bel HR en dan gaan ze je wat faxen.")
