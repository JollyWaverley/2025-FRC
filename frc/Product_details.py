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


def not_blank(question):
    """checks that the user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in. \n to try again")


def get_expenses(exp_type):
    """Gets variables /  fixed expenses and outputs panda
    (as a string) and a subtotal of the expenses"""

    # Lists for panda
    all_items = []

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
    return  all_items


# Main routine goes heer

# loop for testng purposes
while True:
    product_name = not_blank("Product Name: ")
    quantity_made = num_checker("Quantity being made: ", "integer")
    print(f"You are making {quantity_made} {product_name}")
    print()
