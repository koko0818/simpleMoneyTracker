def main():
    categories = {
        "salary": 0.0,
        "other income": 0.0,
        "food": 0.0,
        "rent/utilities": 0.0,
        "transportation": 0.0,
        "hobby": 0.0
    }

    while True:
        try:
            action = int(input("""Enter a number of action you want to implement:
            1. track an expense or income
            2. see the totals by category
            3. see the overall balance
            Or, enter 0 to exit.
            """))

            if action == 1:
                track(categories)

            elif action == 2:
                category(categories)

            elif action == 3:
                print(f"The current overall balance is ${balance(categories)}")
            elif action == 0:
                break
        except ValueError:
            print("Your input is not an integer")
            pass

def track(categories):
    try:
        print("Current categories are", ', '.join(categories))
        category = input("Enter a category you want to record the expense/income for: ")
        amount = float(input("Enter the amount as negative if it's an expense, positve if it's income: "))
        categories[category.lower()] += amount
        return categories
    except KeyError:
        print("Please enter an existing category")
        raise
    except ValueError:
        print("Enter a positive or negative number")
        raise

def category(categories):
    for k, v in categories.items():
        print(f"{k}: ${v}")
    while True:
        answer = input("Would you like to add another category? Y(Yes) / N(No) ")
        try:
            if answer.lower() == "y" or answer.lower() == "yes":
                new_category = input("Category name: ")
                categories[new_category] = 0
                return categories
            elif answer.lower() == "n" or answer.lower() == "no":
                print("Keeping the categories as they are")
                return categories
            else:
                raise ValueError("invalid input")
        except AttributeError:
            print("invalid input")
            raise

def balance(categories):
    # sum all the totals within the dictionary
    return sum(categories.values())

if __name__ == "__main__":
    main()