friends = ["Aditya", "Rohit", "Sneha", "Kiran", "Pooja"]

friends_tuples = []

for name in friends:
    friends_tuples.append((name, len(name)))

print("Friends and name lengths:")
print(friends_tuples)
# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner total expenses:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount.")

# Category with highest difference
max_diff = 0
category = ""

for key in your_expenses:
    diff = abs(your_expenses[key] - partner_expenses[key])
    if diff > max_diff:
        max_diff = diff
        category = key

print("Category with highest spending difference:", category)
print("Difference amount:", max_diff)
