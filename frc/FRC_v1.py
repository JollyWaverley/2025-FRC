import pandas
from tabulate import tabulate
from datetime import date


def generate_statement(statement, decoration, lines):
    """will make the headings (3 lines), subheadings(2 lines) and emphasised text / mini-heading (1 line).
       Only use emoji for single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottem = decoration * len(middle)

    if lines == 1:
        return middle
    elif lines == 2:
        two_lines = f"{middle}\n {top_bottem}"
        return two_lines

    else:
        print(top_bottem)
        print(middle)
        print(top_bottem)
        return None


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        if response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


def instructions():
    print('''
====== Instructions ========

Instructions go here...
    ''')

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

# initialise variables...

# assume we have no fixed expenses for now
fixed_subtotal = 0
fixed_panda_string = ""

print(generate_statement("Fund raising Calculator", "🪙",1))
want_instruction = yes_no("do you want to see instructions?")
print()

if want_instruction == "yes":
    instructions()

# get product details
product_name = not_blank("Product Name: ")
quantity_made = num_checker("Quantity being made: ", "integer")

print("Let's get the Variable expenses....")
variable_expenses = get_expenses("variable", quantity_made)

# retrieve panda and subtotal from results of function
variable_panda_string = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print("panda string: ", variable_panda_string)
print("variable subtotal: ", variable_subtotal)

# ask user if they have fixed expenses and retrieve them
print()
has_fixed = yes_no("do you have fixed expenses? ")

if has_fixed == "yes":
    fixed_expenses = get_expenses("fixed")

    fixed_panda_string = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

    # If the user has not entered any fixed expenses,
    # Set panda to "" so that it does not display!
    if fixed_subtotal == 0:
        has_fixed = "no"
    fixed_panda_string = ""

print("variable expenses: ", variable_expenses)
print("fixed subtotal: ", fixed_subtotal)

total_expenses = variable_subtotal + fixed_subtotal
total_expenses_string = f"Total Expenses: ${total_expenses:.2f}"

# Get profit Goal here.

# strings / output area

# **** Get current date for heading and filename ****
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# headings / strings...
main_heading_strings = get_expenses("Fund raising Calculator"
                                    f"({product_name}, {day}/{month}/{year})", "=")
quantity_string = f"Quantity being made: {quantity_made}"
variable_heading_string = generate_statement("Variable", "-")
variable_subtotal_string = f"Variable Expenses Subtotal: ${variable_subtotal:.2f}"

# set up strings if we have fixed costs
if has_fixed == "yes":
    fixed_heading_string = generate_statement("Fixed Expenses", "-")
    fixed_subtotal_string = f"Fixed expenses Subtotal: {fixed_subtotal}"
# set fixed cost strings to blank if we don't have fixed costs
else:
    fixed_heading_string = generate_statement("You have no fixed Expenses", "-")
    fixed_subtotal_string = "Fixed expenses subtotal $0.00"

# List of strings to be outputted / written to ile
to_write = [main_heading_strings, quantity_string,
            "\n", variable_heading_string, variable_panda_string,
            variable_subtotal_string,
            "\n", fixed_heading_string, fixed_panda_string,
            fixed_subtotal_string, total_expenses_string]

# Print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = f"{product_name}_{year}_{month}_{day}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "W+")

# write the item item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
