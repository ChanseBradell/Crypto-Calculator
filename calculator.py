import sys


def calculate_values():
    initial_value = bought_amount * buy_price
    sold_value = sold_amount * sell_price
    remaining_units = bought_amount - sold_amount
    remaining_units_value = remaining_units * sell_price
    profit = (sold_value + remaining_units_value) - initial_value
    return initial_value, sold_value, remaining_units, remaining_units_value, profit


def print_profit_information():
    print("""\n\n\n
    {0} units were purchased at a price of {1} each for a total price of {2}.
    {3} units were sold at a price of {4} each for a total price of {5}.
    {6} units remain and hold an approximate value of {7} each for a total value of {8} if valued at the sale price.
    
    The total current value including any remaining units is: {9}.
    The total profit from this transaction is {10}. 
    \n\n\n"""
          .format(bought_amount, buy_price, initial_value, sold_amount, sell_price, sold_value, remaining_units,
                  sell_price, remaining_units_value, (sold_value + remaining_units_value), profit))


def print_usage_instructions():
    print("""\n\n\n
        The specified input parameters are invalid.
    
        Parameters: <BUY PRICE> <BOUGHT AMOUNT> <SELL PRICE> <SOLD AMOUNT>
    
        Example usage: python calculator.py 100 10 200 5
        \n\n\n""")


def validate_args():
    pass


# If input parameters are specified, use them instead of prompting the user.
if len(sys.argv) == 5:
    args = [float(i) for i in sys.argv[1:]]
    buy_price, bought_amount, sell_price, sold_amount = args
# If the user tries to use the wrong amount of input parameters, prompt them with usage instructions.
elif 5 > len(sys.argv) > 1:
    print_usage_instructions()
    exit()
# Prompt the user for all needed information.
else:
    buy_price = float(input("Please input the buy price: "))
    bought_amount = float(input("Please input the bought amount: "))
    sell_price = float(input("Please input the sell price: "))
    sold_amount = float(input("Please input the sold amount: "))

# Do the calculations.
initial_value, sold_value, remaining_units, remaining_units_value, profit = calculate_values()
#Print the statistics.
print_profit_information()

