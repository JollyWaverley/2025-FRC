import pandas
from tabulate import tabulate


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


def get_expenses(exp_type, how_many=1):
    """Gets variables /  fixed expenses and outputs panda
    (as a string) and a subtotal of the expenses"""

    # Lists for panda

    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # Expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / item": all_dollar_per_item
    }

    # default amount to 1 for fixed expenses and
    amount = how_many  # how_many defaults to 1

    # loop to get expenses
    while True:

        # Get item name and check its mot blank
        item_name = not_blank("Item Name: ")

        # checks users enter at least one variable expenses
        # NOTE: If you type the conditions without the brackets,
        # all on one line and then add in the enters,
        # Pycharm will add in the brackets automatically

        # checks users enter at least on variable expense
        if (exp_type == "variable" and item_name == "xxx") and len(all_items) == 0:
            print("Oops you have not entered anything.    "
                  "You need at least one item.")
            continue

        elif item_name == "xxx":
            break

        # Get item amount for variable expenses <enter> defaults to number of
        # products being made.

        if exp_type == "variable":

            # get amount
            amount = num_checker(f"How many, press <enter> for {how_many}",
                                 "integer", exit_code="")

            if amount == "":
                amount = how_many

        how_much_question = "Price for one? $"

        # Get price for one item (question customised depending on expense type).
        price_for_one = num_checker(how_much_question, "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)

    # make panda
    expenses_frame = pandas.DataFrame(expenses_dict)

    # calculate Row cost
    expenses_frame['Cost'] = expenses_frame['Amount'] * expenses_frame['$ / item']

    # calculate sub total
    subtotal = expenses_frame['Cost'].sum()

    # Apply currency formatting to currency columns.
    add_dollars = ['Amount', '$ / item', 'Cost']
    for var_item in add_dollars:
        expenses_frame[var_item] = expenses_frame[var_item].apply(currency)

    # make expenses frame into a string with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expenses_frame, headers='keys',
                                  tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expenses_frame[['Item', 'Cost']], headers='keys',
                                  tablefmt='psql', showindex=False)

    # return the expenses panda and subtotal
    return expense_string, subtotal


def currency(x):
    """formats number as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main routine starts here

quantity_made = num_checker("Quantity being made: ",
                            "integer")
print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print("Getting fixed costs...")
fixed_expenses = get_expenses("fixed")
print()
fixed_panda = fixed_expenses[0]
fixed_subtotal = fixed_expenses[1]

# Temporary output area (for easy testing)

print("=== Variable Expenses ===")
print(variable_panda)
print(f"Variable subtotal: ${variable_subtotal:.2f}")
print()

print("=== Fixed expenses ===")
print(fixed_panda)
print(f"Fixed subtotal: ${fixed_subtotal:.2f}")

total_expenses = variable_subtotal + fixed_subtotal
print(f"Total Expenses: ${total_expenses:.2f}")
