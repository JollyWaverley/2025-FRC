def not_blank(question):
    """checks that the user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in. \n to try again")


def num_checker(question, num_type="float"):
    """Checks users enter an integer / float that is more than zero"""

    error = "Please enter a number more than zero."

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type):
    """Gets variables /  fixed expenses and outputs panda
    (as a string) and a subtotal of the expenses"""

    # Lists for panda
    all_items: list[str] = []

    # Expenses dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        # checks users enter at least on variable expense
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("Oops you have not entered anything.    "
                  "You need at least one item.")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

    # return all the item for now so we can check the loop.
    return all_items


# Main routine starts here

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable")
num_variable = len(variable_expenses)
print(f"You entered {num_variable} items")
print()

print("Getting Fixed Costs...")
fixed_expenses = get_expenses("fixed")
num_fixed = len(fixed_expenses)
print(f"You entered {num_fixed} items")
