import pandas


def not_blank(question):
    """checks that the user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in. \n to try again")


def num_checker(question, num_type="float", exit_code=None):
    """Checks users enter an integer / float that is more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter a number more than 0"

    while True:

        response = input(question)

        # checks for exit code and returns it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that number
        # is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type, how_many):
    """Gets variables /  fixed expenses and outputs panda
    (as a string) and a subtotal of the expenses"""

    # Lists for panda

    all_items = []
    all_amounts = []
    all_costs = []

    # Expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "Cost": all_costs
    }

    # default amount to 1 for fixed expenses and
    # to avoid PEP 8 error for variable expenses
    amount = 1

    # loop to get expenses
    while True:

        # Get item name and check its mot blank
        item_name = not_blank("Item Name: ")

        # checks users enter at least one variable expenses
        # NOTE: If

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

quantity_made = num_checker("Quantity being made: ",
                            "integer")
print()

print("Getting Variable Costs,,,")
variable_expenses = get_expenses("variable", quantity_made)
print()
print(variable_expenses)
