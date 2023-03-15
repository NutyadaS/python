score_input = input("Score? ")
score = int(score_input)

if score <50:
    print("F")
elif score <=64:
    print("D")
elif score <=74:
    print("C")
elif score <=84:
    print ("B")
else:
    print("A")
