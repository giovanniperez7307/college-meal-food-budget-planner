# College Meal and Food Budget Planner
# Group Members: Gio, A.J., Jay

# Grocery items and prices
groceries = {
    "Rice": 4.50,
    "Eggs": 3.50,
    "Chicken": 8.50,
    "Frozen Vegetables": 2.50,
    "Bananas": 1.60,
    "Pasta": 1.80,
    "Bread": 2.50,
    "Milk": 3.00,
    "Beans": 1.50,
    "Yogurt": 2.00
}

# Meal names and prices
meals = {
    "Beans and Rice Bowl": 1.75,
    "Egg and Toast": 1.50,
    "Pasta with Tomato Sauce": 2.10,
    "Peanut Butter Banana Toast": 1.35,
    "Chicken and Rice": 2.85,
    "Tuna Sandwich": 2.25,
    "Yogurt and Oats": 1.65
}

budget = 0
shopping_list = []
meal_plan = []


# Set the weekly budget
def set_budget():
    global budget
    budget = float(input("Enter your weekly budget: $"))
    print("Budget set to $", budget)


# Calculate grocery spending
def calculate_total():
    total = 0

    for item in shopping_list:
        total = total + groceries[item]

    return total


# Add a grocery item
def add_grocery():
    print(groceries)
    item = input("Enter an item: ").title()

    if item in groceries:
        shopping_list.append(item)
        print(item, "added to your list.")
    else:
        print("Item not found.")


# Remove a grocery item
def remove_grocery():
    item = input("What item do you want to remove? ").title()

    if item in shopping_list:
        shopping_list.remove(item)
        print(item, "removed.")
    else:
        print("Item not found.")


# Show grocery list and budget
def show_groceries():
    print("\nYour Grocery List:")

    for item in shopping_list:
        print(item, "- $", groceries[item])

    total = calculate_total()

    print("Total spent: $", round(total, 2))
    print("Money remaining: $", round(budget - total, 2))


# Bubble Sort: organize groceries by price
def sort_groceries():
    items = shopping_list.copy()

    for i in range(len(items)):
        for j in range(len(items) - 1):

            if groceries[items[j]] > groceries[items[j + 1]]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp

    print("\nGroceries from cheapest to most expensive:")

    for item in items:
        print(item, "- $", groceries[item])


# Greedy Algorithm: choose affordable meals
def affordable_meals():
    amount = float(input("Enter your meal budget: $"))

    # Sort meals from cheapest to most expensive
    meal_names = list(meals.keys())

    for i in range(len(meal_names)):
        for j in range(len(meal_names) - 1):

            if meals[meal_names[j]] > meals[meal_names[j + 1]]:
                temp = meal_names[j]
                meal_names[j] = meal_names[j + 1]
                meal_names[j + 1] = temp

    total = 0

    print("\nAffordable meals:")

    # Add meals while they fit the budget
    for meal in meal_names:
        if total + meals[meal] <= amount:
            print(meal, "- $", meals[meal])
            total = total + meals[meal]

    print("Total: $", round(total, 2))
    print("Remaining: $", round(amount - total, 2))


# Add meals to weekly meal plan
def add_meal():
    print("\nAvailable Meals:")

    for meal in meals:
        print(meal, "- $", meals[meal])

    choice = input("Enter a meal: ").strip()

    if choice in meals:
        meal_plan.append(choice)
        print("Meal added.")
    else:
        print("Meal not found.")


# Show weekly meal plan
def show_meals():
    total = 0

    print("\nYour Weekly Meal Plan:")

    for meal in meal_plan:
        print(meal, "- $", meals[meal])
        total = total + meals[meal]

    print("Total meal cost: $", round(total, 2))


# Main program menu
while True:

    print("\n===== COLLEGE FOOD BUDGET PLANNER =====")
    print("1. Set Budget")
    print("2. Add Grocery")
    print("3. Remove Grocery")
    print("4. View Grocery List")
    print("5. Sort Groceries")
    print("6. Find Affordable Meals")
    print("7. Add Meal to Plan")
    print("8. View Meal Plan")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        set_budget()

    elif choice == "2":
        add_grocery()

    elif choice == "3":
        remove_grocery()

    elif choice == "4":
        show_groceries()

    elif choice == "5":
        sort_groceries()

    elif choice == "6":
        affordable_meals()

    elif choice == "7":
        add_meal()

    elif choice == "8":
        show_meals()

    elif choice == "0":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice.")
