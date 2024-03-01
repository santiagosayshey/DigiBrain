import random

flips = int(input("How many iterations: "))
print("Running " + str(flips) + " iterations")

heads=tails=0
for i in range(flips):
    throw = random.randint(1,2)
    if throw == 1:
        heads += 1
    else:
        tails += 1

print("Heads: " + str(heads) + " (" + format((heads/flips)*100, '.2f') + "%)")
print("Tails: " + str(tails) + " (" + format((tails/flips)*100, '.2f') + "%)")