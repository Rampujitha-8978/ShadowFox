import random

rolls = []
count_6 = 0
count_1 = 0
two_sixes_in_row = 0

previous = None

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        count_6 += 1
        if previous == 6:
            two_sixes_in_row += 1

    if roll == 1:
        count_1 += 1

    previous = roll

print("Dice rolls:", rolls)
print("Number of times rolled 6:", count_6)
print("Number of times rolled 1:", count_1)
print("Number of times two 6s in a row:", two_sixes_in_row)
total_jumping_jacks = 100
completed = 0

for i in range(1, 11):   # 10 sets of 10 jumping jacks
    completed += 10
    remaining = total_jumping_jacks - completed

    answer = input("You completed 10 jumping jacks. Are you tired? (yes/y or no/n): ").lower()

    if answer == "yes" or answer == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print(f"You completed a total of {completed} jumping jacks.")
            break

    if remaining > 0:
        print(f"{remaining} jumping jacks remaining.")

    if completed == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break
