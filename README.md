 # Simple Money Tracker
    #### Description:
    I made a money tracker that is simple. I find it difficult to be consistent with money tracking so I wanted to make a program that is straightfoward to use and easy to keep up with. \n
    It consists of main and three other functions. \n
    The main functions firstly asks the user to choose an action they want to proceed with. \n
    There are four options:
    1. track an expense or income
    2. see the toals by category
    3. see the overall balance.
    Or 0 to quit.
    Each function is called base on which integer user has input, if it's not 1, 2, 3, or 0, it will go back to showing the options. If the input is 0, the program will terminate. \n
    Now, the first function prints the current dictionary of expenses and incomes. It will add a new record with the category the user chooses and amount. User should input a positive number if it's an income and a negative number if it's an expense.
    I made it in try except blocks function so the function will throw an error if the category does not exist in the current dictionary or the amount is not a number and go back to asking for an input. \n
    The second function is called category and it prints all the categories and the corresponding amount recored so far. It will ask the user if they would like to add a new category and make it if they say yes. I also made this function in try except so it will throw an error if they don't answer with yes, no, y or n, and go back to asking user for an input. \n
    Lastly, the last function will simply return the overall sum of all values recorded in the dictionary so far. \n