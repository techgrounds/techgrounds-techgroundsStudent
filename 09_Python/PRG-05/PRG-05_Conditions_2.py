#Ask the user of your script for a number. Give them a response based on whether the number is higher than, lower than, or equal to 100.
EIS = int(input("Aan wat voor getal moet ik dan denken, als ik met jou in zee ga?"))
if EIS > 100:
    print("Op wat voor site heb jij zitten snuffelen? Per uur?? Tot ziens.")
elif EIS < 100:
    print("Dit kan ik voor je regelen. Bel HR maar en ze zullen een en ander naar je faxen.")
else:
    print("Warempel, Daar schrik ik wel van! Goed, bel HR en dan gaan ze je wat faxen.")
